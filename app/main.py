
from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from app.schemas import MachineInput, PredictionResponse
from app.model_service import predict_failure


# Project directories
BASE_DIR = Path(__file__).resolve().parent.parent
FRONTEND_DIR = BASE_DIR / "frontend"


# FastAPI application
app = FastAPI(
    title="Predictive Maintenance API",
    description="API for predicting machine failures using a calibrated ML model.",
    version="1.0.0",
)


# CORS for local frontend development
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500",
        "http://127.0.0.1:5501",
        "http://localhost:5501",
    ],
    allow_credentials=False,
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"],
)


# Serve CSS and JavaScript
app.mount(
    "/static",
    StaticFiles(directory=str(FRONTEND_DIR)),
    name="static",
)


# Serve frontend homepage
@app.get("/", include_in_schema=False)
def home():
    return FileResponse(FRONTEND_DIR / "index.html")


# Health check
@app.get("/health")
def health_check():
    return {"status": "healthy"}


# Machine failure prediction
@app.post("/predict", response_model=PredictionResponse)
def predict(data: MachineInput):
    return predict_failure(
        machine_type=data.Type,
        air_temperature=data.air_temperature,
        process_temperature=data.process_temperature,
        rotational_speed=data.rotational_speed,
        torque=data.torque,
        tool_wear=data.tool_wear,
    )
