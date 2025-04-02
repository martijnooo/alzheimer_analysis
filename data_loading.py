import pandas as pd
from helper.sql_engine import get_engine

# Get the SQL engine
engine = get_engine()

# Load dataset
csv_path = r"C:\Users\Martijn\Downloads\alzheimers_disease_data.csv"
df = pd.read_csv(csv_path)

# Define table column mappings
TABLE_COLUMNS = {
    "patient": ["PatientID", "Age", "Gender", "Ethnicity", "EducationLevel"],
    "lifestyle": ["PatientID", "BMI", "Smoking", "AlcoholConsumption", "PhysicalActivity", "DietQuality", "SleepQuality"],
    "clinical_measurements": ["PatientID", "SystolicBP", "DiastolicBP", "CholesterolTotal", "CholesterolLDL", "CholesterolHDL", "CholesterolTriglycerides"],
    "medical_history": ["PatientID", "FamilyHistoryAlzheimers", "CardiovascularDisease", "Diabetes", "Depression", "HeadInjury", "Hypertension"],
    "cognitive_assessments": ["PatientID", "MMSE", "FunctionalAssessment", "MemoryComplaints", "BehavioralProblems", "ADL"],
    "symptoms": ["PatientID", "Confusion", "Disorientation", "PersonalityChanges", "DifficultyCompletingTasks", "Forgetfulness"],
    "alzheimers_data": ["PatientID", "Diagnosis"]
}

def extract_dataframes(df, table_columns):
    """Extracts DataFrames based on the column mappings."""
    return {table: df.get(columns) for table, columns in table_columns.items()}

def save_to_database(dataframes, schema, engine):
    """
    Saves multiple DataFrames to a database.

    Parameters:
    - dataframes (dict): Dictionary of table names and corresponding DataFrames.
    - schema (str): Schema name in the database.
    - engine: SQLAlchemy engine for database connection.
    """
    with engine.connect() as connection:
        for table_name, df in dataframes.items():
            if df is not None:
                df.to_sql(table_name, schema=schema, con=connection, if_exists='append', index=False)

# Extract and save data
dataframes = extract_dataframes(df, TABLE_COLUMNS)
save_to_database(dataframes, schema="alzheimer", engine=engine)
