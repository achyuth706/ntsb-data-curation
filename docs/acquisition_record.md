# Acquisition record

**Project:** NTSB Aviation Accident Database Curation  
**Prepared by:** Achyutha Sushanth Ariga, University of Illinois Urbana-Champaign, School of Information Sciences  
**Date of acquisition (approx.):** 2026-03-31 (derived from file modification times;  
see audit trail below)

---

## Source

- **Publisher:** National Transportation Safety Board (NTSB)
- **Portal:** NTSB Aviation Data Download — https://data.ntsb.gov/avdata
- **Data type:** Monthly update archives of the NTSB aviation accident and incident
  database (*eADMSPUB*), distributed as ZIP archives each containing one Microsoft
  Access database file (`.mdb`)

NTSB data is produced by a U.S. federal government agency in the course of its
official duties and is therefore in the public domain under 17 U.S.C. § 105.
No copyright restrictions apply to the source data.

---

## Files acquired

| Filename | Size (bytes) | Size (MB) | File mtime (UTC) |
|---|---:|---:|---|
| `up01DEC.mdb` | 6,287,360 | 6.00 | 2026-03-31T00:55:35+00:00 |
| `up01JAN.mdb` | 6,483,968 | 6.18 | 2026-03-31T01:31:23+00:00 |
| `up01FEB.mdb` | 6,504,448 | 6.20 | 2026-03-31T01:29:53+00:00 |
| `up01JUL.mdb` | 7,073,792 | 6.75 | 2026-03-31T01:33:14+00:00 |
| **Total** | **26,349,568** | **25.13** | |

File modification times are recorded in `logs/provenance.log` (JSON Lines format)
and reflect the timestamps at time of download. Files are preserved unmodified in
`data/raw/`, which is excluded from version control (see `.gitignore`) due to size.

---

## Scope and temporal coverage

Each `.mdb` file is one monthly update snapshot. The four archives correspond to
update packages for December, January, February, and July, all from the 2025–2026
update cycle. They are not consecutive months; they represent a convenience sample
drawn from the archives available on the NTSB portal at the time of acquisition.

The NTSB database covers civil aviation accidents and incidents investigated by the
United States from approximately 2008 onward, but these specific archives are
recent monthly update packages and not a full historical release. Rows in the
curated tables carry dates across that broader range wherever NTSB included updated
records for older investigations in its monthly packages.

---

## Format and structure

Each `.mdb` file contains approximately 20 relational tables stored in Microsoft
Access 97–2003 format. The six core tables extracted (`events`, `aircraft`,
`injury`, `narratives`, `flight_crew`, `engines`) and five reference tables
(`eADMSPUB_DataDictionary`, `Country`, `states`, `ct_iaids`, `ct_seqevt`) are
documented in `docs/data_dictionary.md` and `docs/controlled_vocabularies.md`.
Extraction was performed using `pyodbc` with the Microsoft Access ODBC driver on
Windows 11; no conversion tools were applied to the `.mdb` files themselves.

---

## Verification

NTSB does not publish checksums or digital signatures for its `.mdb` archives. The
original files are stored unmodified in `data/raw/`; their file sizes (recorded in
`logs/provenance.log`) serve as the primary integrity reference. Checksums could be
computed from the files in `data/raw/` using standard tools (e.g.,
`certutil -hashfile <file> SHA256` on Windows) and appended to this record for
long-term verification.

---

## Versioning

NTSB updates its portal monthly. Each archive represents the state of NTSB's
database at a specific publication date; older investigations may be updated with
new findings in later archives. The curation pipeline retains the most recent
version of any record that appears in multiple archives (see
`docs/data_quality_notes.md` § Curation decisions). Users requiring the current
state of any investigation should retrieve the latest archive directly from
https://data.ntsb.gov/avdata.

---

## Audit trail

| Field | Value |
|---|---|
| Acquired by | Achyutha Sushanth Ariga |
| Acquisition tool | Web browser (manual download from NTSB portal) |
| Acquisition date (approx.) | 2026-03-31 (based on `.mdb` file modification times) |
| Storage location | `data/raw/` (local, not committed to version control) |
| Extraction run | `20260505T225036Z` (see `logs/curation_log.md`) |
| Extraction platform | Windows 11, Python 3.14.3, pyodbc 5.3.0 |
