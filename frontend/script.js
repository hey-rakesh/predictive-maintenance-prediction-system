
const form = document.getElementById("prediction-form");
const predictButton = document.getElementById("predict-button");

const resultSection = document.getElementById("result");
const predictionMessage = document.getElementById("prediction-message");
const failureProbability = document.getElementById("failure-probability");
const thresholdValue = document.getElementById("threshold-value");
const errorMessage = document.getElementById("error-message");


form.addEventListener("submit", async (event) => {
    event.preventDefault();

    resultSection.classList.add("hidden");
    errorMessage.classList.add("hidden");

    const payload = {
        Type: document.getElementById("machine-type").value,
        air_temperature: Number(document.getElementById("air-temperature").value),
        process_temperature: Number(document.getElementById("process-temperature").value),
        rotational_speed: Number(document.getElementById("rotational-speed").value),
        torque: Number(document.getElementById("torque").value),
        tool_wear: Number(document.getElementById("tool-wear").value)
    };

    predictButton.disabled = true;
    predictButton.textContent = "Analyzing machine...";

    try {
        const response = await fetch("http://127.0.0.1:8000/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(payload)
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(
                data.detail
                    ? JSON.stringify(data.detail)
                    : "Prediction request failed."
            );
        }

        predictionMessage.textContent = data.message;
        failureProbability.textContent =
            `${(data.failure_probability * 100).toFixed(2)}%`;

        thresholdValue.textContent =
            `${(data.threshold * 100).toFixed(2)}%`;

        resultSection.classList.remove("hidden");

    } catch (error) {
        errorMessage.textContent =
            `Could not get prediction: ${error.message}`;

        errorMessage.classList.remove("hidden");

    } finally {
        predictButton.disabled = false;
        predictButton.textContent = "Predict Machine Failure";
    }
});
