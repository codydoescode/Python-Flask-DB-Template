import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.engine import URL
from dotenv import load_dotenv

load_dotenv()

connection_string = URL.create(
    "mssql+pyodbc",
    username=os.getenv("DB_USERNAME"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=int(os.getenv("DB_PORT", default="1433")),
    database=os.getenv("DB_NAME"),
    query={
        "driver": "ODBC Driver 18 for SQL Server",
        "Encrypt": "yes",
        "TrustServerCertificate": "yes",
    }
)

engine = create_engine(connection_string)
SessionLocal = scoped_session(sessionmaker(bind=engine))
