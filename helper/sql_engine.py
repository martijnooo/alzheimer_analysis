from sqlalchemy import create_engine

def get_engine():
    # Prompt the user for username and password
    username = input("Enter your MySQL username: ")
    password = input("Enter your MySQL password: ")

    host = '127.0.0.1'
    port = '3306'
    db = "alzheimer"

    # Create an engine to connect to MySQL
    return create_engine(f'mysql+pymysql://{username}:{password}@{host}:{port}/{db}')