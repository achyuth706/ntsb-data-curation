# Data Dictionary — NTSB Aviation Accident Database

IS547 Foundations of Data Curation, Spring 2026
Status: Draft

This document describes the key fields across the main tables extracted from the NTSB .mdb files. Definitions are based on the built-in NTSB data dictionary (eADMSPUB_DataDictionary), which is included in data/reference/ and contains complete definitions for all fields.

## Shared Fields

ev_id — unique identifier for each accident event. This field appears in all tables and is how the tables are linked together.

aircraft_key — identifies individual aircraft within a single event. Most accidents involve one aircraft so this is usually 1.

ntsb_no — the NTSB case number assigned to the investigation (e.g. GAA25WA243).

## events

One row per accident.

ev_date — date the accident occurred.
ev_city, ev_state, ev_country — location of the accident. ev_state uses two-letter codes; OF means outside the US.
latitude, longitude — coordinates in degree-minute-second format. Missing for about 40% of records in recent archives because investigations are still in progress.
dec_latitude, dec_longitude — same coordinates in decimal degrees.
ev_highest_injury — the worst injury level among all people involved. FATL = fatal, SERS = serious, MINR = minor, NONE = no injuries.
inj_tot_f, inj_tot_s, inj_tot_m, inj_tot_n — counts of fatal, serious, minor, and uninjured persons.
wx_cond_basic — basic weather condition. VMC = visual conditions, IMC = instrument conditions.
light_cond — lighting at the time of the accident. DLIT = daylight, NITE = night, DUSK/DAWN as expected.
invest_agy — which agency investigated. NTSB or FAA are most common.

## aircraft

One row per aircraft involved in the accident.

damage — how badly the aircraft was damaged. DEST = destroyed, SUBS = substantial, MINR = minor, NONE = no damage.
acft_make, acft_model — manufacturer and model name (e.g. CESSNA, 172).
acft_category — type of aircraft. AIR = airplane, HELI = helicopter, BALL = balloon, GLID = glider.
acft_year — year the aircraft was manufactured.
far_part — the FAA regulation part under which the flight was operating. 091 = general aviation (Part 91), 121 = commercial airline, 135 = charter/commuter.
type_fly — type of flight operation. PERS = personal, INST = instructional, BUSI = business.
homebuilt — whether the aircraft was amateur-built. Y or N.
num_eng — number of engines.

## injury

One row per injury type per event. Breaks down who was injured and how severely.

inj_person_type — the category of person. PLT = pilot, PASS = passenger, GRND = ground personnel.
inj_level — severity. FATL, SERS, MINR, NONE.
inj_person_count — number of people at that injury level. About 22% null in the sample archive.

## narratives

Written descriptions of what happened. One row per aircraft per event.

narr_accp — preliminary narrative written early in the investigation.
narr_accf — final narrative written after the investigation is complete. Often empty in recent archives because the investigation is still open.
narr_cause — the probable cause statement. Also often empty for the same reason.

## flight_crew

One row per crew member involved.

crew_category — role. PLT = pilot, CPT = captain, etc.
crew_age — age of the crew member.
crew_sex — M or F.
med_certf — medical certificate type held. CL1, CL2, CL3 = first/second/third class; SPRT = sport pilot.
crew_inj_level — injury level of this crew member.
pc_profession — whether flying was their profession. Yes or No.

## engines

One row per engine per aircraft.

eng_type — engine type. REC = reciprocating (piston), TF = turbofan, TP = turboprop, TJ = turbojet.
eng_mfgr, eng_model — engine manufacturer and model.
hp_or_lbs — power output, in horsepower for piston engines or pounds of thrust for jets.

---

Note: Many fields have high null rates in the sample archive (up01DEC.mdb). This is expected because that archive contains recent accidents where investigations are still ongoing. Fields like narr_cause and latlong_acq get filled in as investigations are completed. Full null rate statistics per column are in logs/cleaning_report.json.