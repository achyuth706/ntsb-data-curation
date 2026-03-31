# Curated NTSB Aviation Accident Dataset

**IS547 Foundations of Data Curation — Spring 2026**  
**Author:** Achyutha Sushanth Ariga, University of Illinois Urbana-Champaign

This project curates a multi-archive sample of the NTSB Aviation Accident Database. Four monthly update archives (`.mdb` format) are extracted, cleaned, merged across archives with documented deduplication rules, and exported as plain CSV tables alongside a data dictionary, controlled vocabulary, quality notes, and provenance logs. The goal is to demonstrate defensible curation decisions and produce a dataset that a researcher can understand, reproduce, and reuse without access to the original Access environment.

---

## What's in this repository

```
data/raw/          original .mdb files — download from NTSB; not redistributed here
data/processed/    six cleaned core tables as CSV (events, aircraft, injury, narratives,
                   flight_crew, engines)
data/reference/    five NTSB reference and lookup tables as CSV
scripts/           ntsb_extract.py (extraction pipeline) and generate_docs.py (doc generator)
docs/              data dictionary, controlled vocabularies, quality notes, narrative notes,
                   schema diagram, acquisition record, and preservation plan
logs/              provenance.log, curation_log.md, and data_quality.md from extraction runs
metadata/          DataCite v4.4 metadata record (dataset_metadata.json)
LICENSE            CC0 1.0 Universal public domain dedication
CITATION.cff       machine-readable citation metadata
requirements.txt   Python dependencies
```

---

## Quick start

```bash
git clone https://github.com/achyuth706/ntsb-data-curation
cd ntsb-data-curation
pip install -r requirements.txt
```

Place `.mdb` files downloaded from https://data.ntsb.gov/avdata into `data/raw/`, then:

```bash
python scripts/ntsb_extract.py
python scripts/generate_docs.py
```

Outputs are written to `data/processed/`, `data/reference/`, `logs/`, and `docs/`.

---

## Environment

- Windows 10 or 11
- Python 3.14
- Microsoft Access ODBC Driver (included with Microsoft Access, or install the [Microsoft Access Database Engine Redistributable](https://www.microsoft.com/en-us/download/details.aspx?id=54920))
- Python dependencies: see `requirements.txt`

---

## Documentation index

- [docs/data_dictionary.md](docs/data_dictionary.md) — field-level metadata for all six core tables
- [docs/controlled_vocabularies.md](docs/controlled_vocabularies.md) — coded values and their meanings
- [docs/data_quality_notes.md](docs/data_quality_notes.md) — interpretive notes on missingness and curation decisions
- [docs/narrative_field_notes.md](docs/narrative_field_notes.md) — guidance on the free-text narrative fields
- [docs/schema_diagram.md](docs/schema_diagram.md) — relational ER diagram (Mermaid)
- [docs/acquisition_record.md](docs/acquisition_record.md) — source, scope, file sizes, audit trail
- [docs/preservation_plan.md](docs/preservation_plan.md) — Zenodo deposit strategy and citation format
- [metadata/dataset_metadata.json](metadata/dataset_metadata.json) — DataCite v4.4 metadata record

---

## Curation workflow at a glance

- **Acquire** — download monthly `.mdb` archives from https://data.ntsb.gov/avdata into `data/raw/`
- **Extract and merge** — `ntsb_extract.py` reads each archive in modification-time order, normalises column names, drops within-archive duplicates, then merges across archives retaining the most recent record for any event that appears in multiple archives
- **Generate docs** — `generate_docs.py` reads the curated CSVs, NTSB data dictionary, and quality log to produce `data_dictionary.md` and `controlled_vocabularies.md`
- **Log provenance** — each run appends a JSON record to `logs/provenance.log` and a human-readable entry to `logs/curation_log.md`; `logs/data_quality.md` is overwritten with the latest missing-value report

---

## Source data

NTSB Aviation Data Download portal: https://data.ntsb.gov/avdata  
U.S. federal government work; public domain under 17 U.S.C. § 105.

---

## Citation

Available on Zenodo: https://doi.org/10.5281/zenodo.20059187

---

## License

CC0 1.0 Universal — see [LICENSE](LICENSE).

---

## Course context

Course project for IS547 Foundations of Data Curation, Spring 2026, University of Illinois Urbana-Champaign.
