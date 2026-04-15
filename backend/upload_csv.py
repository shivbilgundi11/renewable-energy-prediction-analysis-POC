import pandas as pd
from fastapi import APIRouter, UploadFile, File
from sqlalchemy import text
from database import engine

router = APIRouter()

@router.post("/upload-csv")
async def upload_csv(file: UploadFile = File(...)):

    # Read CSV
    df = pd.read_csv(file.file)

    with engine.connect() as conn:

        # STEP 1: Clear old dataset
        conn.execute(text("TRUNCATE TABLE historical_generation RESTART IDENTITY"))

        # STEP 2: Insert new dataset
        for _, row in df.iterrows():
            conn.execute(
                text("""
                INSERT INTO historical_generation (timestamp, generation_mw)
                VALUES (:timestamp, :generation)
                """),
                {
                    "timestamp": row["timestamp"],
                    "generation": row["generation_mw"]
                }
            )

        conn.commit()

    return {
        "message": "CSV uploaded successfully",
        "rows_inserted": len(df)
    }