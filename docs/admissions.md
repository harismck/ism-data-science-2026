# Admissions
Information on applications to higher education instutitions in Lithuania from 2024. 
Data is provided by Association of Lithuanian Higher Education Institutions for Joint Admissions (LAMA BPO).

You can read more about the dataset [here](https://data.gov.lt/datasets/2914/).

## Table: applications
Data on applications to higher education institutions. Each row represents an application (`application_id`).


### Columns:
- **application_id** (orig. name `prasymo_id`) - Application identification number

- **person_id** (orig. name `asmens_id`) - Person identification number

- **choice_at** (orig. name `pasirinkimo_data`) - Date and time when the program choice was made

- **admission_stage** (orig. name `priemimo_etapas`) - Name of the admission stage. Possible values: `Main Admission`, `First Round Of Additional Admission`, `Second Round Of Additional Admission`

- **stage_start_date** (orig. name `etapo_pradzia`) - Start date of the admission stage

- **stage_end_date** (orig. name `etapo_pabaiga`) - End date of the admission stage

- **priority_number** (orig. name `prioriteto_nr`) - Priority number of the study/training program in the application

- **program_id** (orig. name `programos_id`) - Program identification number

- **financing** (orig. name `finansavimas`) - Type of program financing - indicates whether the studies will be financed by the state.. Possible values: `Financed`, `Non-financed`, `Stipend`

- **participated_in_competition** (orig. name `ar_dalyvavo_konkurse`) - Flag indicating whether the application participated in the admission competition (requirements for participation are met)

- **invited** (orig. name `ar_pakviete`) - Flag indicating whether the applicant received an invitation

- **invitation_date** (orig. name `pakvietimo_data`) - Date when the invitation to the study program was received. NULL if the applicant was not invited.

- **signed** (orig. name `ar_pasirase`) - Flag indicating whether the invited person signed a contract for the study program


## Table: profiles
Demographic data about individuals who applied to higher education institutions. 
Each row represents a unique applicant in a given admission year. 
The table includes both Lithuanian citizens and foreigners.
Note that education data for older applicants may be incomplete due to lack of digitization.


### Columns:
- **person_id** (orig. name `asmens_id`) - Person ID

- **is_possibly_foreigner** (orig. name `ar_galimai_uzsienietis`) - Flag indicating if the person is potentially a foreigner. If no personal ID is provided in the admission application, 
it is assumed they are a foreigner. However, this flag does not include foreigners who have a Lithuanian personal ID.


- **birth_year** (orig. name `gimimo_metai`) - Person's birth year

- **gender** (orig. name `lytis`) - Person's gender. Possible values: `M`, `F`

- **education_institution_code** (orig. name `issilavinim_inst_jar`) - Education institution (school) code in the Register of Legal Entities

- **education_institution** (orig. name `issilavinimo_institucija`) - Educational institution where the person obtained their maturity certificate

- **education_municipality_code** (orig. name `issilavinimo_sav_kodas`) - Municipality code of the educational institution

- **education_municipality** (orig. name `issilavinimo_sav`) - Name of the municipality where the educational institution is located

- **residence_municipality** (orig. name `asm_gyv_sav`) - Name of the municipality where the person resided at the time of application

- **residence_place** (orig. name `asm_gyv_vieta`) - Person's place of residence (settlement) at the time of application. Censored if there are less than 10 applicants in the settlement.

- **residence_type** (orig. name `asm_gyv_tipas`) - Type of settlement at the time of application.. Possible values: `homestead`, `railway_station`, `city`, `village`, `town`

- **application_year** (orig. name `prasymo_metai`) - Year when the application was submitted


## Table: programs
Data on higher education programs in Lithuanian higher education institutions. Each record represents 
an educational program offered by a higher education institution for a specific admission year. 


### Columns:
- **program_id** (orig. name `programos_id`) - Program ID

- **program_year** (orig. name `programos_metai`) - Time period for which the program data is relevant

- **program_code** (orig. name `programos_valst_kodas`) - Code of the educational program

- **program_name** (orig. name `programos_pavadinimas`) - Name of the educational program

- **program_name_en** - `program_name` translated to English using claude-3.5-sonnet.

- **institution_code** (orig. name `istaigos_jar`) - Educational institution code in the Register of Legal Entities

- **code_validation** (orig. name `jar_validacija`) - Validation of the legal entity code. Possible values: `Valid`

- **educational_institution** (orig. name `mokymo_istaiga`) - Name of the educational institution

- **county_code** (orig. name `apskrities_kodas`) - Code of the county where the study/training program is conducted

- **county** (orig. name `apskritis`) - Text value of the 1st level hierarchy value for the classified value (in Lithuanian)

- **municipality_code** (orig. name `savivaldybes_kodas`) - Code of the municipality where the study/training program is conducted

- **municipality** (orig. name `savivaldybe`) - Text value of the 2nd level hierarchy value for the classified value (in Lithuanian)

