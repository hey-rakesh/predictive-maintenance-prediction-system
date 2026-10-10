# 🏭 Predictive Maintenance Prediction System

An end-to-end Machine Learning application that predicts potential industrial machine failures using sensor data and a configurable probability threshold. The project demonstrates how machine learning can support proactive maintenance and reduce unexpected equipment downtime.

## 🚀 Live Demo

**🌐 Live Application:** [Predictive Maintenance Prediction System](https://predictive-maintenance-prediction-system-gd0u.onrender.com/)

Open the live application to enter machine sensor readings and view the prediction result.

## ✨ Features

- **Machine Failure Prediction:** Predicts whether a machine is likely to fail based on its operating conditions.
- **Failure Probability:** Displays the estimated probability of machine failure.
- **Threshold-Based Classification:** Uses a tuned decision threshold to convert predicted probabilities into failure/no-failure classifications.
- **Interactive Web Interface:** Provides a simple interface for entering sensor values and viewing results.
- **REST API:** Uses FastAPI to serve machine learning predictions.
- **Input Validation:** Uses Pydantic to validate incoming prediction data.
- **Cloud Deployment:** Deployed on Render for online access.

## 🧠 Machine Learning Workflow

1. Load and explore the predictive maintenance dataset.
2. Perform data cleaning and preprocessing.
3. Select relevant machine sensor features.
4. Train and evaluate classification models.
5. Tune model hyperparameters and evaluate performance.
6. Tune the decision threshold for failure classification.
7. Save the trained model and load it in the backend.
8. Serve predictions through FastAPI.
9. Deploy the application on Render.

## 📊 Input Features

The system uses machine operating parameters such as:

| Feature | Description |
|---|---|
| Air temperature [K] | Temperature of the surrounding air in Kelvin |
| Process temperature [K] | Operating process temperature in Kelvin |
| Rotational speed [rpm] | Machine rotational speed in revolutions per minute |
| Torque [Nm] | Rotational force produced by the machine |
| Tool wear [min] | Accumulated tool wear time in minutes |

## 🎯 Prediction Output

The application returns the following information:

- **Failure Prediction:** `0` for no predicted failure or `1` for predicted failure.
- **Failure Probability:** Estimated probability of machine failure.
- **Decision Threshold:** The probability cutoff used for classification.
- **Prediction Message:** A readable explanation of the predicted result.

### Example Response

```json
{
  "failure_prediction": 0,
  "failure_probability": 0.04846,
  "threshold": 0.37,
  "message": "No machine failure predicted"
}
```

In this example, the estimated failure probability is approximately **4.85%**, which is below the decision threshold of **37%**. Therefore, the model predicts no machine failure.

*Note: This is an illustrative response based on a project prediction example.*

## 🛠️ Technology Stack

**Machine Learning & Data Processing**
- Python
- Pandas
- NumPy
- Scikit-learn

**Backend & API**
- FastAPI
- Pydantic
- Uvicorn

**Deployment**
- Render

## ⚙️ Run Locally

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd <YOUR_PROJECT_FOLDER>
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the FastAPI server

```bash
uvicorn main:app --reload
```

Replace `main:app` with the correct Python module and FastAPI application variable if your project uses a different entry point.

### 5. Open the application

- Live application: [Render Deployment](https://predictive-maintenance-prediction-system-gd0u.onrender.com/)
- Local API: `http://127.0.0.1:8000`
- Interactive API documentation: `http://127.0.0.1:8000/docs`

The API documentation URL assumes the default FastAPI documentation route is enabled.

## 🔮 Future Improvements

- Predict the specific reason for machine failure, such as tool wear, heat dissipation, power failure, or overstrain.
- Add feature-level explanations for individual predictions.
- Integrate real-time IoT sensor data.
- Add historical prediction tracking and maintenance alerts.
- Improve model monitoring and evaluation on new data.

## 🎓 Learning Outcomes

This project demonstrates practical experience with:

- Classification for imbalanced datasets.
- Machine learning model evaluation.
- Hyperparameter and decision-threshold tuning.
- Probability-based prediction.
- REST API development using FastAPI.
- Request validation using Pydantic.
- Deployment of an ML application to the cloud.

## 👨‍💻 Author

**Rakesh Verma**

- GitHub: [hey-rakesh](https://github.com/hey-rakesh)
- Live Project: [Predictive Maintenance Prediction System](https://predictive-maintenance-prediction-system-gd0u.onrender.com/)

---

⭐ If you find this project useful, consider giving the repository a star.
