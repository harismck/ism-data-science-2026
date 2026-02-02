# vehicle_inspections
The centralized technical inspection database of the Association of Technical Inspection Companies of Lithuania 'TRANSEKSTA' contains data on the technical inspections of road vehicles carried out by associated companies. The dataset includes data since 2015, updated weekly. It features pseudonymized identifiers of the vehicle and technical inspection station, vehicle registration numbers and VIN (vehicle identification numbers), makes, models, classes, body types, specific purposes, production years, fuel types, smoke emissions, CO emissions at regular and elevated engine speeds, mileage, technical inspection conclusions, whether the inspection was passed, station municipality, inspection type, week-accurate date, and periodicity.
You can read more about the dataset [here]().


## inspection
Vehicle technical inspection data

### Columns:
- `unique_identifier` (orig. name `vda_id`) - Unique identifier

- `vehicle_identifier` (orig. name `tp_id`) - Vehicle identifier

- `registration_number` (orig. name `tp_valst_nr`) - Vehicle registration number

- `registration_number_markings` (orig. name `tp_valst_nr_zymejimas`) - Markings of letters, digits, and other symbols in the vehicle registration number

- `vin_number` (orig. name `tp_vin_nr`) - Vehicle Identification Number (VIN)

- `make` (orig. name `tp_marke`) - Vehicle make

- `model` (orig. name `tp_modelis`) - Vehicle model

- `class` (orig. name `tp_klase`) - Vehicle class

- `body_type` (orig. name `tp_kebulas`) - Vehicle body type

- `special_purpose` (orig. name `tp_spc`) - Vehicle special purpose or designation

- `manufacture_year` (orig. name `tp_pag_metai`) - Year of manufacture of the vehicle

- `fuel_type` (orig. name `tp_kuras`) - Type of fuel used by the vehicle

- `smoke_emission` (orig. name `tp_dumingumas`) - Smoke emission level of the vehicle

- `co_emission_standard` (orig. name `tp_co_tarsa`) - Carbon monoxide emission of the vehicle at standard engine RPM

- `co_emission_elevated` (orig. name `tp_co_tarsa_2000`) - Carbon monoxide emission of the vehicle at elevated engine RPM (>2000 RPM)

- `mileage_km` (orig. name `tp_rida_km`) - Total mileage of the vehicle in kilometers

- `inspection_station_code` (orig. name `ta_stoties_kodas`) - Code of the technical inspection station

- `inspection_station_municipality` (orig. name `ta_stoties_savivaldybe`) - Municipality of the technical inspection station

- `inspection_type` (orig. name `ta_tipas`) - Type of technical inspection carried out

- `inspection_type_en` - `inspection_type` translated to English using gpt-4o-2024-11-20.

- `inspection_conclusion_en` - `inspection_conclusion` translated to English using gpt-4o-2024-11-20.

- `inspection_conclusion` (orig. name `ta_isvada`) - Conclusion made about the vehicle condition during inspection

- `inspection_passed` (orig. name `ar_ta_islaikyta`) - Indicates if the vehicle passed the inspection

- `inspection_date_week` (orig. name `ta_savaites_data`) - Inspection date with week-level precision

- `inspection_periodicity_months` (orig. name `ta_periodiskumas_men`) - Inspection periodicity in months

