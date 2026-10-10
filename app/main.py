
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.schemas import MachineInput, PredictionResponse
from app.model_service import predict_failure

app = FastAPI(
    title="Predictive Maintenance API",
    description="API for predicting machine failures using a calibrated ML model.",
    version="1.0.0",
)

# Allow requests from the local frontend development server
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


@app.get("/")
def home():
    return {
        "message": "Predictive Maintenance API is running",
        "status": "success",
    }


@app.get("/health")
def health_check():
    return {"status": "healthy"}


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
