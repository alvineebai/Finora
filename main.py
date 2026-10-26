
from fastapi import FastAPI

app = FastAPI(title="Finora API")


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "application": "Finora API"
    }
