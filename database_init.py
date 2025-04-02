from sqlalchemy import text
from helper.sql_engine import get_engine


def create_database(connection):
    connection.execute(text('CREATE DATABASE IF NOT EXISTS alzheimer'))
    connection.execute(text('USE alzheimer'))
    print("Switched to 'alzheimer' database.")

def drop_existing_tables(connection):
    tables = []
    for table in tables:
        connection.execute(text(f'DROP TABLE IF EXISTS {table}'))
    print("Dropped all tables from previous runs (if they existed).")

def patient_table(connection):
    connection.execute(text('''
        CREATE TABLE IF NOT EXISTS patient (
            PatientID INT PRIMARY KEY,
            Age INT,
            Gender INT,
            Ethnicity INT,
            EducationLevel INT
        )
    '''))

def lifestyle_table(connection):
    connection.execute(text('''
        CREATE TABLE IF NOT EXISTS lifestyle (
            PatientID INT,
            BMI FLOAT,
            Smoking INT,
            AlcoholConsumption FLOAT,
            PhysicalActivity FLOAT,
            DietQuality FLOAT,
            SleepQuality FLOAT,
            FOREIGN KEY (PatientID) REFERENCES patient(PatientID)
        )
    '''))

def clinical_measurements_table(connection):
    connection.execute(text('''
        CREATE TABLE IF NOT EXISTS clinical_measurements (
            PatientID INT,
            SystolicBP INT,
            DiastolicBP INT,
            CholesterolTotal FLOAT,
            CholesterolLDL FLOAT,
            CholesterolHDL FLOAT,
            CholesterolTriglycerides FLOAT,
            FOREIGN KEY (PatientID) REFERENCES patient(PatientID)
        )
    '''))

def medical_history_table(connection):
    connection.execute(text('''
        CREATE TABLE IF NOT EXISTS medical_history (
            PatientID INT,
            FamilyHistoryAlzheimers INT,
            CardiovascularDisease INT,
            Diabetes INT,
            Depression INT,
            HeadInjury INT,
            Hypertension INT,
            FOREIGN KEY (PatientID) REFERENCES patient(PatientID)
        )
    '''))

def cognitive_functional_assessments_table(connection):
    connection.execute(text('''
        CREATE TABLE IF NOT EXISTS cognitive_functional_assessments (
            PatientID INT,
            MMSE FLOAT,
            FunctionalAssessment FLOAT,
            MemoryComplaints INT,
            BehavioralProblems INT,
            ADL FLOAT,
            FOREIGN KEY (PatientID) REFERENCES patient(PatientID)
        )
    '''))

def symptoms_table(connection):
    connection.execute(text('''
        CREATE TABLE IF NOT EXISTS symptoms (
            PatientID INT,
            Confusion INT,
            Disorientation INT,
            PersonalityChanges INT,
            DifficultyCompletingTasks INT,
            Forgetfulness INT,
            FOREIGN KEY (PatientID) REFERENCES patient(PatientID)
        )
    '''))

def alzheimers_data_table(connection):
    connection.execute(text('''
        CREATE TABLE IF NOT EXISTS alzheimers_data (
            PatientID INT,
            Diagnosis INT,
            FOREIGN KEY (PatientID) REFERENCES patient(PatientID)
        )
    '''))

def main():
    engine = get_engine()
    with engine.connect() as connection:
        create_database(connection)
        drop_existing_tables(connection)
        patient_table(connection)
        symptoms_table(connection)
        alzheimers_data_table(connection)
        cognitive_functional_assessments_table(connection)
        medical_history_table(connection)
        lifestyle_table(connection)
        clinical_measurements_table(connection)

if __name__ == "__main__":
    main()
