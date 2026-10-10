
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200


def test_valid_prediction():
    payload = {
        "Type": "M",
        "air_temperature": 298.1,
        "process_temperature": 308.6,
        "rotational_speed": 1500,
        "torque": 40.0,
        "tool_wear": 100,
    }

    response = client.post("/predict", json=payload)

    assert response.status_code == 200

    data = response.json()
    assert data["failure_prediction"] in [0, 1]
    assert 0 <= data["failure_probability"] <= 1
    assert 0 <= data["threshold"] <= 1


def test_invalid_machine_type():
    payload = {
        "Type": "X",
        "air_temperature": 298.1,
        "process_temperature": 308.6,
        "rotational_speed": 1500,
        "torque": 40.0,
        "tool_wear": 100,
    }

    response = client.post("/predict", json=payload)
    assert response.status_code == 422


def test_missing_field():
    payload = {
        "Type": "M",
        "air_temperature": 298.1,
        "process_temperature": 308.6,
        "rotational_speed": 1500,
        "tool_wear": 100,
    }

    response = client.post("/predict", json=payload)
    assert response.status_code == 422
