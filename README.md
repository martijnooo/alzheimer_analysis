# Table of Contents

1. [Patient Information](#patient-information)
    - [Patient ID](#patient-id)
    - [Demographic Details](#demographic-details)
2. [Lifestyle Factors](#lifestyle-factors)
3. [Medical History](#medical-history)
4. [Clinical Measurements](#clinical-measurements)
5. [Cognitive and Functional Assessments](#cognitive-and-functional-assessments)
6. [Symptoms](#symptoms)
7. [Diagnosis Information](#diagnosis-information)

---

## Patient Information

### Patient ID
- **PatientID**: A unique identifier assigned to each patient (4751 to 6900).

### Demographic Details
- **Age**: The age of the patients ranges from 60 to 90 years.
- **Gender**: Gender of the patients, where:
  - `0`: Male
  - `1`: Female
- **Ethnicity**: The ethnicity of the patients, coded as:
  - `0`: Caucasian
  - `1`: African American
  - `2`: Asian
  - `3`: Other
- **EducationLevel**: The education level of the patients, coded as:
  - `0`: None
  - `1`: High School
  - `2`: Bachelor's
  - `3`: Higher

---

## Lifestyle Factors
- **BMI**: Body Mass Index of the patients, ranging from 15 to 40.
- **Smoking**: Smoking status, where:
  - `0`: No
  - `1`: Yes
- **AlcoholConsumption**: Weekly alcohol consumption in units, ranging from 0 to 20.
- **PhysicalActivity**: Weekly physical activity in hours, ranging from 0 to 10.
- **DietQuality**: Diet quality score, ranging from 0 to 10.
- **SleepQuality**: Sleep quality score, ranging from 4 to 10.

---

## Medical History
- **FamilyHistoryAlzheimers**: Family history of Alzheimer's Disease, where:
  - `0`: No
  - `1`: Yes
- **CardiovascularDisease**: Presence of cardiovascular disease, where:
  - `0`: No
  - `1`: Yes
- **Diabetes**: Presence of diabetes, where:
  - `0`: No
  - `1`: Yes
- **Depression**: Presence of depression, where:
  - `0`: No
  - `1`: Yes
- **HeadInjury**: History of head injury, where:
  - `0`: No
  - `1`: Yes
- **Hypertension**: Presence of hypertension, where:
  - `0`: No
  - `1`: Yes

---

## Clinical Measurements
- **SystolicBP**: Systolic blood pressure, ranging from 90 to 180 mmHg.
- **DiastolicBP**: Diastolic blood pressure, ranging from 60 to 120 mmHg.
- **CholesterolTotal**: Total cholesterol levels, ranging from 150 to 300 mg/dL.
- **CholesterolLDL**: Low-density lipoprotein cholesterol levels, ranging from 50 to 200 mg/dL.
- **CholesterolHDL**: High-density lipoprotein cholesterol levels, ranging from 20 to 100 mg/dL.
- **CholesterolTriglycerides**: Triglycerides levels, ranging from 50 to 400 mg/dL.

---

## Cognitive and Functional Assessments
- **MMSE**: Mini-Mental State Examination score, ranging from 0 to 30. Lower scores indicate cognitive impairment.
- **FunctionalAssessment**: Functional assessment score, ranging from 0 to 10. Lower scores indicate greater impairment.
- **MemoryComplaints**: Presence of memory complaints, where:
  - `0`: No
  - `1`: Yes
- **BehavioralProblems**: Presence of behavioral problems, where:
  - `0`: No
  - `1`: Yes
- **ADL**: Activities of Daily Living score, ranging from 0 to 10. Lower scores indicate greater impairment.

---

## Symptoms
- **Confusion**: Presence of confusion, where:
  - `0`: No
  - `1`: Yes
- **Disorientation**: Presence of disorientation, where:
  - `0`: No
  - `1`: Yes
- **PersonalityChanges**: Presence of personality changes, where:
  - `0`: No
  - `1`: Yes
- **DifficultyCompletingTasks**: Presence of difficulty completing tasks, where:
  - `0`: No
  - `1`: Yes
- **Forgetfulness**: Presence of forgetfulness, where:
  - `0`: No
  - `1`: Yes

---

## Diagnosis Information
- **Diagnosis**: Diagnosis status for Alzheimer's Disease, where:
  - `0`: No
  - `1`: Yes