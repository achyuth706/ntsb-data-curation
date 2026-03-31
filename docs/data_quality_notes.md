# Data quality notes

**Companion to:** `logs/data_quality.md`  
**Run reflected:** `20260505T225036Z`  
**Tables covered:** events (253 rows), aircraft (256 rows), injury (1,375 rows), narratives (71 rows), flight\_crew (63 rows), engines (53 rows)

---

## Overview

Data quality is most usefully understood as fitness-for-use: the degree to which a dataset meets the needs of a particular application (Strong, Lee & Wang, 1997). Under that framing, a high missing-value rate is not automatically a defect — it may be a structurally correct reflection of the data-generation process. Peer, Green & Stephenson (2014) extend this by emphasising that curators have a responsibility to document the *reasons* for imperfection, not merely its extent. This document fulfils that responsibility for the current curated extract of the NTSB Aviation Accident Database.

---

## Missingness as signal, not noise

The most prominent pattern in this dataset is that many fields are null precisely because investigations are still open. The NTSB does not publish probable-cause determinations until an investigation is formally closed, which can take months to years after an accident. Accordingly, 47.9% of `narr_cause` and 47.9% of `narr_accf` (factual narrative) records in the narratives table are null. These are not data-entry failures; they are semantically meaningful absences indicating that NTSB staff had not yet completed those narrative sections at the time the archive was exported.

The same logic applies to geolocation. Approximately 40.7% of `latitude` and 40.3% of `longitude` values in the events table are missing. Early-stage investigations may rely on imprecise location descriptions ("near Tucson, AZ") before coordinates are verified and entered. The companion field `latlong_acq` — itself 67.6% null — would have indicated whether coordinates were GPS-derived or estimated; its absence reinforces that these are incomplete rather than inaccurate records.

Researchers should treat null values in this dataset as evidence of investigation status, not evidence of poor data collection.

---

## Per-table observations

**Events (253 rows, 74 columns).** Eleven columns are 100% null across all 253 rows: `wx_brief_comp`, `vis_rvr`, `vis_rvv`, `wx_dens_alt`, `wx_int_precip`, `ntsb_docket`, `ntsb_notf_from`, `ntsb_notf_date`, `ntsb_notf_tm`, `fiche_number`, and `faa_dist_office`. These fields exist in the NTSB schema but were not populated for any event in this extract. The weather-detail fields (`vis_rvr`, `vis_rvv`, `wx_dens_alt`, `wx_int_precip`) require specific instrumentation and reporting conditions that most small general-aviation accidents do not trigger. The notification and docket fields are only populated once an investigation reaches a specific administrative milestone. `fiche_number` is a legacy microfilm reference now obsolete for modern investigations. `mid_air` and `on_ground_collision` are 98.8% null because they apply only to the rare subset of accidents involving multiple aircraft.

**Aircraft (256 rows, 94 columns).** Aircraft has the widest schema of any table and correspondingly the most nulls: 75 of 94 columns carry at least one missing value, and 11 are 100% null. Several of these (`acft_reg_cls`, `oprtng_cert`, `oper_cert`, `evacuation`, `report_to_icao`) apply only to commercial or regulated operations; most accidents in this extract involve Part 91 general-aviation flights, so these fields simply do not apply. Notably, `damage` is 33.2% null (85 of 256 records), which likely reflects open investigations where damage classification has not yet been confirmed.

**Injury (1,375 rows, 8 columns).** Injury is the largest table because it stores one row per person-category per injury level per aircraft per event. Only one column carries missing values: `inj_person_count` at 26.1% (359 rows). These nulls likely represent categorical injury records where a count had not been entered at the time of export rather than zero-injury categories.

**Narratives (71 rows, 9 columns).** Only 71 of 253 events have any narratives record, meaning roughly 72% of events have no associated narrative at all — a direct indicator that the majority of investigations in this extract were still open. Of those 71 records, `narr_cause` (probable cause) and `narr_accf` (factual narrative, full) are each 47.9% null (34 records), and `narr_accp` (factual narrative, preliminary) is 11.3% null. `narr_inc` is 100% null by design: this archive contains accident records only; the incident narrative field is a schema placeholder unused in this context.

**Flight crew (63 rows, 34 columns).** Six columns are 100% null: `crew_rat_endorse`, `seatbelts_used`, `shldr_harn_used`, `bfr`, `child_restraint`, and `mr_faa_med_certf`. These fields are only populated when a crew member is injured or when an investigation specifically addresses restraint systems and biennial flight review status. `crew_tox_perf` is 57.1% null, reflecting that toxicological testing is reserved for fatal or serious-injury accidents.

**Engines (53 rows, 18 columns).** Propeller-related fields are 52–68% null because many aircraft in the dataset use fixed-pitch propellers for which model and type data are rarely entered, or are jet/turbine-powered with no propeller at all.

---

## Curation decisions

**Missing values were preserved, not imputed or dropped.** Imputing missing values would introduce fabricated data into an authoritative accident record; dropping rows would silently reduce the sample and obscure the investigation-completeness signal described above. Visible missingness supports the metadata-quality dimension of transparency (Bruce & Hillmann, 2004).

**Categorical codes were not recoded.** Values such as `damage` (MINR, SUBS, DEST), `ev_highest_injury` (FATL, SERS, MINR, NONE, UNK), and `acft_category` (AIR, HELI, BALL, etc.) are preserved exactly as NTSB encoded them. Recoding would overwrite NTSB's authoritative terminology and complicate round-tripping back to the source system. The full controlled vocabulary is published separately in `docs/controlled_vocabularies.md`.

**Cross-archive deduplication retained the latest record.** The four archives were processed in modification-time order; where the same event appeared in multiple archives (three events in both events and aircraft), `drop_duplicates(keep='last')` retained the most recently updated record. NTSB updates investigation records as they progress, so the latest version is the most complete.

---

## Known limitations for reuse

This curated extract spans four monthly update archives (December, January, February, and July, all from approximately the same annual update cycle), representing a narrow and non-consecutive temporal slice. Findings should not be generalised to the full NTSB accident record. All-null columns reflect schema fields that NTSB populates conditionally; their presence does not indicate that the information was collected and discarded. Narrative fields are free text authored by individual NTSB investigators, are subject to revision as investigations conclude, and should be treated as contextual documentation rather than structured data.

---

## References

Bruce, T., & Hillmann, D. (2004). The continuum of metadata quality: Defining, expressing, exploiting. In D. Hillmann & E. Westbrooks (Eds.), *Metadata in practice* (pp. 238–256). ALA Editions.

Peer, L., Green, A., & Stephenson, E. (2014). Committing to data quality review. *International Journal of Digital Curation*, *9*(1), 263–291. https://doi.org/10.2218/ijdc.v9i1.317

Strong, D. M., Lee, Y. W., & Wang, R. Y. (1997). Data quality in context. *Communications of the ACM*, *40*(5), 103–110. https://doi.org/10.1145/253769.253804
