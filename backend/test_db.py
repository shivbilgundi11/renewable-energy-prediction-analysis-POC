from database import engine
from sqlalchemy import text

try:
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1"))
        print("Database connection is ACTIVE")
        print("Test Query Result:", result.scalar())

except Exception as e:
    print("Connection failed:", e)