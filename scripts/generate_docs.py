"""
NTSB Aviation Accident Database — Documentation Generator
IS547 Foundations of Data Curation, Spring 2026

Reads the curated CSVs, NTSB data dictionary, and data-quality log, then
auto-generates two Markdown documentation files:

    docs/controlled_vocabularies.md   — coded fields and their meanings
    docs/data_dictionary.md           — per-column field-level metadata

Usage:
    python scripts/generate_docs.py
    python scripts/generate_docs.py --data-dir data --logs-dir logs --docs-dir docs
"""

import os
import re
import sys
import argparse

import pandas as pd


CORE_TABLES = ["events", "aircraft", "injury", "narratives", "flight_crew", "engines"]

KEY_NOTES = {
    "ev_id":          "primary / foreign key",
    "aircraft_key":   "foreign key (within event)",
    "crew_no":        "composite key component",
    "eng_no":         "composite key component",
    "injury_level":   "composite key component",
    "inj_person_category": "composite key component",
    "person_category": "composite key component",
    "source_archive": "curation-added field",
}

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def find_col(df: pd.DataFrame, candidates: list[str]) -> str | None:
    """Return the first column in df whose name matches (case-insensitive)
    any of the candidate strings. Returns None if no match is found."""
    lower_map = {c.lower(): c for c in df.columns}
    for cand in candidates:
        if cand.lower() in lower_map:
            return lower_map[cand.lower()]
    return None


def normalize_col_name(name: str) -> str:
    """Apply the same column normalisation used by ntsb_extract.py."""
    name = str(name).strip().lower()
    name = re.sub(r"[\s\-\/]+", "_", name)
    name = re.sub(r"[^\w]", "", name)
    return name


def infer_dtype_label(series: pd.Series) -> str:
    """Map a pandas Series dtype to a human-friendly label."""
    dtype = series.dtype
    if pd.api.types.is_bool_dtype(dtype):
        return "boolean"
    if pd.api.types.is_integer_dtype(dtype):
        return "integer"
    if pd.api.types.is_float_dtype(dtype):
        return "numeric"
    if pd.api.types.is_datetime64_any_dtype(dtype):
        return "datetime"
    if dtype == object:
        sample = series.dropna().head(10)
        if len(sample) > 0 and sample.astype(str).str.match(
            r"^\d{4}-\d{2}-\d{2}", na=False
        ).mean() > 0.7:
            return "datetime"
    return "text"


def escape_pipe(s: str) -> str:
    """Escape pipe characters so they don't break Markdown table cells."""
    return str(s).replace("|", "\\|")


def truncate(s: str, n: int = 200) -> str:
    s = str(s).strip()
    return s[:n] + "…" if len(s) > n else s


# ---------------------------------------------------------------------------
# Parse logs/data_quality.md
# ---------------------------------------------------------------------------

def parse_quality_log(log_path: str) -> dict:
    """Parse the Markdown quality report and return
    {table_name: {column: (missing_count, missing_pct)}}.
    """
    result: dict = {}
    current_table: str | None = None
    in_table = False

    with open(log_path, encoding="utf-8") as fh:
        for line in fh:
            # Section header: ## `events`
            m = re.match(r"^##\s+`(\w+)`", line)
            if m:
                current_table = m.group(1)
                result[current_table] = {}
                in_table = False
                continue

            # Table header row
            if current_table and "| Column | Missing |" in line:
                in_table = True
                continue

            # Separator row (skip)
            if in_table and re.match(r"^\|[-:| ]+\|", line):
                continue

            # Data row: | `col_name` | 253 | 100.0% |
            if in_table and current_table:
                m = re.match(
                    r"\|\s*`([^`]+)`\s*\|\s*([\d,]+)\s*\|\s*([\d.]+)%\s*\|", line
                )
                if m:
                    col   = m.group(1)
                    count = int(m.group(2).replace(",", ""))
                    pct   = float(m.group(3))
                    result[current_table][col] = (count, pct)
                elif line.strip() and not line.startswith("|"):
                    in_table = False

    return result


# ---------------------------------------------------------------------------
# Generate docs/controlled_vocabularies.md
# ---------------------------------------------------------------------------

def generate_controlled_vocabularies(
    dd: pd.DataFrame,
    docs_dir: str,
) -> None:
    """Write docs/controlled_vocabularies.md."""

    col_table   = find_col(dd, ["table", "Table", "Table_name", "tablename"])
    col_field   = find_col(dd, ["column", "Column", "Column_Name", "Field", "field_name"])
    col_code    = find_col(dd, ["code_iaids", "Code", "code", "Value"])
    col_meaning = find_col(dd, ["meaning", "Meaning", "Description", "code_meaning"])

    print(f"  Column mappings for controlled_vocabularies.md:")
    print(f"    table   -> {col_table}")
    print(f"    column  -> {col_field}")
    print(f"    code    -> {col_code}")
    print(f"    meaning -> {col_meaning}")

    missing = [n for n, v in [
        ("table", col_table), ("column", col_field),
        ("code", col_code), ("meaning", col_meaning)
    ] if v is None]
    if missing:
        print(f"\n  ERROR: Could not find columns for: {missing}")
        print(f"  Available columns: {list(dd.columns)}")
        sys.exit(1)

    # Normalise table/column names in the data dictionary for lookup
    dd = dd.copy()
    dd["_norm_table"] = dd[col_table].astype(str).str.lower().str.strip()
    dd["_norm_col"]   = dd[col_field].apply(normalize_col_name)

    print(f"  Unique tables in data dictionary: "
          f"{sorted(dd['_norm_table'].unique())[:20]}")

    lines: list[str] = []

    lines += [
        "# Controlled vocabularies\n",
        "This document lists the coded values used in each core table of the "
        "curated NTSB Aviation Accident Database. Codes and meanings are taken "
        "directly from NTSB's *eADMSPUB_DataDictionary* — no recoding has been "
        "applied. Publishing a controlled vocabulary supports interoperability "
        "and reuse (Wilkinson et al., 2016).\n",
        "> **Curation decision:** Codes are reproduced as-is. Researchers needing "
        "normalised labels should map through this document.\n",
        "",
    ]

    for table in CORE_TABLES:
        lines.append(f"## {table}\n")

        sub = dd[dd["_norm_table"] == table]
        if sub.empty and table == "flight_crew":
            sub = dd[dd["_norm_table"] == "flight_crew"]

        # Rows with an actual code value
        coded = sub[
            sub[col_code].notna()
            & (sub[col_code].astype(str).str.strip() != "")
            & (sub[col_code].astype(str).str.strip().str.lower() != "nan")
        ].copy()

        if coded.empty:
            lines.append(
                "*No coded fields identified in the data dictionary for this table.*\n"
            )
            continue

        for field in sorted(coded["_norm_col"].unique()):
            field_rows = (
                coded[coded["_norm_col"] == field][[col_code, col_meaning]]
                .drop_duplicates()
                .sort_values(col_code)
            )
            if field_rows.empty:
                continue

            lines.append(f"### `{field}`\n")
            lines.append("| Code | Meaning |")
            lines.append("|---|---|")
            for _, row in field_rows.iterrows():
                code    = escape_pipe(str(row[col_code]).strip())
                meaning = escape_pipe(
                    str(row[col_meaning]).strip()
                    if pd.notna(row[col_meaning]) else ""
                )
                lines.append(f"| `{code}` | {meaning} |")
            lines.append("")

    out_path = os.path.join(docs_dir, "controlled_vocabularies.md")
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))
    print(f"  Written: {out_path}")


# ---------------------------------------------------------------------------
# Generate docs/data_dictionary.md
# ---------------------------------------------------------------------------

def generate_data_dictionary(
    dd: pd.DataFrame,
    quality: dict,
    data_dir: str,
    docs_dir: str,
) -> None:
    """Write docs/data_dictionary.md."""

    col_table = find_col(dd, ["table", "Table", "Table_name", "tablename"])
    col_field = find_col(dd, ["column", "Column", "Column_Name", "Field", "field_name"])
    col_code  = find_col(dd, ["code_iaids", "Code", "code", "Value"])
    col_qdesc = find_col(dd, ["question_def", "Question_def"])
    col_sdesc = find_col(dd, ["short_desc", "Short_desc", "short_description"])

    dd = dd.copy()
    dd["_norm_table"] = dd[col_table].astype(str).str.lower().str.strip()
    dd["_norm_col"]   = dd[col_field].apply(normalize_col_name)

    # Build description lookup: (table, col) → longest non-null question_def or short_desc
    desc_lookup: dict[tuple, str] = {}
    for _, row in dd.iterrows():
        key = (row["_norm_table"], row["_norm_col"])
        if key in desc_lookup:
            continue
        desc = ""
        if col_qdesc and pd.notna(row[col_qdesc]):
            desc = str(row[col_qdesc]).strip()
        elif col_sdesc and pd.notna(row[col_sdesc]):
            desc = str(row[col_sdesc]).strip()
        desc_lookup[key] = desc

    # Build coded-fields set: (table, col) that have at least one code entry
    coded_fields: set[tuple] = set()
    if col_code:
        mask = (
            dd[col_code].notna()
            & (dd[col_code].astype(str).str.strip() != "")
            & (dd[col_code].astype(str).str.strip().str.lower() != "nan")
        )
        for _, row in dd[mask].iterrows():
            coded_fields.add((row["_norm_table"], row["_norm_col"]))

    lines: list[str] = []

    lines += [
        "# Data dictionary\n",
        "Field-level metadata for each of the six curated core tables. "
        "Descriptions are taken from NTSB's *eADMSPUB_DataDictionary*. "
        "Fields with coded values link to "
        "[controlled_vocabularies.md](controlled_vocabularies.md). "
        "Missingness percentages reflect the latest extraction run "
        "(see `logs/data_quality.md`).\n",
        "",
    ]

    for table in CORE_TABLES:
        lines.append(f"## {table}\n")

        csv_path = os.path.join(data_dir, "processed", f"{table}.csv")
        df = pd.read_csv(csv_path, low_memory=False)
        print(f"  {table}: {len(df):,} rows x {len(df.columns)} cols")

        table_quality = quality.get(table, {})

        lines.append("| Field | Type | Description | Missing% | Notes |")
        lines.append("|---|---|---|---:|---|")

        for col in df.columns:
            dtype_label = infer_dtype_label(df[col])

            # Description lookup
            desc = desc_lookup.get((table, col), "")
            if not desc:
                # Try flight_crew alias
                desc = desc_lookup.get(("flight_crew", col), "") if table == "flight_crew" else ""
            desc_cell = truncate(escape_pipe(desc)) if desc else ""

            # Missingness
            if col in table_quality:
                count, pct = table_quality[col]
                miss_str = f"{pct}%"
            else:
                miss_str = "0%"

            # Notes
            note_parts: list[str] = []
            if col in KEY_NOTES:
                note_parts.append(KEY_NOTES[col])

            if (table, col) in coded_fields:
                note_parts.append(
                    "see [controlled vocabularies](controlled_vocabularies.md)"
                )

            notes_cell = "; ".join(note_parts)

            lines.append(
                f"| `{col}` | {dtype_label} | {desc_cell} | {miss_str} | {notes_cell} |"
            )

        lines.append("")

    lines += [
        "---\n",
        "**References**\n",
        "Bruce, T., & Hillmann, D. (2004). The continuum of metadata quality: "
        "Defining, expressing, exploiting. In D. Hillmann & E. Westbrooks (Eds.), "
        "*Metadata in practice* (pp. 238–256). ALA Editions.\n",
        "Wilkinson, M. D., Dumontier, M., Aalbersberg, I. J., Appleton, G., "
        "Axton, M., Baak, A., … Mons, B. (2016). The FAIR guiding principles "
        "for scientific data management and stewardship. *Scientific Data*, "
        "*3*, 160018. https://doi.org/10.1038/sdata.2016.18\n",
    ]

    out_path = os.path.join(docs_dir, "data_dictionary.md")
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))
    print(f"  Written: {out_path}")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Auto-generate documentation from curated NTSB data."
    )
    parser.add_argument(
        "--data-dir", default="data",
        help="Base data directory containing processed/ and reference/ (default: data)"
    )
    parser.add_argument(
        "--logs-dir", default="logs",
        help="Directory containing data_quality.md (default: logs)"
    )
    parser.add_argument(
        "--docs-dir", default="docs",
        help="Output directory for generated Markdown files (default: docs)"
    )
    args = parser.parse_args()

    os.makedirs(args.docs_dir, exist_ok=True)

    # ------------------------------------------------------------------
    # 1. Load & inspect data dictionary
    # ------------------------------------------------------------------
    dd_path = os.path.join(args.data_dir, "reference", "eadmspub_datadictionary.csv")
    print(f"[1/4] Loading data dictionary: {dd_path}")
    dd = pd.read_csv(dd_path, low_memory=False)
    print(f"  Shape: {dd.shape}")
    print(f"  Columns: {list(dd.columns)}")
    print("  Sample rows (first 3):")
    print(dd.head(3).to_string())
    print()

    # ------------------------------------------------------------------
    # 2. Parse quality log
    # ------------------------------------------------------------------
    quality_path = os.path.join(args.logs_dir, "data_quality.md")
    print(f"[2/4] Parsing quality log: {quality_path}")
    quality = parse_quality_log(quality_path)
    for t, cols in quality.items():
        print(f"  {t}: {len(cols)} columns with missing values")
    print()

    # ------------------------------------------------------------------
    # 3. Generate controlled_vocabularies.md
    # ------------------------------------------------------------------
    print(f"[3/4] Generating controlled_vocabularies.md ...")
    generate_controlled_vocabularies(dd, args.docs_dir)
    print()

    # ------------------------------------------------------------------
    # 4. Generate data_dictionary.md
    # ------------------------------------------------------------------
    print(f"[4/4] Generating data_dictionary.md ...")
    generate_data_dictionary(dd, quality, args.data_dir, args.docs_dir)
    print()

    print("Done. Files written to:", args.docs_dir)


if __name__ == "__main__":
    main()
