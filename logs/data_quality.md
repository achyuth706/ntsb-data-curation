# Data Quality Report

Generated: 2026-05-06T05:26:15.396146+00:00  
Run ID: `20260506T052615Z`

This report reflects the most recent extraction run. Missing values are reported, not removed — the curation principle is to preserve original data and make limitations visible (Peer, Green & Stephenson, 2014; Bruce & Hillmann, 2004).

## `events`

- Rows: **253**
- Columns: **74**
- Within-archive duplicates dropped: 0
- Cross-archive duplicates dropped (kept latest): 3

**Columns with missing values:**

| Column | Missing | % |
|---|---:|---:|
| `wx_brief_comp` | 253 | 100.0% |
| `vis_rvr` | 253 | 100.0% |
| `vis_rvv` | 253 | 100.0% |
| `wx_dens_alt` | 253 | 100.0% |
| `wx_int_precip` | 253 | 100.0% |
| `ntsb_docket` | 253 | 100.0% |
| `ntsb_notf_from` | 253 | 100.0% |
| `ntsb_notf_date` | 253 | 100.0% |
| `ntsb_notf_tm` | 253 | 100.0% |
| `fiche_number` | 253 | 100.0% |
| `faa_dist_office` | 253 | 100.0% |
| `mid_air` | 250 | 98.8% |
| `on_ground_collision` | 250 | 98.8% |
| `wx_obs_tmzn` | 244 | 96.4% |
| `inj_f_grnd` | 205 | 81.0% |
| `inj_s_grnd` | 205 | 81.0% |
| `inj_m_grnd` | 193 | 76.3% |
| `apt_dir` | 192 | 75.9% |
| `apt_elev` | 186 | 73.5% |
| `apt_name` | 183 | 72.3% |
| `latlong_acq` | 171 | 67.6% |
| `metar` | 167 | 66.0% |
| `ev_nr_apt_id` | 162 | 64.0% |
| `vis_sm` | 157 | 62.1% |
| `wx_obs_time` | 156 | 61.7% |
| `wx_obs_fac_id` | 154 | 60.9% |
| `wind_vel_kts` | 153 | 60.5% |
| `sky_cond_ceil` | 150 | 59.3% |
| `sky_cond_nonceil` | 141 | 55.7% |
| `ev_nr_apt_loc` | 140 | 55.3% |
| `wx_obs_elev` | 134 | 53.0% |
| `light_cond` | 134 | 53.0% |
| `wx_src_iic` | 130 | 51.4% |
| `wx_cond_basic` | 130 | 51.4% |
| `ev_site_zipcode` | 116 | 45.8% |
| `latitude` | 103 | 40.7% |
| `dec_latitude` | 103 | 40.7% |
| `longitude` | 102 | 40.3% |
| `dec_longitude` | 102 | 40.3% |
| `apt_dist` | 74 | 29.2% |
| `sky_nonceil_ht` | 74 | 29.2% |
| `sky_ceil_ht` | 74 | 29.2% |
| `wx_temp` | 74 | 29.2% |
| `wx_dew_pt` | 74 | 29.2% |
| `altimeter` | 74 | 29.2% |
| `ev_state` | 47 | 18.6% |
| `ev_highest_injury` | 23 | 9.1% |
| `inj_tot_t` | 23 | 9.1% |
| `ev_tmzn` | 18 | 7.1% |
| `ev_time` | 5 | 2.0% |

## `aircraft`

- Rows: **256**
- Columns: **94**
- Within-archive duplicates dropped: 0
- Cross-archive duplicates dropped (kept latest): 3

**Columns with missing values:**

| Column | Missing | % |
|---|---:|---:|
| `acft_reg_cls` | 256 | 100.0% |
| `oper_same` | 256 | 100.0% |
| `oper_addr_same` | 256 | 100.0% |
| `oprtng_cert` | 256 | 100.0% |
| `oper_cert` | 256 | 100.0% |
| `dprt_timezn` | 256 | 100.0% |
| `dest_same_local` | 256 | 100.0% |
| `phase_flt_spec` | 256 | 100.0% |
| `report_to_icao` | 256 | 100.0% |
| `evacuation` | 256 | 100.0% |
| `elt_reason_other` | 256 | 100.0% |
| `med_type_flight` | 255 | 99.6% |
| `oper_cert_num` | 251 | 98.0% |
| `oper_code` | 248 | 96.9% |
| `oper_dba` | 247 | 96.5% |
| `cc_seats` | 243 | 94.9% |
| `oper_dom_int` | 243 | 94.9% |
| `oper_pax_cargo` | 243 | 94.9% |
| `elt_aided_loc_ev` | 242 | 94.5% |
| `afm_hrs_last_insp` | 234 | 91.4% |
| `oper_sched` | 232 | 90.6% |
| `elt_model` | 220 | 85.9% |
| `fuel_on_board` | 217 | 84.8% |
| `elt_manufacturer` | 217 | 84.8% |
| `elt_type` | 214 | 83.6% |
| `elt_oper` | 211 | 82.4% |
| `rwy_num` | 207 | 80.9% |
| `rwy_len` | 206 | 80.5% |
| `rwy_width` | 206 | 80.5% |
| `pax_seats` | 204 | 79.7% |
| `fc_seats` | 202 | 78.9% |
| `afm_hrs` | 199 | 77.7% |
| `acft_series` | 197 | 77.0% |
| `date_last_insp` | 195 | 76.2% |
| `dest_state` | 193 | 75.4% |
| `flight_plan_activated` | 192 | 75.0% |
| `dest_apt_id` | 192 | 75.0% |
| `cert_max_gr_wt` | 191 | 74.6% |
| `elt_install` | 190 | 74.2% |
| `type_last_insp` | 188 | 73.4% |
| `dprt_time` | 188 | 73.4% |
| `dest_city` | 188 | 73.4% |
| `dest_country` | 187 | 73.0% |
| `oper_street` | 181 | 70.7% |
| `dprt_pt_same_ev` | 174 | 68.0% |
| `dprt_state` | 170 | 66.4% |
| `owner_street` | 168 | 65.6% |
| `flt_plan_filed` | 166 | 64.8% |
| `dprt_apt_id` | 163 | 63.7% |
| `dprt_city` | 160 | 62.5% |
| `dprt_country` | 159 | 62.1% |
| `oper_name` | 152 | 59.4% |
| `second_pilot` | 151 | 59.0% |
| `oper_zip` | 147 | 57.4% |
| `owner_acft` | 139 | 54.3% |
| `owner_zip` | 139 | 54.3% |
| `oper_state` | 138 | 53.9% |
| `oper_city` | 137 | 53.5% |
| `air_medical` | 136 | 53.1% |
| `site_seeing` | 135 | 52.7% |
| `owner_city` | 134 | 52.3% |
| `owner_state` | 134 | 52.3% |
| `total_seats` | 130 | 50.8% |
| `acft_year` | 129 | 50.4% |
| `certs_held` | 124 | 48.4% |
| `num_eng` | 115 | 44.9% |
| `acft_serial_no` | 104 | 40.6% |
| `oper_country` | 89 | 34.8% |
| `type_fly` | 89 | 34.8% |
| `owner_country` | 87 | 34.0% |
| `damage` | 85 | 33.2% |
| `acft_fire` | 74 | 28.9% |
| `acft_expl` | 74 | 28.9% |
| `acft_category` | 74 | 28.9% |
| `far_part` | 24 | 9.4% |

## `injury`

- Rows: **1,375**
- Columns: **8**
- Within-archive duplicates dropped: 0
- Cross-archive duplicates dropped (kept latest): 0

**Columns with missing values:**

| Column | Missing | % |
|---|---:|---:|
| `inj_person_count` | 359 | 26.1% |

## `narratives`

- Rows: **71**
- Columns: **9**
- Within-archive duplicates dropped: 0
- Cross-archive duplicates dropped (kept latest): 0

**Columns with missing values:**

| Column | Missing | % |
|---|---:|---:|
| `narr_inc` | 71 | 100.0% |
| `narr_accf` | 34 | 47.9% |
| `narr_cause` | 34 | 47.9% |
| `narr_accp` | 8 | 11.3% |

## `flight_crew`

- Rows: **63**
- Columns: **34**
- Within-archive duplicates dropped: 0
- Cross-archive duplicates dropped (kept latest): 0

**Columns with missing values:**

| Column | Missing | % |
|---|---:|---:|
| `crew_rat_endorse` | 63 | 100.0% |
| `seatbelts_used` | 63 | 100.0% |
| `shldr_harn_used` | 63 | 100.0% |
| `bfr` | 63 | 100.0% |
| `child_restraint` | 63 | 100.0% |
| `mr_faa_med_certf` | 63 | 100.0% |
| `seat_occ_row` | 59 | 93.7% |
| `infl_rest_depl` | 57 | 90.5% |
| `ft_as_of` | 45 | 71.4% |
| `med_crtf_limit` | 42 | 66.7% |
| `bfr_date` | 37 | 58.7% |
| `crew_tox_perf` | 36 | 57.1% |
| `med_crtf_vldty` | 24 | 38.1% |
| `date_lst_med` | 23 | 36.5% |
| `infl_rest_inst` | 21 | 33.3% |
| `available_restraint` | 21 | 33.3% |
| `restraint_used` | 21 | 33.3% |
| `crew_sex` | 19 | 30.2% |
| `med_certf` | 16 | 25.4% |
| `crew_age` | 15 | 23.8% |
| `pc_profession` | 11 | 17.5% |
| `crew_city` | 9 | 14.3% |
| `crew_res_state` | 9 | 14.3% |
| `crew_res_country` | 5 | 7.9% |
| `crew_inj_level` | 3 | 4.8% |
| `seat_occ_pic` | 3 | 4.8% |

## `engines`

- Rows: **53**
- Columns: **18**
- Within-archive duplicates dropped: 0
- Cross-archive duplicates dropped (kept latest): 0

**Columns with missing values:**

| Column | Missing | % |
|---|---:|---:|
| `propeller_model` | 36 | 67.9% |
| `propeller_type` | 28 | 52.8% |
| `propeller_make` | 28 | 52.8% |
| `power_units` | 21 | 39.6% |
| `hp_or_lbs` | 20 | 37.7% |
| `carb_fuel_injection` | 17 | 32.1% |
| `eng_model` | 4 | 7.5% |

