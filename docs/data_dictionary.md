# Data dictionary

Field-level metadata for each of the six curated core tables. Descriptions are taken from NTSB's *eADMSPUB_DataDictionary*. Fields with coded values link to [controlled_vocabularies.md](controlled_vocabularies.md). Missingness percentages reflect the latest extraction run (see `logs/data_quality.md`).


## events

| Field | Type | Description | Missing% | Notes |
|---|---|---|---:|---|
| `ev_id` | text | Each event is assigned a unique 10- or 11-digit alphanumeric code in the database. This code, used in conjunction with the aircraft_key variable, is used to reference all database records. All databas… | 0% | primary / foreign key |
| `ntsb_no` | text |  | 0% |  |
| `ev_type` | text | Refers to a regulatory definition of the event severity. The severity of a general aviation accident or incident is classified as the combination of the highest level of injury sustained by the person… | 0% | see [controlled vocabularies](controlled_vocabularies.md) |
| `ev_date` | text | The date of the event. Dates are be entered in the format: MM/DD/YYYY | 0% |  |
| `ev_dow` | text | The day of the week on which the event occurred. | 0% | see [controlled vocabularies](controlled_vocabularies.md) |
| `ev_time` | numeric | The local time of the event in 4-digit, 24-hour format. | 2.0% |  |
| `ev_tmzn` | text | The 3-letter code corresponding to the time zone in which the event took place. Note that both the time zone and daylight saving / standard time are referenced in the 3-letter code. | 7.1% | see [controlled vocabularies](controlled_vocabularies.md) |
| `ev_city` | text | The city or place location closest to the site of the event. | 0% |  |
| `ev_state` | text | The state in which the event occurred (if in the US). Also includes the Pacific Ocean as PO, the Caribbean Sea as CB, the Atlantic Ocean as AO, the Gulf of Mexico as GM, and Puerto Rico as PR. | 18.6% | see [controlled vocabularies](controlled_vocabularies.md) |
| `ev_country` | text | The country in which the event took place. | 0% |  |
| `ev_site_zipcode` | numeric | The 5-digit address zip code for the event location. A zip code lookup for addresses within the US and US territories is available from the US Postal Service at http://www.usps.com/zip4/. A Canadian p… | 45.8% |  |
| `ev_year` | integer | The calendar year in which the event took place. | 0% |  |
| `ev_month` | integer | Event date month | 0% |  |
| `mid_air` | text | Indicate whether accident involved an in-flight collision between aircraft. Note that a midair collision is recorded as a single accident (1 event ID) with multiple aircraft (2+ aircraft keys) | 98.8% | see [controlled vocabularies](controlled_vocabularies.md) |
| `on_ground_collision` | text | Indicate whether a collision occurred between 2 or more aircraft on the ground. Note that a collision is recorded as a single accident (1 event ID) with multiple aircraft (2+ aircraft keys) | 98.8% | see [controlled vocabularies](controlled_vocabularies.md) |
| `latitude` | text | Latitude and longitude are entered for the event site in degrees, minutes of arc, and seconds of arc. If the event occurred on an airport, the published coordinates for that airport can be entered. If… | 40.7% |  |
| `longitude` | text | Latitude and longitude are entered for the event site in degrees, minutes of arc, and seconds of arc. If the event occurred on an airport, the published coordinates for that airport can be entered. If… | 40.3% |  |
| `latlong_acq` | text | Indicates whether the reported Latitude/Longitude coordinates represent a measurement from GPS or other official source, or whether they were estimated. | 67.6% | see [controlled vocabularies](controlled_vocabularies.md) |
| `apt_name` | text | Airport name if the event took place within 3 miles of an airport, or the involved aircraft was taking off from, or on approach to, an airport. | 72.3% |  |
| `ev_nr_apt_id` | text | If the event did not occur on an airport/airstrip, this is the nearest | 64.0% |  |
| `ev_nr_apt_loc` | text | Indicate whether the event took place on or off an airport/airstrip. | 55.3% | see [controlled vocabularies](controlled_vocabularies.md) |
| `apt_dist` | numeric | The distance from the center of the involved airport to the event site in statute miles. | 29.2% |  |
| `apt_dir` | numeric | The direction from the center of the involved airport to the event site in degrees magnetic. | 75.9% |  |
| `apt_elev` | numeric | The elevation of the involved airport in feet above mean sea level (MSL). | 73.5% |  |
| `wx_brief_comp` | numeric | The type(s) of weather briefing(s) obtained by the accident flight crew. | 100.0% | see [controlled vocabularies](controlled_vocabularies.md) |
| `wx_src_iic` | text | This variable refers to the source of the weather information cited in the event record. Used in conjunction with the weather variables in the "events" table. | 51.4% | see [controlled vocabularies](controlled_vocabularies.md) |
| `wx_obs_time` | numeric | The time (local) that the weather observation was taken. Time should be in a 4 digit, 24-hour format. | 61.7% |  |
| `wx_obs_dir` | integer | The direction of the event site from the weather reporting station in degrees magnetic. | 0% |  |
| `wx_obs_fac_id` | text | The alphanumeric identifier for the weather observation facility used to provide the weather data for the event. A weather reporting station ID lookup tool is available from the National Weather Servi… | 60.9% |  |
| `wx_obs_elev` | numeric | The elevation of the event site in feet above mean sea level (MSL). | 53.0% |  |
| `wx_obs_dist` | integer | The distance from the weather reporting station to the event site in nautical miles. | 0% |  |
| `wx_obs_tmzn` | text | The local time zone corresponding to the weather observation time entered. | 96.4% |  |
| `light_cond` | text | Select the lighting condition that best describes the conditions at the time of the event. | 53.0% | see [controlled vocabularies](controlled_vocabularies.md) |
| `sky_cond_nonceil` | text | The cloud condition (non-ceiling) type present at the time of the event. Indicate the cloud condition (non-ceiling) type present at the time of the event. A non-ceiling is defined as any cloud layer o… | 55.7% | see [controlled vocabularies](controlled_vocabularies.md) |
| `sky_nonceil_ht` | numeric | The height, in feet above ground level (AGL) of the lowest cloud condition (non-ceiling) present at the time of the event . Height means the vertical distance between the ground or water and the lowes… | 29.2% |  |
| `sky_ceil_ht` | numeric | The height, in feet above ground level (AGL), of the lowest cloud ceiling reported at the event location at the time of the event. Ceiling height is the vertical distance between the ground or water a… | 29.2% |  |
| `sky_cond_ceil` | text | The type of cloud coverage that best describes the cloud ceiling at the time of the accident. A ceiling is defined as any cloud layer of greater than 4/8 coverage. | 59.3% | see [controlled vocabularies](controlled_vocabularies.md) |
| `vis_rvr` | numeric | Visibility Runway Visual Range (Feet) | 100.0% |  |
| `vis_rvv` | numeric | Visibility Runway Visual Value (Statute Miles) | 100.0% |  |
| `vis_sm` | numeric | The visibility, either in-flight or ground visibility as appropriate, at the time of the event. Visibility is reported in statute miles. | 62.1% |  |
| `wx_temp` | numeric | The reported ambient air temperature at the time of the event, typically reported in degrees Celsius. | 29.2% |  |
| `wx_dew_pt` | numeric | Dew point is the temperature to which air must be cooled to become saturated by the water vapor already present in the air. Aviation weather reports normally include the air temperature and dew point … | 29.2% |  |
| `wind_dir_deg` | integer | The local indicated wind direction at the time of the event. This is the wind direction at the time of the event. Wind direction is recorded as the average direction over a 2-minute period. Direction … | 0% |  |
| `wind_dir_ind` | text | Indicate whether the reported wind direction was variable. Wind direction may be considered variable if, during the 2-minute evaluation period, the speed is 6 knots or less. Direction may be considere… | 0% | see [controlled vocabularies](controlled_vocabularies.md) |
| `wind_vel_kts` | numeric | The local reported wind speed at the time of the event. Reported wind speed is determined using the average of speed over a 2-minute period. Direction may be considered variable if over the 2-minute e… | 60.5% |  |
| `wind_vel_ind` | text | The local reported wind speed at the time of the event. Reported wind speed is determined using the average of speed over a 2-minute period. Direction may be considered variable if, over the 2-minute … | 0% | see [controlled vocabularies](controlled_vocabularies.md) |
| `gust_ind` | text | Indicate whether gusting winds were reported locally at the time of the event. Gusting wind is defined in chapter 5 of the Federal Meteorological Handbook as rapid fluctuations in wind speed with a va… | 0% | see [controlled vocabularies](controlled_vocabularies.md) |
| `gust_kts` | integer | If gusting winds were reported locally at the time of the event, indicate the reported velocity of wind gusts in knots. Wind gust speed is defined in chapter 5 of the Federal Meteorological Handbook a… | 0% |  |
| `altimeter` | numeric | Barometric pressure at the event sight at the time of the event. Barometric pressure is also referred to as the altimeter setting in reference to the altimeter adjustment for changing barometric press… | 29.2% |  |
| `wx_dens_alt` | numeric | Density altitude is a measure of air density, not altitude. Aircraft performance calculations are based on the standard conditions of 59 degrees Fahrenheit,  pressure 29.92 inches of mercury at sea le… | 100.0% |  |
| `wx_int_precip` | numeric | The intensity of any precipitation phenomena occurring at the time of the event. | 100.0% | see [controlled vocabularies](controlled_vocabularies.md) |
| `metar` | text | METAR is an acronym for the French words meaning "Aviation Routine Weather Report." METAR reports are the primary form of surface weather report. METAR reports are made hourly from tower controlled ai… | 66.0% |  |
| `ev_highest_injury` | text | Indicate the highest level of injury among all injuries sustained as a result of the event. | 9.1% | see [controlled vocabularies](controlled_vocabularies.md) |
| `inj_f_grnd` | numeric | Number of persons on the ground who were involved in the event who received fatal injuries. An example of a person on the ground who might be involved in an accident would be airport ground services o… | 81.0% |  |
| `inj_m_grnd` | numeric | Number of persons on the ground who were involved in the event who received no injuries. An example of a person on the ground who might be involved in an accident would be airport ground services or m… | 76.3% |  |
| `inj_s_grnd` | numeric | Number of persons on the ground who were involved in the event who received serious injuries. An example of a person on the ground who might be involved in an accident would be airport ground services… | 81.0% |  |
| `inj_tot_f` | integer | The total number of injuries of each severity level that resulted from an event. | 0% |  |
| `inj_tot_m` | integer | The total number of injuries of each severity level that resulted from an event. | 0% |  |
| `inj_tot_n` | integer | The total number of injuries of each severity level that resulted from an event. | 0% |  |
| `inj_tot_s` | integer | The total number of injuries of each severity level that resulted from an event. | 0% |  |
| `inj_tot_t` | numeric | The total number of all injuries that resulted from an event. | 9.1% |  |
| `invest_agy` | text | Investigating Agency | 0% | see [controlled vocabularies](controlled_vocabularies.md) |
| `ntsb_docket` | numeric | This variable is now obsolete. To obtain certified copies of the NTSB Public Docket for a particular accident, or for more information, please contact the NTSB Public Inquiries Branch at 202-314-6551. | 100.0% |  |
| `ntsb_notf_from` | numeric | NTSB Notification Source | 100.0% |  |
| `ntsb_notf_date` | numeric | NTSB Notification Date | 100.0% |  |
| `ntsb_notf_tm` | numeric | NTSB Notification Time | 100.0% |  |
| `fiche_number` | numeric | Fiche Number and/or location -used to find docket information | 100.0% |  |
| `lchg_date` | text | Date of most recent change to record | 0% |  |
| `lchg_userid` | text | User who most recently changed record | 0% |  |
| `wx_cond_basic` | text | The basic weather conditions at the time of the event. | 51.4% | see [controlled vocabularies](controlled_vocabularies.md) |
| `faa_dist_office` | numeric | FAA Flight Standards District Office (FSDO) closest to the event site. This variable is not well populated in the database. | 100.0% |  |
| `dec_latitude` | numeric |  | 40.7% |  |
| `dec_longitude` | numeric |  | 40.3% |  |
| `source_archive` | text |  | 0% | curation-added field |

## aircraft

| Field | Type | Description | Missing% | Notes |
|---|---|---|---:|---|
| `ev_id` | text | Each event is assigned a unique 10- or 11- digit alphanumeric code in the database. This code, used in conjunction with the aircraft_key variable, is used to reference all database records. All databa… | 0% | primary / foreign key |
| `aircraft_key` | integer | The aircraft key variable is used to distinguish between individual aircraft in the event of an occurrence involving more than one aircraft. For example. if two aircraft collide, they will be assigned… | 0% | foreign key (within event) |
| `regis_no` | text | The full registration (tail) number of the involved aircraft, including the International Civil Aviation Organization (ICAO) country prefix. Note: the prefix for US registered aircraft is "N." | 0% |  |
| `ntsb_no` | text | Each accident/incident is assigned a unique case number by the NTSB. This number is used as a reference in all documents referring to the event. The first 3 characters are a letter abbreviation of the… | 0% |  |
| `acft_missing` | text | Indicate whether an aircraft is classified and missing. | 0% | see [controlled vocabularies](controlled_vocabularies.md) |
| `far_part` | text | The applicable regulation part (14 CFR) or authority the aircraft was operating under at the time of the accident. | 9.4% | see [controlled vocabularies](controlled_vocabularies.md) |
| `flt_plan_filed` | text | The type of ATC flight plan filed for the accident flight. This includes plans filed before departure, plans filed enroute, company flight plans, and scheduled routing plans. | 64.8% | see [controlled vocabularies](controlled_vocabularies.md) |
| `flight_plan_activated` | text | If an ATC flight plan was filed for the accident flight, indicate whether that flight plan was activated. A previously filed flight plan is activated or opened through radio contact with a Flight Serv… | 75.0% | see [controlled vocabularies](controlled_vocabularies.md) |
| `damage` | text | Indicate the severity of damage to the accident aircraft. For the purposes of this variable, aircraft damage categories are defined in 49 CFR 830.2. | 33.2% | see [controlled vocabularies](controlled_vocabularies.md) |
| `acft_fire` | text | Indicate the occurrence of an aircraft fire. | 28.9% | see [controlled vocabularies](controlled_vocabularies.md) |
| `acft_expl` | text | Indicate the occurrence of an aircraft explosion. | 28.9% | see [controlled vocabularies](controlled_vocabularies.md) |
| `acft_make` | text | Name of the manufacturer of the involved aircraft. If the involved aircraft is certified as "amateur-built," include the name of manufacturer of the kit or plans when appropriate. | 0% |  |
| `acft_model` | text | The full alphanumeric aircraft model code, including any applicable series or derivative identifiers. For example, a 200 series Boeing 737 is entered as 737-200. | 0% |  |
| `acft_series` | text | This refers to derivative versions of the same model. For example, the Boeing 737-200 and 737-400 series. This variable is not consistently populated throughout the database. | 77.0% |  |
| `acft_serial_no` | text | The full aircraft serial number, as assigned by the manufacturer or certificator. | 40.6% |  |
| `cert_max_gr_wt` | numeric | The actual certificated max gross weight for the aircraft involved in the occurrence. This should be the same as the maximum gross weight indicated on the aircraft weight and balance. Maximum gross we… | 74.6% |  |
| `acft_category` | text | The category of the involved aircraft. In this case, the definition of aircraft category is the same as that used with respect to the certification, ratings, privileges, and limitations of airmen. Als… | 28.9% | see [controlled vocabularies](controlled_vocabularies.md) |
| `acft_reg_cls` | numeric | Aircraft registration class codes include both the foreign/domestic registration type and the foreign/domestic location of operation at the time of the accident. | 100.0% | see [controlled vocabularies](controlled_vocabularies.md) |
| `homebuilt` | text | Indicate whether the involved aircraft was certified with a Special Airworthiness Certificate (FAA Form 8130-7), in the experimental category as an amateur-built aircraft. | 0% | see [controlled vocabularies](controlled_vocabularies.md) |
| `fc_seats` | numeric | Refers to the number of aircraft seats by type. | 78.9% |  |
| `cc_seats` | numeric | Refers to the number of aircraft seats by type. | 94.9% |  |
| `pax_seats` | numeric | Refers to the number of aircraft seats by type. | 79.7% |  |
| `total_seats` | numeric | Total (actual) number of seats for which the accident aircraft is configured. The number of seats may vary between aircraft based on operation and / or configuration differences such as cargo versus p… | 50.8% |  |
| `num_eng` | numeric | The total number of engines on the accident aircraft. | 44.9% |  |
| `fixed_retractable` | text | Indicate whether the accident aircraft had either fixed or retractable landing gear. | 0% | see [controlled vocabularies](controlled_vocabularies.md) |
| `type_last_insp` | text | Indicate the type of inspection most recently conducted on the involved aircraft. | 73.4% | see [controlled vocabularies](controlled_vocabularies.md) |
| `date_last_insp` | text | The calendar date of the most recent aircraft inspection in the format MM/DD/YYYY. | 76.2% |  |
| `afm_hrs_last_insp` | numeric | The total number of operating hours accumulated on the aircraft airframe since the last inspection. | 91.4% |  |
| `afm_hrs` | numeric | The total number of operating hours on the aircraft airframe. You must also indicate whether the entered time was measured at the last inspection or at the time of the accident. | 77.7% |  |
| `elt_install` | text | Indicate whether the accident aircraft had an Emergency Locator Transmitter (ELT) installed. The ELT is a transmitter that contains an inertia switch that activates in the event of an impact. This sig… | 74.2% | see [controlled vocabularies](controlled_vocabularies.md) |
| `elt_oper` | text | If the accident aircraft had an Emergency Locator Transmitter (ELT) installed, indicate whether the transmitter was activated as a result of the accident. The ELT is a transmitter that contains an ine… | 82.4% | see [controlled vocabularies](controlled_vocabularies.md) |
| `elt_aided_loc_ev` | text | If the accident aircraft had an Emergency Locator Transmitter (ELT) installed, and the transmitter was activated as a result of the accident, indicate whether the transmitted signal aided in locating … | 94.5% | see [controlled vocabularies](controlled_vocabularies.md) |
| `elt_type` | text | The elt_type field is used to inicate the FAA Technical Service Order (TSO) an aircraft Emergency Locator Transmitter was designed under. | 83.6% | see [controlled vocabularies](controlled_vocabularies.md) |
| `owner_acft` | text | Full name of the owner of the accident aircraft as it appears on the aircraft registration. | 54.3% |  |
| `owner_street` | text | Street address of the registered owner of the accident aircraft. | 65.6% |  |
| `owner_city` | text | City address of the registered owner of the accident aircraft. | 52.3% |  |
| `owner_state` | text | State address of the registered owner of the accident aircraft. | 52.3% |  |
| `owner_country` | text | Country address of the registered owner of the accident aircraft. | 34.0% |  |
| `owner_zip` | text | Zip code of the registered owner of the accident aircraft. A zip code lookup for addresses within the US and US territories is available from the US Postal Service at http://www.usps.com/zip4/. A Cana… | 54.3% |  |
| `oper_individual_name` | text | Indicate whether the aircraft operator is an individual. | 0% | see [controlled vocabularies](controlled_vocabularies.md) |
| `oper_name` | text | The full name of the operator of the accident aircraft. This typically refers to an organization or group (e.g., airline or corporation) rather than the pilot. | 59.4% |  |
| `oper_same` | numeric | Indicate whether the aircraft operator is the same as the registered owner. | 100.0% | see [controlled vocabularies](controlled_vocabularies.md) |
| `oper_dba` | text | If the accident aircraft was operated by a business, air carrier, or as part of a code share agreement, this is the carrier, business, or code share name. | 96.5% |  |
| `oper_addr_same` | numeric | Indicate whether the aircraft operator address is the same as the registered owner address. | 100.0% | see [controlled vocabularies](controlled_vocabularies.md) |
| `oper_street` | text | The street address of the operator of the accident aircraft. | 70.7% |  |
| `oper_city` | text | The city address of the operator of the accident aircraft. | 53.5% |  |
| `oper_state` | text | The state address of the operator of the accident aircraft. | 53.9% |  |
| `oper_country` | text | The country address of the operator of the accident aircraft. | 34.8% |  |
| `oper_zip` | text | The zip code of the operator of the accident aircraft. A zip code lookup for addresses within the U.S. and U.S. territories is available from the U.S. Postal Service at http://www.usps.com/zip4/. A Ca… | 57.4% |  |
| `oper_code` | text | For air carriers and commercial operators, this is the operator's 4-character designator code. This is the unique four-letter identifier assigned to the airline by the Federal Aviation Administration.… | 96.9% |  |
| `certs_held` | text | Indicate whether the operator holds a commercial operating certificate, an air taxi operating certificate, or an air carrier operating certificate | 48.4% | see [controlled vocabularies](controlled_vocabularies.md) |
| `oprtng_cert` | numeric | Operator holds a certificate to operate large aircraft other than those listed. Large aircraft are defined as those with more than a 12,500-pound maximum certificated takeoff weight. | 100.0% | see [controlled vocabularies](controlled_vocabularies.md) |
| `oper_cert` | numeric | Indicate whether operator was certified for operations under 14 CFR 133 or 137. | 100.0% | see [controlled vocabularies](controlled_vocabularies.md) |
| `oper_cert_num` | text | If the aircraft operator holds a commercial operating certificate, an air taxi operating certificate, or an air carrier operating certificate, indicate the number of that certificate. | 98.0% |  |
| `oper_sched` | text | If the accident aircraft was conducting air carrier operations under 14 CFR 121, 125, 129, or 135, indicate whether it was operating as a "scheduled or commuter" air carrier or as a "non-scheduled or … | 90.6% | see [controlled vocabularies](controlled_vocabularies.md) |
| `oper_dom_int` | text | If the accident flight was conducting revenue operations under 14 CFR 121, 125, 129, or 135, indicate whether the accident aircraft was operating on a domestic or international flight at the time of t… | 94.9% | see [controlled vocabularies](controlled_vocabularies.md) |
| `oper_pax_cargo` | text | If the accident flight was conducting revenue operations under 14 CFR 121, 125, 129, or 135,  indicate the make up of aircraft load. | 94.9% | see [controlled vocabularies](controlled_vocabularies.md) |
| `type_fly` | text | If the accident aircraft was operating under 14 CFR part 91,103,133, or 137, this was the primary purpose of flight. | 34.8% | see [controlled vocabularies](controlled_vocabularies.md) |
| `second_pilot` | text | Indicate whether a second pilot was on board the aircraft. The role of the second pilot will vary with the type of operation. For example, an instructional flight may have a flight instructor as a sec… | 59.0% | see [controlled vocabularies](controlled_vocabularies.md) |
| `dprt_pt_same_ev` | text | Indicate whether the event took place at the point of departure. | 68.0% | see [controlled vocabularies](controlled_vocabularies.md) |
| `dprt_apt_id` | text | The identification code for the involved aircraft's departure airport. A limited airport identifier lookup tool is available from the IATA at http://www1.iata.org/codes/index.htm. | 63.7% |  |
| `dprt_city` | text | The city address of the involved aircraft's last departure point prior to the event. | 62.5% |  |
| `dprt_state` | text | The state address of the involved aircraft's last departure point prior to the event. | 66.4% |  |
| `dprt_country` | text | The country address of the involved aircraft's last departure point prior to the event. | 62.1% |  |
| `dprt_time` | numeric | The time of the involved aircraft's most recent departure prior to the event. The local time of departure is in 4-digit, 24-hour format. | 73.4% |  |
| `dprt_timezn` | numeric | The time zone corresponding to the indicated time of departure | 100.0% |  |
| `dest_same_local` | numeric | Indicate whether the accident flight was intended as a local flight, returning to the departure airport with no intermediate stops. Examples of local flights might include sightseeing, flight instruct… | 100.0% | see [controlled vocabularies](controlled_vocabularies.md) |
| `dest_apt_id` | text | The identification code for the intended destination airport. A limited airport identifier lookup tool is available from the IATA at http://www1.iata.org/codes/index.htm. | 75.0% |  |
| `dest_city` | text | Indicate the city address of the involved aircraft's intended destination. | 73.4% |  |
| `dest_state` | text | The state address of the involved aircraft's intended destination. | 75.4% |  |
| `dest_country` | text | Indicate the country address of the involved aircraft's intended destination. | 73.0% |  |
| `phase_flt_spec` | numeric | Rather than getting phase of flight from this location, refer to the phase_of_flight variable in the occurrences table. All occurrences include information about the phase of flight in which the occur… | 100.0% | see [controlled vocabularies](controlled_vocabularies.md) |
| `report_to_icao` | numeric | Indicate whether a report was sent to the International Civil Aviation Organization (ICAO). | 100.0% | see [controlled vocabularies](controlled_vocabularies.md) |
| `evacuation` | numeric | Indicate whether an emergency evacuation was performed. "Emergency Evacuation" is any exit from the aircraft in which an emergency egress system is involved. This may also include egress through the m… | 100.0% | see [controlled vocabularies](controlled_vocabularies.md) |
| `lchg_date` | text | Date of most recent change to record | 0% |  |
| `lchg_userid` | text | User who most recently changed record | 0% |  |
| `afm_hrs_since` | text | Indicate whether the time entered for total airframe hours was measured at the last inspection or at the time of the accident. | 0% | see [controlled vocabularies](controlled_vocabularies.md) |
| `rwy_num` | text | If the involved aircraft was taking off, landing, or on approach to a designated runway, this refers to the runway identifier. The Runway ID is in a 2-digit format corresponding to the first 2 digits … | 80.9% |  |
| `rwy_len` | numeric | If the involved aircraft was taking off, landing, or on approach to a designated runway, this refers to the actual length available. | 80.5% |  |
| `rwy_width` | numeric | If the involved aircraft was taking off, landing, or on approach to a designated runway, this refers to the runway width and indicates the units (meters/feet) of measurement. If the runway or airstrip… | 80.5% |  |
| `site_seeing` | text | Indicate whether the accident aircraft was conducting revenue sightseeing operations at the time of the accident. Revenue sightseeing flight  is defined in 14 CFR 135.1 as sightseeing flights for comp… | 52.7% | see [controlled vocabularies](controlled_vocabularies.md) |
| `air_medical` | text | Indicate whether the accident aircraft was operating as an Air Medical Flight at the time of the accident. An "Air Medical Flight" is defined as an operation for the purpose of carrying medical person… | 53.1% | see [controlled vocabularies](controlled_vocabularies.md) |
| `med_type_flight` | text | If the involved aircraft was operating as a medical flight, indicate the type of medical service it was providing. | 99.6% | see [controlled vocabularies](controlled_vocabularies.md) |
| `acft_year` | numeric |  | 50.4% |  |
| `fuel_on_board` | numeric | Fuel On Board at Takeoff in gallons | 84.8% |  |
| `commercial_space_flight` | boolean |  | 0% |  |
| `unmanned` | boolean |  | 0% |  |
| `ifr_equipped_cert` | boolean |  | 0% |  |
| `elt_mounted_aircraft` | boolean |  | 0% |  |
| `elt_connected_antenna` | boolean |  | 0% |  |
| `elt_manufacturer` | text |  | 84.8% |  |
| `elt_model` | text |  | 85.9% |  |
| `elt_reason_other` | numeric |  | 100.0% |  |
| `source_archive` | text |  | 0% | curation-added field |

## injury

| Field | Type | Description | Missing% | Notes |
|---|---|---|---:|---|
| `ev_id` | text | Each event is assigned a unique 10- or 11-digit alphanumeric code in the database. This code, used in conjunction with the aircraft_key variable, is used to reference all database records. All databas… | 0% | primary / foreign key |
| `aircraft_key` | integer | The aircraft key is used in conjunction with the event id number ("ev_id") to distinguish between aircraft and accident in the event of a collision between 2 or more aircraft. For example, a midair co… | 0% | foreign key (within event) |
| `inj_person_category` | text | Reading data from the injury table requires the combination of the inj_person_category, injury_level, and inj_person_count variables. The desired inj_person_category and injury_level variables are set… | 0% | composite key component; see [controlled vocabularies](controlled_vocabularies.md) |
| `injury_level` | text | Reading data from the injury table requires the combination of the inj_person_category, injury_level, and inj_person_count variables. The desired inj_person_category and injury_level variables are set… | 0% | composite key component; see [controlled vocabularies](controlled_vocabularies.md) |
| `inj_person_count` | numeric | Reading data from the injury table requires the combination of the inj_person_category, injury_level, and inj_person_count variables. The desired inj_person_category and injury_level variables are set… | 26.1% |  |
| `lchg_date` | text | Date of most recent change to record | 0% |  |
| `lchg_userid` | text | User who most recently changed record | 0% |  |
| `source_archive` | text |  | 0% | curation-added field |

## narratives

| Field | Type | Description | Missing% | Notes |
|---|---|---|---:|---|
| `ev_id` | text | Each event is assigned a unique 10- or 11- digit alphanumeric code in the database. This code, used in conjunction with the aircraft_key variable, is used to reference all database records. All databa… | 0% | primary / foreign key |
| `aircraft_key` | integer | The aircraft key is used in conjunction with the event id number ("ev_id") to distinguish between aircraft and accident in the event of a collision between 2 or more aircraft. For example, a midair co… | 0% | foreign key (within event) |
| `narr_accp` | text | A description of what occurred in chronological order, the circumstances leading to the accident, and the nature of the accident.  Includes details related to the terrain and  wreckage distribution if… | 11.3% |  |
| `narr_accf` | text | An updated narrative of the accident occurrences and details released with the final event report. | 47.9% |  |
| `narr_cause` | text | Includes a text summary statement of the probable cause findings included in the event investigation record. Not available until the final report is released. | 47.9% |  |
| `narr_inc` | numeric | Not included in the NTSB database. | 100.0% |  |
| `lchg_date` | text | Date of most recent change to record | 0% |  |
| `lchg_userid` | text | User who most recently changed record | 0% |  |
| `source_archive` | text |  | 0% | curation-added field |

## flight_crew

| Field | Type | Description | Missing% | Notes |
|---|---|---|---:|---|
| `ev_id` | text | Each event is assigned a unique 10- or 11- digit alphanumeric code in the database. This code, used in conjunction with the aircraft_key variable, is used to reference all database records. All databa… | 0% | primary / foreign key |
| `aircraft_key` | integer | The aircraft key is used in conjunction with the event id number ("ev_id") to distinguish between aircraft and accident in the event of a collision between 2 or more aircraft. For example, a midair co… | 0% | foreign key (within event) |
| `crew_no` | integer | Unique Identifier for Each Pilot | 0% | composite key component |
| `crew_category` | text | Category that best describes the responsibilities of the flight crew member at the time of the accident. Complete this section for only one crew member at a time. You will be given the opportunity to … | 0% | see [controlled vocabularies](controlled_vocabularies.md) |
| `crew_age` | numeric | Indicates the age of the flight crew member in years | 23.8% |  |
| `crew_sex` | text | Indicates the sex of the flight crew member | 30.2% | see [controlled vocabularies](controlled_vocabularies.md) |
| `crew_city` | text | Indicates the city of residence of the flight crew member | 14.3% |  |
| `crew_res_state` | text | Indicates the state of residence of the flight crew member using the 2 letter state abbreviation | 14.3% |  |
| `crew_res_country` | text | Indicates the country of residence of the flight crew member using a country code abbreviation | 7.9% |  |
| `med_certf` | text | The class of medical certificate held by the crew member at the time of the event. Note that this question refers to the class of medical certificate issued and not the valid operating privileges base… | 25.4% | see [controlled vocabularies](controlled_vocabularies.md) |
| `med_crtf_vldty` | text | The validity of the medical certificate (and waivers) held by the crew member at the time of the event. Note that this question is referring to the valid operating privileges of the certificate based … | 38.1% | see [controlled vocabularies](controlled_vocabularies.md) |
| `date_lst_med` | text | Question refers to the medical certification requirement of 14 CFR 61.3(c). The standards for medical certification are prescribed in 14 CFR 67. | 36.5% |  |
| `crew_rat_endorse` | numeric | Indicate whether the flight crew member held an appropriate type-rating or endorsement for the accident aircraft. Examples of aircraft requiring a type rating include large aircraft (more than 12,000 … | 100.0% | see [controlled vocabularies](controlled_vocabularies.md) |
| `crew_inj_level` | text | The level of injury sustained by the crew member as a result of the event. | 4.8% | see [controlled vocabularies](controlled_vocabularies.md) |
| `seatbelts_used` | numeric | Indicate whether the flight crew member was wearing a seat belt at the time of the event. | 100.0% | see [controlled vocabularies](controlled_vocabularies.md) |
| `shldr_harn_used` | numeric | If the flight crew member was wearing a seat belt at the time of the event, indicate whether they were also wearing a shoulder harness. | 100.0% | see [controlled vocabularies](controlled_vocabularies.md) |
| `crew_tox_perf` | text | Indicate whether toxicology tests were performed on the flight crew and/or passengers. May be used to test for medications, alcohol, or other substances. If performed, the results of toxicology tests … | 57.1% | see [controlled vocabularies](controlled_vocabularies.md) |
| `seat_occ_pic` | text | Indicates the seat occupied by the flight crew member at the time of the event. If the seat is not known, select "unknown." | 4.8% | see [controlled vocabularies](controlled_vocabularies.md) |
| `pc_profession` | text | The profession that most closely matches the principal profession of the crew member. | 17.5% | see [controlled vocabularies](controlled_vocabularies.md) |
| `bfr` | numeric | This question refers to the requirement of 14 CFR 61.56 for the completion of a flight review (or equivalent) at least every 24 months in order to act as pilot in command of an aircraft. This variable… | 100.0% | see [controlled vocabularies](controlled_vocabularies.md) |
| `bfr_date` | text | The date of the most recent flight review (as required by 14 CFR 61.56) completed by the crew member. Acceptable alternatives include the satisfactory completion of one or more phases of an FAA-sponso… | 58.7% |  |
| `ft_as_of` | text | This field is used to indicate the date when the reported flight crew flight hour data was recorded (e.g. the date of the last flight log book entry, date of medical ceritificate application, or date … | 71.4% |  |
| `lchg_date` | text | Date of most recent change to record | 0% |  |
| `lchg_userid` | text | User who most recently changed record | 0% |  |
| `seat_occ_row` | numeric |  | 93.7% |  |
| `infl_rest_inst` | text | Inflatable Restraint Installed | 33.3% | see [controlled vocabularies](controlled_vocabularies.md) |
| `infl_rest_depl` | text | Inflatable Restraint Deployed | 90.5% | see [controlled vocabularies](controlled_vocabularies.md) |
| `child_restraint` | numeric | Child Restraint | 100.0% | see [controlled vocabularies](controlled_vocabularies.md) |
| `med_crtf_limit` | text |  | 66.7% |  |
| `mr_faa_med_certf` | numeric | Most Recent FAA Medical Certificate | 100.0% | see [controlled vocabularies](controlled_vocabularies.md) |
| `pilot_flying` | boolean |  | 0% |  |
| `available_restraint` | text | Available Restraint Type | 33.3% | see [controlled vocabularies](controlled_vocabularies.md) |
| `restraint_used` | text | Restraint Used | 33.3% | see [controlled vocabularies](controlled_vocabularies.md) |
| `source_archive` | text |  | 0% | curation-added field |

## engines

| Field | Type | Description | Missing% | Notes |
|---|---|---|---:|---|
| `ev_id` | text | Each event is assigned a unique 10- or 11- digit alphanumeric code in the database. This code, used in conjunction with the aircraft_key variable, is used to reference all database records. All databa… | 0% | primary / foreign key |
| `aircraft_key` | integer | The aircraft key is used in conjunction with the event id number ("ev_id") to distinguish between aircraft and accident in the event of a collision between 2 or more aircraft. For example, a midair co… | 0% | foreign key (within event) |
| `eng_no` | integer | For aircraft with more than one engine, each engine is assigned a unique identifier code to distinguish between engines. This number is used in the occurrence/seq_of_events codes involving an engine. … | 0% | composite key component |
| `eng_type` | text | The type of engine(s) on the involved aircraft. | 0% | see [controlled vocabularies](controlled_vocabularies.md) |
| `eng_mfgr` | text | Select the appropriate engine manufacturer from the drop-down list. If the manufacturer is not listed, type the full name of the engine manufacturer. | 0% |  |
| `eng_model` | text | Enter the full engine model and series designation. | 7.5% |  |
| `power_units` | numeric | The power output of the engine. In order to be meaningful, this value must be accompanied by an indication of units of measure, either horsepower (HP) or pounds of thrust (lbs.) | 39.6% |  |
| `hp_or_lbs` | text | Specifies whether the unit of measure for the indicated engine power rating is horsepower (hp) or pounds of thrust (lbs). | 37.7% | see [controlled vocabularies](controlled_vocabularies.md) |
| `lchg_userid` | text | User who most recently changed record | 0% |  |
| `lchg_date` | text | Date of most recent change to record | 0% |  |
| `carb_fuel_injection` | text | For those aircraft with reciprocating (piston) engines, indicate whether the fuel system type is carbureted or fuel-injected. | 32.1% | see [controlled vocabularies](controlled_vocabularies.md) |
| `propeller_type` | text | If the involved aircraft is propeller-driven, indicate whether the propeller is fixed pitch or controllable/variable pitch. | 52.8% | see [controlled vocabularies](controlled_vocabularies.md) |
| `propeller_make` | text |  | 52.8% |  |
| `propeller_model` | text |  | 67.9% |  |
| `eng_time_total` | numeric |  | 0% |  |
| `eng_time_last_insp` | numeric |  | 0% |  |
| `eng_time_overhaul` | numeric |  | 0% |  |
| `source_archive` | text |  | 0% | curation-added field |
