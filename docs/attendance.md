# Attendance
The dataset contains monthly attendance data of students by school, class, and subject. The data is obtained from the electronic diaries of 'UAB Tavo mokykla' TAMO and the 'National Education Center' diary 'Mano dienynas' for the periods 2018-09-01 to 2024-08-31 and 2012-09-01 to 2024-08-31, respectively.
You can read more about the dataset [here]().

## attendance
Monthly attendance data by school and subject. Collected from electronic diaries "TAMO" and "Mano dienynas".

### Columns:
- `unique_id` (orig. name `vda_id`) - Unique identifier

- `report_period` (orig. name `atask_laikotarp`) - Period for which the attendance data is reported

- `school_code` (orig. name `ins_kodas`) - Education institution (school) code in the Register of Legal Entities

- `division_code` (orig. name `pad_kodas`) - Code of the institution division in the National Education Registry

- `student_class` (orig. name `srautas`) - Student group (grades 1 to 12)

- `subject_code` (orig. name `mokdal_kodas`) - Subject code

- `electronic_diary` (orig. name `dienynas`) - Name of the electronic diary used (NAŠC or TAMO)

- `student_count_nsa` (orig. name `nsa_mokiniu_sk`) - Number of students in the school according to the NSA student registry on the first day of the reporting period

- `student_count_diary` (orig. name `dienyno_mokiniu_sk`) - Number of students determined according to diary entries during the reporting period, counting unique students who received at least one entry in the diary (attendance or grade)

- `excused_lessons_illness` (orig. name `pateisintu_del_ligos_sk`) - Number of excused lessons due to illness

- `excused_lessons_other` (orig. name `pateisintu_del_kita_sk`) - Number of excused lessons for other reasons

- `unexcused_lessons` (orig. name `nepateisintu_sk`) - Number of unexcused lessons


## subject
Data on school subjects.

### Columns:
- `unique_id` (orig. name `vda_id`) - Unique identifier

- `electronic_diary` (orig. name `dienynas`) - Name of the electronic diary used (NAŠC or TAMO)

- `subject_code` (orig. name `mokdal_kodas`) - Subject code

- `subject_name` (orig. name `mokdal_pav`) - Name of the subject

- `subject_name_en` - `subject_name` translated to English using gpt-4o-2024-11-20.


## school
Schools data

### Columns:
- `unique_id` (orig. name `vda_id`) - Unique identifier

- `school_code` (orig. name `ins_kodas`) - Education institution (school) code in the Register of Legal Entities

- `division_code` (orig. name `pad_kodas`) - Code of the institution division in the National Education Registry

- `school_name` (orig. name `ins_pav`) - Name of the education institution (school) in the Register of Legal Entities

- `division_name` (orig. name `pad_pav`) - Name of the institution division in the National Education Registry

- `municipality_code` (orig. name `sav_kodas`) - Municipality code

- `municipality_name` (orig. name `sav_pav`) - Municipality name

