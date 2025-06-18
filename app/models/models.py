from sqlalchemy import text
from app.db.session import SessionLocal

def get_sql_server_version():
    db = SessionLocal()
    try:
        result = db.execute(text("SELECT @@VERSION")).scalar()
        return result
    finally:
        db.close()
