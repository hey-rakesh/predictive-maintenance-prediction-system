
from pathlib import Path

import joblib


# Project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Model artifacts folder
ARTIFACTS_DIR = BASE_DIR / "Predictive Maintenance"

# Saved model and threshold paths
MODEL_PATH = ARTIFACTS_DIR / "calibrated_voting_model.joblib"
THRESHOLD_PATH = ARTIFACTS_DIR / "calibrated_voting_threshold.joblib"


def load_model():
    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            f"Model file not found: {MODEL_PATH}"
        )

    if not THRESHOLD_PATH.exists():
        raise FileNotFoundError(
            f"Threshold file not found: {THRESHOLD_PATH}"
        )

    model = joblib.load(MODEL_PATH)
    threshold = joblib.load(THRESHOLD_PATH)

    return model, float(threshold)


model, threshold = load_model()








print("Model loaded successfully!")
print("Threshold loaded successfully!")
print("Threshold value:", threshold)



import pandas as pd


def predict_failure(
    machine_type: str,
    air_temperature: float,
    process_temperature: float,
    rotational_speed: int,
    torque: float,
    tool_wear: int,
):
    input_data = pd.DataFrame(
        [
            {
                "Type": machine_type,
                "Air temperature [K]": air_temperature,
                "Process temperature [K]": process_temperature,
                "Rotational speed [rpm]": rotational_speed,
                "Torque [Nm]": torque,
                "Tool wear [min]": tool_wear,
            }
        ]
    )

    # Keep features in the exact training order
    input_data = input_data[
        [
            "Type",
            "Air temperature [K]",
            "Process temperature [K]",
            "Rotational speed [rpm]",
            "Torque [Nm]",
            "Tool wear [min]",
        ]
    ]

    failure_probability = float(
        model.predict_proba(input_data)[0][1]
    )

    failure_prediction = int(
        failure_probability >= threshold
    )

    if failure_prediction == 1:
        message = "Machine failure predicted"
    else:
        message = "No machine failure predicted"

    return {
        "failure_prediction": failure_prediction,
        "failure_probability": failure_probability,
        "threshold": threshold,
        "message": message,
    }
