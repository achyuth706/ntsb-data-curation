# Narrative field notes

**Source table:** `data/processed/narratives.csv`  
**Rows:** 71  &nbsp;|&nbsp; **Columns:** 9  
**Coverage:** 71 of 253 total events (28.1%) have any narratives record

---

## What the narrative fields are

The narratives table holds four free-text fields authored by NTSB investigators:

| Field | Role |
|---|---|
| `narr_accp` | Preliminary factual narrative — the first written account, typically filed while the investigation is still active |
| `narr_accf` | Full factual narrative — a more complete description of the accident sequence, finalised after field investigation |
| `narr_cause` | Probable-cause statement — NTSB's formal determination of the cause(s) and contributing factors |
| `narr_inc` | Incident narrative — analogous fields for *incidents* rather than *accidents* |

The remaining columns (`ev_id`, `aircraft_key`, `lchg_date`, `lchg_userid`, `source_archive`) are keys, timestamps, and a curation-added provenance field.

---

## Structural observations

Only 71 of the 253 events in this extract have a narratives record at all — roughly 28% coverage. This is expected: NTSB creates a narratives record only once sufficient investigative progress has been made to draft any text. The remaining 182 events are likely still in early-stage investigation.

Among the 71 narratives records:

- `narr_accp` (preliminary narrative): **11.3% null** (8 of 71). This is the most consistently populated field; most investigations have at least a preliminary account.
- `narr_accf` (full factual narrative): **47.9% null** (34 of 71). Produced only after the investigation is substantially complete.
- `narr_cause` (probable cause): **47.9% null** (34 of 71). Published at the same milestone as the full narrative; the two fields are null together in nearly every case.
- `narr_inc` (incident narrative): **100% null** (71 of 71). See below.

The near-identical null rates for `narr_accf` and `narr_cause` (both exactly 34 null) confirm that these two fields are gated on the same event: formal closure of the investigation.

---

## Why `narr_inc` is 100% null

This is a known structural feature, not a data-quality problem. The NTSB distinguishes regulatory *accidents* (events involving fatal or substantial-damage outcomes) from *incidents* (less severe occurrences). The four source archives used in this project (`up01DEC.mdb`, `up01JAN.mdb`, `up01FEB.mdb`, `up01JUL.mdb`) are accident archives. The `narr_inc` field is part of NTSB's unified schema but is unused in accident records. Its presence as an all-null column is a schema artifact and should not be interpreted as missing data.

---

## Variability in length and style

The narrative fields vary substantially in length. `narr_accp` ranges from 350 to 44,072 characters (median 2,763), reflecting that some preliminary accounts are brief ICAO Annex 13 notifications for foreign-government-led investigations, while others contain the full draft report. `narr_accf` ranges from 370 to 8,220 characters (median 1,378). `narr_cause` is the most consistent in length — 66 to 724 characters, median 142 — because NTSB probable-cause statements follow a deliberate stylistic convention: a single, technically precise sentence or short paragraph identifying the cause and contributing factors (e.g., *"The loss of engine power due to fatigue failure of the crankshaft."*).

Style also varies by investigation type. International accidents reported under ICAO Annex 13 (where a foreign authority leads the investigation) often contain only a brief deferral notice in `narr_accp` and leave `narr_accf` and `narr_cause` null regardless of investigation closure status, because NTSB is not the releasing authority.

---

## Interpretive limitations

Probable-cause statements reflect investigator judgment at the time of writing and are occasionally revised after initial publication. `narr_accf` may abbreviate or omit details that appear in the underlying docket. Neither field should be treated as exhaustive; the NTSB accident docket (available through the NTSB public docket system) contains the full evidentiary record. Encoding artefacts are present in a small number of records — the replacement character (observed in at least one `narr_cause` value) indicates that the source Access database stored certain characters in a non-UTF-8 encoding that was not fully recovered during extraction.

---

## Reuse guidance

The narrative fields are well suited to qualitative coding, exploratory natural-language processing, or providing contextual framing for quantitative accident analysis. They should not be treated as definitive without corroboration from the underlying investigation file. Researchers using `narr_cause` for causal classification should note that NTSB's probable-cause language is standardised but not exhaustively controlled: investigators choose from a large vocabulary of approved terms, which can produce surface-level inconsistencies across records.

---

## Curation decision

No narrative text has been modified, normalised, truncated, or corrected in this curation project. The text is reproduced verbatim from the source Access databases, including any encoding artefacts. This decision preserves the authority and provenance of NTSB's own investigative writing and ensures that any downstream analysis is working from the original record rather than a curatorial interpretation of it.

