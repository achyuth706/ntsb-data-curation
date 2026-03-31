"""
NTSB Aviation Accident Database — Extraction & Curation Pipeline
IS547 Foundations of Data Curation, Spring 2026

Reads one or more Microsoft Access (.mdb) archives from the NTSB public data
portal, extracts core relational tables and reference tables, applies
documented cleaning steps, merges across archives by natural key, and writes
provenance and data-quality logs.

Usage:
    # Process all .mdb files in data/raw/ (default, recommended)
    python scripts/ntsb_extract.py

    # Process a single file
    python scripts/ntsb_extract.py --input data/raw/up01DEC.mdb

Outputs:
    data/processed/<table>.csv      cleaned & merged core tables
    data/reference/<table>.csv      reference / lookup tables (from latest archive)
    logs/provenance.log             machine-readable per-run log (appended, JSON Lines)
    logs/curation_log.md            human-readable cumulative log (appended)
    logs/data_quality.md            data quality snapshot (overwritten per run)
"""

import os
import sys
import json
import argparse
import platform
from datetime import datetime, timezone

import pandas as pd
import pyodbc
import warnings
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=FutureWarning)


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

CORE_TABLES = [
    "events",
    "aircraft",
    "injury",
    "narratives",
    "Flight_Crew",
    "engines",
]

REFERENCE_TABLES = [
    "eADMSPUB_DataDictionary",
    "Country",
    "states",
    "ct_iaids",
    "ct_seqevt",
]

# Natural keys (post-normalization) used for cross-archive deduplication.
# Decision: an event is uniquely identified by ev_id; everything else
# describes attributes of an aircraft within an event, keyed by
# (ev_id, aircraft_key) plus a within-aircraft discriminator where needed.
TABLE_KEYS = {
    "events":       ["ev_id"],
    "aircraft":     ["ev_id", "aircraft_key"],
    "injury":       ["ev_id", "aircraft_key", "injury_level", "person_category"],
    "narratives":   ["ev_id", "aircraft_key"],
    "flight_crew":  ["ev_id", "aircraft_key", "crew_no"],
    "engines":      ["ev_id", "aircraft_key", "eng_no"],
}


def normalized_table_name(table):
    """Map original table name to its CSV / dict key (lowercase, snake_case)."""
    return "flight_crew" if table == "Flight_Crew" else table.lower()


# ---------------------------------------------------------------------------
# Database connection
# ---------------------------------------------------------------------------

def get_connection(mdb_path):
    """Open a pyodbc connection to a Microsoft Access .mdb file."""
    conn_str = (
        r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
        rf"DBQ={os.path.abspath(mdb_path)};"
    )
    return pyodbc.connect(conn_str)


def list_tables(conn):
    cursor = conn.cursor()
    return [row.table_name for row in cursor.tables(tableType="TABLE")]


def extract_table(conn, table_name):
    return pd.read_sql(f"SELECT * FROM [{table_name}]", conn)


# ---------------------------------------------------------------------------
# Cleaning
# ---------------------------------------------------------------------------

def normalize_columns(df):
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(r"[\s\-\/]+", "_", regex=True)
        .str.replace(r"[^\w]", "", regex=True)
    )
    return df


def clean_table(df):
    """Cleaning decisions:
       - Column names normalized to lowercase snake_case (cross-table joins).
       - String whitespace stripped (NTSB exports often have trailing spaces).
       - Exact duplicate rows dropped within a single archive.
       - Missing values are NOT dropped; preserved to keep limitations visible.
    """
    df = normalize_columns(df)
    str_cols = df.select_dtypes(include="object").columns
    if len(str_cols):
        df[str_cols] = df[str_cols].apply(lambda c: c.str.strip())
    before = len(df)
    df = df.drop_duplicates()
    return df, before - len(df)


def missing_summary(df):
    miss = df.isnull().sum()
    miss = miss[miss > 0]
    total = len(df) if len(df) else 1
    return {col: (int(n), round(n / total * 100, 1)) for col, n in miss.items()}


# ---------------------------------------------------------------------------
# Archive discovery & merge
# ---------------------------------------------------------------------------

def discover_archives(raw_dir):
    """Return .mdb paths sorted by mtime (oldest first).
    Sorting by mtime means the most recently modified archive's rows are
    appended last; drop_duplicates(keep='last') then retains the latest record.
    """
    if not os.path.isdir(raw_dir):
        raise FileNotFoundError(f"Raw directory not found: {raw_dir}")
    files = [
        os.path.join(raw_dir, f)
        for f in os.listdir(raw_dir)
        if f.lower().endswith(".mdb")
    ]
    if not files:
        raise FileNotFoundError(f"No .mdb files found in {raw_dir}")
    files.sort(key=os.path.getmtime)
    return files


def merge_with_dedup(frames, table_key):
    """Concat frames (already in mtime order) and dedupe by natural key."""
    if not frames:
        return pd.DataFrame(), 0
    merged = pd.concat(frames, ignore_index=True)
    key_cols = TABLE_KEYS.get(table_key)
    if key_cols and all(k in merged.columns for k in key_cols):
        before = len(merged)
        merged = merged.drop_duplicates(subset=key_cols, keep="last")
        return merged, before - len(merged)
    return merged, 0


# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------

def write_provenance_log(log_path, run_record):
    os.makedirs(os.path.dirname(log_path), exist_ok=True)
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(json.dumps(run_record, default=str) + "\n")


def write_curation_log(log_path, run_record):
    os.makedirs(os.path.dirname(log_path), exist_ok=True)
    new_file = not os.path.exists(log_path)
    with open(log_path, "a", encoding="utf-8") as f:
        if new_file:
            f.write("# Curation Log\n\n")
            f.write("Cumulative human-readable log of extraction runs. "
                    "Each entry corresponds to one execution of "
                    "`scripts/ntsb_extract.py`.\n\n---\n\n")
        f.write(f"## Run {run_record['run_id']}\n\n")
        f.write(f"- **Timestamp (UTC):** {run_record['timestamp_utc']}\n")
        f.write(f"- **Operator:** {run_record['operator']}\n")
        f.write(f"- **Platform:** {run_record['platform']}\n")
        f.write(f"- **Python:** {run_record['python_version']}\n")
        f.write(f"- **pandas:** {run_record['pandas_version']}\n")
        f.write(f"- **pyodbc:** {run_record['pyodbc_version']}\n")
        f.write(f"- **Archives processed:** {len(run_record['archives'])}\n")
        for a in run_record['archives']:
            f.write(f"  - `{os.path.basename(a['path'])}` "
                    f"(mtime: {a['mtime_utc']}, "
                    f"size: {a['size_bytes']:,} bytes)\n")
        f.write("\n**Core tables (after multi-archive merge & dedup):**\n\n")
        f.write("| Table | Rows | Cols | Within-archive dups | "
                "Cross-archive dups |\n")
        f.write("|---|---:|---:|---:|---:|\n")
        for t, info in run_record['core_tables'].items():
            f.write(f"| {t} | {info['rows']:,} | {info['cols']} | "
                    f"{info['within_archive_dups']:,} | "
                    f"{info['cross_archive_dups']:,} |\n")
        f.write("\n---\n\n")


def write_data_quality_report(path, run_record):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write("# Data Quality Report\n\n")
        f.write(f"Generated: {run_record['timestamp_utc']}  \n")
        f.write(f"Run ID: `{run_record['run_id']}`\n\n")
        f.write("This report reflects the most recent extraction run. "
                "Missing values are reported, not removed — the curation "
                "principle is to preserve original data and make limitations "
                "visible (Peer, Green & Stephenson, 2014; "
                "Bruce & Hillmann, 2004).\n\n")
        for table, info in run_record['core_tables'].items():
            f.write(f"## `{table}`\n\n")
            f.write(f"- Rows: **{info['rows']:,}**\n")
            f.write(f"- Columns: **{info['cols']}**\n")
            f.write(f"- Within-archive duplicates dropped: "
                    f"{info['within_archive_dups']:,}\n")
            f.write(f"- Cross-archive duplicates dropped (kept latest): "
                    f"{info['cross_archive_dups']:,}\n\n")
            miss = info.get('missing', {})
            if miss:
                f.write("**Columns with missing values:**\n\n")
                f.write("| Column | Missing | % |\n|---|---:|---:|\n")
                for col, (n, pct) in sorted(
                    miss.items(), key=lambda kv: -kv[1][1]
                ):
                    f.write(f"| `{col}` | {n:,} | {pct}% |\n")
                f.write("\n")
            else:
                f.write("No missing values.\n\n")


# ---------------------------------------------------------------------------
# Main pipeline
# ---------------------------------------------------------------------------

def run(raw_dir, output_dir, single_input=None):
    timestamp = datetime.now(timezone.utc)
    run_id = timestamp.strftime("%Y%m%dT%H%M%SZ")

    if single_input:
        if not os.path.exists(single_input):
            raise FileNotFoundError(f"File not found: {single_input}")
        archives = [single_input]
    else:
        archives = discover_archives(raw_dir)

    archive_records = [
        {
            "path": p,
            "mtime_utc": datetime.fromtimestamp(
                os.path.getmtime(p), tz=timezone.utc
            ).isoformat(),
            "size_bytes": os.path.getsize(p),
        }
        for p in archives
    ]

    print(f"Run ID: {run_id}")
    print(f"Archives ({len(archives)}), processed in mtime order:")
    for a in archive_records:
        print(f"  {os.path.basename(a['path'])}  (mtime: {a['mtime_utc']})")

    processed_dir = os.path.join(output_dir, "processed")
    reference_dir = os.path.join(output_dir, "reference")
    os.makedirs(processed_dir, exist_ok=True)
    os.makedirs(reference_dir, exist_ok=True)

    per_table_frames = {normalized_table_name(t): [] for t in CORE_TABLES}
    per_table_within_dups = {normalized_table_name(t): 0 for t in CORE_TABLES}

    for archive_path in archives:
        archive_name = os.path.basename(archive_path)
        print(f"\n--- {archive_name} ---")
        conn = get_connection(archive_path)
        available = list_tables(conn)

        for table in CORE_TABLES:
            if table not in available:
                print(f"  [skip] {table} not in archive")
                continue
            df = extract_table(conn, table)
            df, n_dups = clean_table(df)
            df["source_archive"] = archive_name
            key = normalized_table_name(table)
            per_table_frames[key].append(df)
            per_table_within_dups[key] += n_dups
            print(f"  {table}: {len(df):,} rows, {len(df.columns)} cols "
                  f"({n_dups} within-archive dups dropped)")

        conn.close()

    print("\nMerging across archives & writing processed CSVs...")
    core_summary = {}
    for table in CORE_TABLES:
        key = normalized_table_name(table)
        frames = per_table_frames.get(key, [])
        if not frames:
            print(f"  [skip] {table}: no data across archives")
            continue
        merged, cross_dups = merge_with_dedup(frames, key)
        out_path = os.path.join(processed_dir, f"{key}.csv")
        merged.to_csv(out_path, index=False, encoding="utf-8")
        print(f"  {key}: {len(merged):,} rows after merge "
              f"({cross_dups:,} cross-archive dups dropped)")
        core_summary[key] = {
            "rows": len(merged),
            "cols": len(merged.columns),
            "within_archive_dups": per_table_within_dups[key],
            "cross_archive_dups": cross_dups,
            "missing": missing_summary(merged),
        }

    print("\nExporting reference tables from latest archive...")
    latest = archives[-1]
    conn = get_connection(latest)
    available = list_tables(conn)
    for table in REFERENCE_TABLES:
        if table not in available:
            print(f"  [skip] {table} not in latest archive")
            continue
        df = extract_table(conn, table)
        df = normalize_columns(df)
        out = os.path.join(reference_dir, f"{table.lower()}.csv")
        df.to_csv(out, index=False, encoding="utf-8")
        print(f"  {table}: {len(df):,} rows")
    conn.close()

    run_record = {
        "run_id": run_id,
        "timestamp_utc": timestamp.isoformat(),
        "operator": os.environ.get("USERNAME") or os.environ.get("USER") or "unknown",
        "platform": f"{platform.system()} {platform.release()}",
        "python_version": platform.python_version(),
        "pandas_version": pd.__version__,
        "pyodbc_version": pyodbc.version,
        "archives": archive_records,
        "core_tables": core_summary,
        "decisions": {
            "merge_strategy": "concat in mtime order; drop_duplicates keep='last'",
            "natural_keys": TABLE_KEYS,
            "missing_values": "preserved (reported, not dropped)",
            "column_normalization": "lowercase snake_case",
            "reference_tables_source": "latest archive only",
        },
    }

# Logs go to <repo_root>/logs (sibling of data/)
    logs_dir = os.path.join(os.path.dirname(os.path.abspath(output_dir)), "logs")
    os.makedirs(logs_dir, exist_ok=True)

    write_provenance_log(os.path.join(logs_dir, "provenance.log"), run_record)
    write_curation_log(os.path.join(logs_dir, "curation_log.md"), run_record)
    write_data_quality_report(
        os.path.join(logs_dir, "data_quality.md"), run_record
    )

    print(f"\nLogs written to: {logs_dir}")
    print("Done.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Extract & curate NTSB aviation accident data from .mdb archives."
    )
    parser.add_argument(
        "--input",
        help="Single .mdb file to process (overrides --raw-dir)."
    )
    parser.add_argument(
        "--raw-dir",
        default="data/raw",
        help="Directory of .mdb archives to process (default: data/raw)."
    )
    parser.add_argument(
        "--output",
        default="data/",
        help="Output base directory (default: data/)."
    )
    args = parser.parse_args()

    try:
        run(args.raw_dir, args.output, single_input=args.input)
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)