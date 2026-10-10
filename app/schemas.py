
from pydantic import BaseModel, Field


class MachineInput(BaseModel):
    Type: str = Field(..., pattern="^[LMH]$")

    air_temperature: float = Field(..., gt=0)
    process_temperature: float = Field(..., gt=0)
    rotational_speed: int = Field(..., gt=0)
    torque: float = Field(..., ge=0)
    tool_wear: int = Field(..., ge=0)


class PredictionResponse(BaseModel):
    failure_prediction: int
    failure_probability: float
    threshold: float
    message: str
