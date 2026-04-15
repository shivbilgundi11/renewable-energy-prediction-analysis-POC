from fastapi import FastAPI
from upload_csv import router as upload_router

app = FastAPI()

app.include_router(upload_router)

@app.get("/")
def home():
    return {"message": "Solar POC Backend Running Successfully"}