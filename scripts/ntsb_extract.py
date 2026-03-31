"""
NTSB Aviation Accident Database - Extraction Script
IS547 Foundations of Data Curation | Spring 2026

Reads tables from a NTSB .mdb Access file and exports them to CSV.
Applies basic cleaning: lowercase column names, strip whitespace, drop duplicates.

Usage:
    python ntsb_extract.py --input data/raw/FILE_NAME.mdb --output data/

Dependencies:
    pip install pandas pyodbc

Author: Achyutha Sushanth Ariga
Course: IS547, UIUC, Spring 2026
"""

import os
import argparse

import pandas as pd
import pyodbc


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


def get_connection(mdb_path):
    conn_str = (
        r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
        rf"DBQ={os.path.abspath(mdb_path)};"
    )
    return pyodbc.connect(conn_str)


def list_tables(conn):
    cursor = conn.cursor()
    tables = [row.table_name for row in cursor.tables(tableType="TABLE")]
    return tables


def extract_table(conn, table_name):
    df = pd.read_sql(f"SELECT * FROM [{table_name}]", conn)
    return df


def clean_table(df):
    # Lowercase and normalize column names
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(r"[\s\-\/]+", "_", regex=True)
        .str.replace(r"[^\w]", "", regex=True)
    )

    # Strip whitespace from string columns
    str_cols = df.select_dtypes(include="object").columns
    df[str_cols] = df[str_cols].apply(lambda col: col.str.strip())

    # Drop exact duplicate rows
    before = len(df)
    df = df.drop_duplicates()
    dropped = before - len(df)
    if dropped:
        print(f"    Dropped {dropped} duplicate row(s)")

    # Report missing values (not dropped)
    missing = df.isnull().sum()
    missing = missing[missing > 0]
    if not missing.empty:
        print(f"    Missing values in {len(missing)} column(s):")
        for col, count in missing.items():
            pct = round(count / len(df) * 100, 1)
            print(f"      {col}: {count} ({pct}%)")

    return df


def run(mdb_path, output_dir):
    conn = get_connection(mdb_path)
    available = list_tables(conn)

    processed_dir = os.path.join(output_dir, "processed")
    reference_dir = os.path.join(output_dir, "reference")
    os.makedirs(processed_dir, exist_ok=True)
    os.makedirs(reference_dir, exist_ok=True)

    print("Extracting core tables...")
    for table in CORE_TABLES:
        if table not in available:
            print(f"  Skipping '{table}' (not found)")
            continue
        print(f"  {table}")
        df = extract_table(conn, table)
        df = clean_table(df)
        out = os.path.join(processed_dir, f"{table.lower()}.csv")
        df.to_csv(out, index=False, encoding="utf-8")

    print("\nExporting reference tables...")
    for table in REFERENCE_TABLES:
        if table not in available:
            continue
        print(f"  {table}")
        df = extract_table(conn, table)
        out = os.path.join(reference_dir, f"{table.lower()}.csv")
        df.to_csv(out, index=False, encoding="utf-8")

    conn.close()
    print("\nDone.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", default="data/")
    args = parser.parse_args()

    if not os.path.exists(args.input):
        raise FileNotFoundError(f"File not found: {args.input}")

    run(args.input, args.output)
