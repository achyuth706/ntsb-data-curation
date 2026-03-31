# Controlled vocabularies

This document lists the coded values used in each core table of the curated NTSB Aviation Accident Database. Codes and meanings are taken directly from NTSB's *eADMSPUB_DataDictionary* — no recoding has been applied. Publishing a controlled vocabulary supports interoperability and reuse (Wilkinson et al., 2016).

> **Curation decision:** Codes are reproduced as-is. Researchers needing normalised labels should map through this document.


## events

### `ev_dow`

| Code | Meaning |
|---|---|
| `FR` | Friday |
| `MO` | Monday |
| `SA` | Saturday |
| `SU` | Sunday |
| `TH` | Thursday |
| `TU` | Tuesday |
| `WE` | Wednesday |

### `ev_highest_injury`

| Code | Meaning |
|---|---|
| `FATL` | Fatal |
| `MINR` | Minor |
| `NONE` |  |
| `SERS` | Serious |
| `UNK` | Unknown |

### `ev_nr_apt_loc`

| Code | Meaning |
|---|---|
| `OFAP` | Off Airport/Airstrip |
| `ONAP` | On Airport |
| `ONAS` | On Airstrip |
| `UNK` | Unknown |

### `ev_state`

| Code | Meaning |
|---|---|
| `AK` | ALASKA |
| `AL` | ALABAMA |
| `AO` | ATLANTIC OCEAN |
| `AQ` | AMERICAN SAMOA |
| `AR` | ARKANSAS |
| `AS` | AUSTRALIA |
| `AZ` | ARIZONA |
| `BC` | BOTSWANA |
| `BF` | THE BAHAMAS |
| `CA` | CALIFORNIA |
| `CB` | CARIBBEAN SEA |
| `CD` | CHAD |
| `CH` | CHINA, PEOPLES REPUBLIC OF |
| `CN` | CANADA |
| `CO` | COLORADO |
| `CQ` | NORTHERN MARIANA ISLANDS |
| `CS` | COSTA RICA |
| `CT` | CONNECTICUT |
| `CU` | CUBA |
| `DC` | DISTRICT OF COLUMBIA |
| `DE` | DELAWARE |
| `EI` | IRELAND |
| `FL` | FLORIDA |
| `FR` | FRANCE |
| `FT` | FR TERR OF AFARS ISSAS |
| `GA` | GEORGIA |
| `GE` | GERMANY |
| `GM` | GULF OF AMERICA |
| `GR` | GREECE |
| `GU` | GUAM |
| `HI` | HAWAII |
| `HK` | HONG KONG |
| `IA` | IOWA |
| `IC` | ICELAND |
| `ID` | IDAHO |
| `IE` | INDONESIA |
| `IL` | ILLINOIS |
| `IN` | INDIANA |
| `IT` | ITALY |
| `JA` | JAPAN |
| `JM` | JAMAICA |
| `KQ` | KINGMAN REEF |
| `KS` | KANSAS |
| `KU` | KUWAIT |
| `KY` | KENTUCKY |
| `LA` | LOUISIANA |
| `MA` | MASSACHUSETTS |
| `MD` | MARYLAND |
| `ME` | MAINE |
| `MI` | MICHIGAN |
| `MN` | MINNESOTA |
| `MO` | MISSOURI |
| `MP` | MAURITIUS |
| `MS` | MISSISSIPPI |
| `MT` | MONTANA |
| `MX` | MEXICO |
| `MY` | MALAYSIA |
| `NC` | NORTH CAROLINA |
| `ND` | NORTH DAKOTA |
| `NE` | NEBRASKA |
| `NH` | NEW HAMPSHIRE |
| `NJ` | NEW JERSEY |
| `NM` | NEW MEXICO |
| `NT` | NETHERLANDS ANTILLES |
| `NV` | NEVADA |
| `NY` | NEW YORK |
| `NZ` | NEW ZEALAND |
| `OH` | OHIO |
| `OK` | OKLAHOMA |
| `OR` | OREGON |
| `PA` | PENNSYLVANIA |
| `PO` | PACIFIC OCEAN |
| `PR` | PUERTO RICO |
| `PS` | TRUST TERR OF PACIFIC ISLANDS |
| `RI` | RHODE ISLAND |
| `RP` | PHILIPINES |
| `RQ` | PUERTO RICO |
| `SC` | SOUTH CAROLINA |
| `SD` | SOUTH DAKOTA |
| `TD` | TRINIDAD AND TOBAGO |
| `TK` | TURKS AND CAICOS ISL |
| `TN` | TENNESSEE |
| `TO` | TONGA |
| `TX` | TEXAS |
| `UK` | UNITED KINGDOM |
| `UN` | UNKNOWN |
| `UT` | UTAH |
| `VA` | VIRGINIA |
| `VE` | VENEZUELA |
| `VI` | VIRGIN ISLANDS |
| `VQ` | VIRGIN ISLANDS |
| `VT` | VERMONT |
| `WA` | WASHINGTON |
| `WI` | WISCONSIN |
| `WN` | WEST INDIES |
| `WQ` | WAKE ISLAND |
| `WV` | WEST VIRGINIA |
| `WY` | WYOMING |

### `ev_tmzn`

| Code | Meaning |
|---|---|
| `ADT` | Atlantic Daylight Time |
| `AST` | Atlantic Standard Time |
| `BST` | Bering Standard Time |
| `CDT` | Central Daylight Time |
| `CST` | Central Standard Time |
| `EDT` | Eastern Daylight Time |
| `EST` | Eastern Standard Time |
| `HDT` | Hawaii Daylight Time |
| `HST` | Hawaii Standard Time |
| `MDT` | Mountain Daylight Time |
| `MST` | Mountain Standard Time |
| `PDT` | Pacific Daylight Time |
| `PST` | Pacific Standard Time |
| `UTC` | Coordinated Universal Time? Same as GMT |
| `YDT` | Yukon Daylight Time |
| `YST` | Yukon Standard Time |

### `ev_type`

| Code | Meaning |
|---|---|
| `ACC` | Accident |
| `INC` | Incident |
| `OCC` | Occurrence |
| `UNK` | Unknown Event Type |

### `gust_ind`

| Code | Meaning |
|---|---|
| `N` | Not Gusting |
| `U` | Unknown |
| `Y` | Gusting |

### `invest_agy`

| Code | Meaning |
|---|---|
| `F` | FAA |
| `N` | NTSB |
| `O` | Foreign |
| `U` | Unknown |

### `latlong_acq`

| Code | Meaning |
|---|---|
| `EST` | Lat/Long Estimated |
| `MEAS` | Lat/Long Measured |

### `light_cond`

| Code | Meaning |
|---|---|
| `DAWN` | Dawn |
| `DAYL` | Day |
| `DUSK` | Dusk |
| `NBRT` | Night/Bright |
| `NDRK` | Night/Dark |
| `NITE` | Night |
| `NR` | Not Reported |

### `mid_air`

| Code | Meaning |
|---|---|
| `N` | No |
| `Y` | Yes |

### `on_ground_collision`

| Code | Meaning |
|---|---|
| `N` | No |
| `Y` | Yes |

### `sky_cond_ceil`

| Code | Meaning |
|---|---|
| `BKN` | Broken |
| `NONE` |  |
| `OBSC` | Obscured |
| `OVC` | Overcast |
| `UNK` | Unknown |
| `VV` | Indefinite (V V) |

### `sky_cond_nonceil`

| Code | Meaning |
|---|---|
| `BKNT` | Thin Broken |
| `CLER` | Clear |
| `FEW` | Few |
| `OVCT` | Thin Overcast |
| `POBS` | Partial Obscuration |
| `SCAT` | Scattered |
| `UNK` | Unknown |

### `wind_dir_ind`

| Code | Meaning |
|---|---|
| `U` | Unknown |
| `V` | Variable |
| `Y` | Wind direction could be determined |

### `wind_vel_ind`

| Code | Meaning |
|---|---|
| `CALM` | Calm |
| `LVAR` | Light and Variable |
| `U` | Unknown |
| `UNK` | Unknown |
| `V` | Variable |

### `wx_brief_comp`

| Code | Meaning |
|---|---|
| `ABBR` | Abbreviated |
| `FULL` | Full |
| `NOTP` | Not pertinent |
| `PARB` | Partial - limited by briefer |
| `PARP` | Partial - limited by pilot |
| `UNK` | Unknown |

### `wx_cond_basic`

| Code | Meaning |
|---|---|
| `IMC` | Instrument Meteorological Cond |
| `UNK` | Unknown |
| `VMC` | Visual Meteorological Cond |

### `wx_int_precip`

| Code | Meaning |
|---|---|
| `HVY` | Heavy |
| `LGT` | Light |
| `MOD` | Moderate |
| `UNK` | Unknown |

### `wx_src_iic`

| Code | Meaning |
|---|---|
| `PILO` | Pilot |
| `UNK` | Unknown |
| `WFAC` | Weather Observation Facility |
| `WIT` | Witness |

## aircraft

### `acft_category`

| Code | Meaning |
|---|---|
| `AIR` | Airplane |
| `BALL` | Balloon |
| `BLIM` | Blimp |
| `GLI` | Glider |
| `GYRO` | Gyrocraft |
| `HELI` | Helicopter |
| `PLFT` | Powered-Lift |
| `ULTR` | Ultralight |
| `UNK` | Unknown |

### `acft_expl`

| Code | Meaning |
|---|---|
| `BOTH` | Ground and In-flight |
| `GRD` | Ground |
| `IFLT` | In-flight |
| `NONE` |  |
| `UNK` | Unknown |
| `UORG` | Unknown Origin |

### `acft_fire`

| Code | Meaning |
|---|---|
| `BOTH` | Ground and In-flight |
| `GRD` | Ground |
| `IFLT` | In-flight |
| `NONE` |  |
| `UNK` | Unknown |
| `UORG` | Unknown Origin |

### `acft_missing`

| Code | Meaning |
|---|---|
| `N` | No |
| `Y` | Yes |

### `acft_reg_cls`

| Code | Meaning |
|---|---|
| `FNFN` | Foreign Reg./Foreign Soil |
| `FNUS` | Foreign Registered/U.S. Soil |
| `MIL` | Military |
| `NREG` | Not Registered |
| `UNK` | Unknown |
| `USFN` | U.S. Registered/Foreign Soil |
| `USFO` | U.S. Registered/Foreign Oper. |
| `USUS` | U.S. Registered/U.S. Soil |

### `afm_hrs_since`

| Code | Meaning |
|---|---|
| `ACCI` | Time of Accident |
| `INSP` | Last Inspection |

### `air_medical`

| Code | Meaning |
|---|---|
| `N` | No |
| `Y` | Yes |

### `certs_held`

| Code | Meaning |
|---|---|
| `N` |  |
| `Y` | Yes - certificate holder |

### `damage`

| Code | Meaning |
|---|---|
| `DEST` | Destroyed |
| `MINR` | Minor |
| `NONE` |  |
| `SUBS` | Substantial |
| `UNK` | Unknown |

### `dest_same_local`

| Code | Meaning |
|---|---|
| `LOCL` | dest & departure same, accident can occur anywhere |
| `SAME` | crash at destination city |

### `dprt_pt_same_ev`

| Code | Meaning |
|---|---|
| `N` | No |
| `Y` | Yes |

### `elt_aided_loc_ev`

| Code | Meaning |
|---|---|
| `N` | No |
| `U` | Unknown |
| `Y` | Yes |

### `elt_install`

| Code | Meaning |
|---|---|
| `N` | No |
| `U` | Unknown |
| `Y` | Yes |

### `elt_oper`

| Code | Meaning |
|---|---|
| `N` | No |
| `U` | Unknown |
| `Y` | Yes |

### `elt_type`

| Code | Meaning |
|---|---|
| `C126` | C126 |
| `C91` | C91 |
| `C91A` | C91-A |
| `UNK` | Unknown |

### `evacuation`

| Code | Meaning |
|---|---|
| `N` | No |
| `Y` | Yes |

### `far_part`

| Code | Meaning |
|---|---|
| `091` | Part 91: General Aviation |
| `091F` | Part 91F: Special Flt Ops. |
| `091K` | Part 91 Subpart K: Fractional |
| `103` | Part 103: Ultralight |
| `105` | Part 105: Parachute Jumping |
| `121` | Part 121: Air Carrier |
| `125` | Part 125: 20+ Pax,6000+ lbs |
| `127` | Part 127: Sched AirCar w/Heli. |
| `129` | Part 129: Foreign |
| `133` | Part 133: Rotorcraft Ext. Load |
| `135` | Part 135: Air Taxi & Commuter |
| `137` | Part 137: Agricultural |
| `141` | Part 141: Pilot Schools |
| `ARMF` | Armed Forces |
| `NUSC` | Non-U.S., Commercial |
| `NUSN` | Non-U.S., Non-Commercial |
| `PUBF` | Public Use - Federal |
| `PUBL` | Public Use - Local |
| `PUBS` | Public Use - State |
| `PUBU` | Public Use |
| `UNK` | Unknown |

### `fixed_retractable`

| Code | Meaning |
|---|---|
| `RETR` | Retractable |

### `flight_plan_activated`

| Code | Meaning |
|---|---|
| `N` | No |
| `Y` | Yes |

### `flt_plan_filed`

| Code | Meaning |
|---|---|
| `CVFR` | Company VFR |
| `DFR` | Defense VFR |
| `IFR` | IFR |
| `MVFR` | Military VFR |
| `NONE` |  |
| `SVFR` | Special VFR |
| `UNK` | Unknown |
| `VFF` | Visual Flight - Following |
| `VFIF` | VFR/IFR |
| `VFR` | VFR |
| `VTP` | VFR on top |

### `homebuilt`

| Code | Meaning |
|---|---|
| `N` | No |
| `U` | Unknown |
| `Y` | Yes |

### `med_type_flight`

| Code | Meaning |
|---|---|
| `DISC` | Discretionary |
| `MEDE` | Medical Emergency |
| `ORGT` | Organ Transport |

### `oper_addr_same`

| Code | Meaning |
|---|---|
| `N` | No |
| `Y` | Yes |

### `oper_cert`

| Code | Meaning |
|---|---|
| `AGR` | Agriculture |
| `EXTL` | External Load |
| `UNK` | Unknown |

### `oper_dom_int`

| Code | Meaning |
|---|---|
| `DOM` | Domestic |
| `INT` | International |
| `UNK` | Unknown |

### `oper_individual_name`

| Code | Meaning |
|---|---|
| `N` | No |
| `Y` | Yes |

### `oper_pax_cargo`

| Code | Meaning |
|---|---|
| `CARG` | Cargo |
| `MAIL` | Mail |
| `PACA` | Passenger/Cargo |
| `PAX` | Passenger Only |
| `UNK` | Unknown |

### `oper_same`

| Code | Meaning |
|---|---|
| `N` | No |
| `Y` | Yes |

### `oper_sched`

| Code | Meaning |
|---|---|
| `NSCH` | Non-scheduled |
| `SCHD` | Scheduled |
| `UNK` | Unknown |

### `oprtng_cert`

| Code | Meaning |
|---|---|
| `N` | No |
| `Y` | Yes |

### `phase_flt_spec`

| Code | Meaning |
|---|---|
| `500` | Standing |
| `501` | Standing - pre-flight |
| `502` | Standing - starting engine(s) |
| `503` | Standing - engine(s) operating |
| `504` | Standing - engine(s) not operating |
| `505` | Standing - idling rotors |
| `510` | Taxi |
| `511` | Taxi - pushback/tow |
| `512` | Taxi - to takeoff |
| `513` | Taxi - from landing |
| `514` | Taxi - aerial |
| `520` | Takeoff |
| `521` | Takeoff - roll/run |
| `522` | Takeoff - initial climb |
| `523` | Takeoff - aborted |
| `530` | Climb |
| `531` | Climb - to cruise |
| `540` | Cruise |
| `541` | Cruise - normal |
| `542` | Maneuvering - holding (IFR) |
| `550` | Descent |
| `551` | Descent - normal |
| `552` | Descent - emergency |
| `553` | Descent - uncontrolled |
| `560` | Approach |
| `561` | Approach - VFR pattern - downwind |
| `562` | Approach - VFR pattern - turn to base |
| `563` | Approach - VFR pattern - base leg/base to final |
| `564` | Approach - VFR pattern - final approach |
| `565` | Go-around (VFR) |
| `566` | Approach - Initial approach fix (IAF) to final approach fix (FAF)/outer marker (IFR) |
| `567` | Approach - final approach fix (FAF)/outer marker to threshold (IFR) |
| `568` | Approach - circling (IFR) |
| `569` | Missed approach (IFR) |
| `570` | Landing |
| `571` | Landing - flare/touchdown |
| `572` | Landing - roll |
| `573` | Landing - aborted |
| `574` | Emergency landing |
| `575` | Emergency landing after takeoff |
| `576` | Emergency descent/landing |
| `580` | Maneuvering |
| `581` | Maneuvering - aerial application |
| `582` | Maneuvering - turn to reverse direction |
| `583` | Maneuvering - turn to landing area (emergency) |
| `590` | Hover |
| `591` | Hover - in ground effect |
| `592` | Hover - out of ground effect |
| `600` | Other |
| `610` | Unknown |

### `report_to_icao`

| Code | Meaning |
|---|---|
| `N` | No |
| `Y` | Yes |

### `second_pilot`

| Code | Meaning |
|---|---|
| `N` | No |
| `U` | Unknown |
| `Y` | Yes |

### `site_seeing`

| Code | Meaning |
|---|---|
| `N` | No |
| `Y` | Yes |

### `type_fly`

| Code | Meaning |
|---|---|
| `AAPL` | Aerial Application |
| `ADRP` | Air Drop |
| `AIRM` | Air Medical |
| `AOBV` | Aerial Observation |
| `ASHO` | Air Race/Show |
| `ATXA` | Air Taxi Non-Sched.(135A) |
| `ATXC` | Air Taxi Commuter |
| `ATXO` | Air Taxi Oper./Large Aircraft |
| `ATXS` | Air Taxi Sched./Not Commuter |
| `BANT` | Banner Tow |
| `BUS` | Business |
| `CRGO` | All Cargo Carriers |
| `EXEC` | Executive/Corporate |
| `EXLD` | External Load |
| `FERY` | Ferry |
| `FIRF` | Fire Fighting |
| `FLTS` | Flight Test |
| `GLDT` | Glider Tow |
| `HIRE` | For Hire |
| `ILGL` | Illegal Cargo/Operation |
| `INDS` | Industrial Special |
| `INST` | Instructional |
| `OTH` | Other |
| `OWRK` | Other Work Use |
| `PERS` | Personal |
| `POSI` | Positioning |
| `PUBU` | Public Use |
| `SCAC` | Scheduled Air Carrier |
| `SCRH` | Sched. Air Carrier Helicopter |
| `SITE` | Site Seeing |
| `SKYD` | Skydiving |
| `SUPP` | Supplemental/Commercial Oper. |
| `TVLC` | Travel Club |
| `UNK` | Unknown |

### `type_last_insp`

| Code | Meaning |
|---|---|
| `100H` | 100 Hour |
| `AAIP` | AAIP |
| `ANNL` | Annual |
| `COAW` | Continuous Airworthiness |
| `COND` | Conditional |
| `UNK` | Unknown |

## injury

### `inj_person_category`

| Code | Meaning |
|---|---|
| `ABRD` | Aboard |
| `CABN` | Cabin Crew |
| `CPLT` | Co-Pilot |
| `DSTU` | Dual Student |
| `FENG` | Flight Engineer |
| `FLTI` | Flight Instructor |
| `KPLT` | Check Pilot |
| `OCRW` | Other Crew |
| `PAX` | Passengers |
| `PLT` | Pilot in Command |

### `injury_level`

| Code | Meaning |
|---|---|
| `FATL` | Fatal |
| `MINR` | Minor |
| `NONE` |  |
| `SERS` | Serious |
| `TOTL` | Total |

## narratives

*No coded fields identified in the data dictionary for this table.*

## flight_crew

### `available_restraint`

| Code | Meaning |
|---|---|
| `3` | 3-point |
| `4` | 4-point |
| `5` | 5-point |
| `L` | Lap Only |
| `N` |  |
| `U` | Unknown |

### `bfr`

| Code | Meaning |
|---|---|
| `N` | No |
| `U` | Unknown |
| `Y` | Yes |

### `child_restraint`

| Code | Meaning |
|---|---|
| `CHR` | Lap-held |
| `LAP` | Child Restraint |
| `UNK` | Unknown |

### `crew_category`

| Code | Meaning |
|---|---|
| `CPLT` | Co-Pilot |
| `DSTU` | Student Pilot |
| `FENG` | Flight Engineer |
| `FLTI` | Flight Instructor |
| `KPLT` | Check Pilot |
| `OTHR` | Other Flight Crew |
| `PLT` | Pilot |

### `crew_inj_level`

| Code | Meaning |
|---|---|
| `FATL` | Fatal |
| `MINR` | Minor |
| `NONE` |  |
| `SERS` | Serious |
| `UNK` | Unknown |

### `crew_rat_endorse`

| Code | Meaning |
|---|---|
| `N` | No |
| `U` | Unknown |
| `Y` | Yes |

### `crew_sex`

| Code | Meaning |
|---|---|
| `F` | Female |
| `M` | Male |

### `crew_tox_perf`

| Code | Meaning |
|---|---|
| `N` | No |
| `U` | Unknown |
| `Y` | Yes |

### `infl_rest_depl`

| Code | Meaning |
|---|---|
| `A` |  |
| `N` | Inflatable Restraint Deployed |
| `U` | Unknown |
| `Y` | Yes |

### `infl_rest_inst`

| Code | Meaning |
|---|---|
| `A` |  |
| `N` | Inflatable Restraint Installed |
| `U` | Unknown |
| `Y` | Yes |

### `med_certf`

| Code | Meaning |
|---|---|
| `CL1` | Class 1 |
| `CL2` | Class 2 |
| `CL3` | Class 3 |
| `NONE` |  |
| `SPRT` | Sport Pilot |
| `UNK` | Unknown |

### `med_crtf_vldty`

| Code | Meaning |
|---|---|
| `EXP` | Expired |
| `NONE` |  |
| `NV` | Invalid Medical for flight |
| `UNK` | Unknown |
| `VNOW` | Valid Medical--no waivers/lim. |
| `VWW` | Valid Medical--w/ waivers/lim. |
| `WOWL` | Without Waivers/Limitations |
| `WWL` | With Waivers/Limitations |

### `mr_faa_med_certf`

| Code | Meaning |
|---|---|
| `CL1` | Class 1 |
| `CL2` | Class 2 |
| `CL3` | Class 3 |
| `NONE` |  |
| `SPRT` | Sport Pilot |
| `UNK` | Unknown |

### `pc_profession`

| Code | Meaning |
|---|---|
| `AM` | Aircraft Mechanic |
| `BUS` | Business |
| `CLGY` | Clergy |
| `DOCD` | Doctor/Dentist |
| `ENGR` | Engineer |
| `FARA` | Farmer/Rancher |
| `LAWY` | Lawyer |
| `NO` | No |
| `OMIL` | Other Military |
| `PCIV` | Civilian Pilot |
| `PMIL` | Military Pilot |
| `POLI` | Police |
| `RET` | Retired |
| `STU` | Student |
| `TEAC` | Teacher |
| `UNK` | Unknown |
| `YES` | Yes |

### `restraint_used`

| Code | Meaning |
|---|---|
| `3` | 3-point |
| `4` | 4-point |
| `5` | 5-point |
| `L` | Lap Only |
| `N` |  |
| `U` | Unknown |

### `seat_occ_pic`

| Code | Meaning |
|---|---|
| `CTR` | Center |
| `FRT` | Front |
| `LEFT` | Left |
| `REAR` | Rear |
| `RGT` | Right |
| `SNGL` | Single |
| `UNK` | Unknown |

### `seatbelts_used`

| Code | Meaning |
|---|---|
| `N` | No |
| `U` | Unknown |
| `Y` | Yes |

### `shldr_harn_used`

| Code | Meaning |
|---|---|
| `N` | No |
| `U` | Unknown |
| `Y` | Yes |

## engines

### `carb_fuel_injection`

| Code | Meaning |
|---|---|
| `CARB` | Carburetor |
| `FINJ` | Fuel Injected |

### `eng_type`

| Code | Meaning |
|---|---|
| `REC` | Reciprocating |
| `TF` | Turbo Fan |
| `TJ` | Turbo Jet |
| `TP` | Turbo Prop |
| `TS` | Turbo Shaft |
| `UNK` | Unknown |

### `hp_or_lbs`

| Code | Meaning |
|---|---|
| `HP` | Horsepower |
| `LBS` | Pounds |

### `propeller_type`

| Code | Meaning |
|---|---|
| `CONP` | Controllable Pitch |
| `FIXP` | Fixed Pitch |
