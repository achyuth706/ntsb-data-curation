# Preservation plan

**Project:** NTSB Aviation Accident Database Curation  
**Author:** Achyutha Sushanth Ariga, University of Illinois Urbana-Champaign, School of Information Sciences

---

## Overview

The raw NTSB `.mdb` archives are already publicly accessible through
https://data.ntsb.gov/avdata and will continue to be updated monthly. What
is not publicly available — and therefore benefits from independent preservation —
is the curated artifact set produced by this project: the cleaned and merged CSV
tables, the data dictionary and controlled vocabulary documentation, the provenance
logs, and the extraction pipeline. Together, these constitute a reproducible
research object that makes the NTSB data substantially more reusable than the
original `.mdb` archives without a custom Access environment (NASEM, 2019).
Preserving them ensures that the curation work is not silently lost if NTSB
updates or restructures its portal.

---

## Repository selection: Zenodo

**Zenodo** (https://zenodo.org) is the recommended repository for this deposit
for three reasons. First, it is operated by CERN under open-access principles and
has an explicit preservation commitment for the lifetime of CERN, providing
institutional durability that personal or course storage cannot. Second, every
Zenodo record receives a DataCite DOI minted against the DataCite Metadata
Schema v4.4 (DataCite Metadata Working Group, 2021), making the dataset
findable through DOI-resolving discovery services and citeable in academic work.
Third, Zenodo integrates directly with GitHub, so future releases of this
repository can be deposited with a single click during a GitHub Release.

Two alternatives were considered. **IDEALS** (Illinois Digital Environment for
Access to Learning and Scholarship, the UIUC institutional repository) would
provide good institutional context but is oriented toward theses and faculty
publications; dataset deposits are accepted but receive less visibility in
cross-disciplinary data discovery tools. **ICPSR** (Inter-university Consortium
for Political and Social Research) is an excellent fit for quantitative social
science but would require submission review, has stricter format requirements, and
is designed for larger longitudinal studies rather than a focused curation
exercise. Zenodo's low barriers, strong DOI infrastructure, and generalist scope
make it the best match for this project's scope.

---

## Format choices

| Artifact | Format | Rationale |
|---|---|---|
| Curated tables | CSV (UTF-8) | Open, plain-text, readable without proprietary software |
| Metadata record | JSON (DataCite v4.4) | Machine-readable, schema-validated, portable |
| Documentation | Markdown | Renders on GitHub; plain-text portable for long-term access |
| Provenance log | JSON Lines | Append-only, machine-readable; each line is a valid JSON object |
| Source `.mdb` files | **Not deposited** | See below |

---

## Persistent identifier strategy

Each Zenodo release mints a version-specific DOI and a concept DOI that always
resolves to the latest version. Version-specific DOIs ensure that cited results
are reproducible against a fixed dataset snapshot — a key requirement for
scientific reproducibility (Duerr et al., 2011). 

---

## Long-term access

Zenodo's preservation policy commits to retaining all deposits for the lifetime
of CERN. The CSV and Markdown formats chosen here require no proprietary software
and are well-supported by migration pathways; if CSV ever becomes obsolete,
content can be re-encoded with no semantic loss. The provenance log and metadata
record document the full lineage of the dataset, satisfying the OAIS model's
requirement for representation information.

---

## What is not preserved here

The original `.mdb` files are not included in the Zenodo deposit for two reasons:
file size (four archives total 25.1 MB, approaching Zenodo's default file-size
limits for a student account), and the fact that NTSB is the authoritative source
for those files. Users who need the original Access databases should retrieve them
directly from https://data.ntsb.gov/avdata. The narrative texts in
`data/processed/narratives.csv` are reproduced verbatim from NTSB; users who
require authoritative, non-curated versions of investigation narratives should
consult the NTSB public docket system.

---

## FAIR alignment

| Principle | How addressed |
|---|---|
| **Findable** | DataCite DOI + structured `metadata/dataset_metadata.json`; indexed by Zenodo and DataCite search |
| **Accessible** | Zenodo open-access deposit; no login required to download |
| **Interoperable** | CSV + JSON formats; controlled vocabulary published in `docs/controlled_vocabularies.md` |
| **Reusable** | CC0 license; data dictionary and provenance logs document every transformation (Wilkinson et al., 2016) |

---

## Citation

Available on Zenodo: https://doi.org/10.5281/zenodo.20059187

---

## References

DataCite Metadata Working Group. (2021). *DataCite Metadata Schema documentation
for the publication and citation of research data and other research outputs.
Version 4.4*. DataCite e.V. https://doi.org/10.14454/3w3z-sa82

Duerr, R. E., Downs, R. R., Tilmes, C., Barkstrom, B., Lenhardt, W. C.,
Glassy, J., … Slaughter, P. (2011). On the utility of identification schemes
for digital earth science data. *Earth Science Informatics*, *4*(3), 139–160.
https://doi.org/10.1007/s12145-011-0083-6

National Academies of Sciences, Engineering, and Medicine. (2019).
*Reproducibility and replicability in science*. The National Academies Press.
https://doi.org/10.17226/25303

Wilkinson, M. D., Dumontier, M., Aalbersberg, I. J., Appleton, G., Axton, M.,
Baak, A., … Mons, B. (2016). The FAIR guiding principles for scientific data
management and stewardship. *Scientific Data*, *3*, 160018.
https://doi.org/10.1038/sdata.2016.18
