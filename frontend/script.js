
const form = document.getElementById("prediction-form");
const predictButton = document.getElementById("predict-button");

const resultSection = document.getElementById("result");
const predictionMessage = document.getElementById("prediction-message");
const failureProbability = document.getElementById("failure-probability");
const thresholdValue = document.getElementById("threshold-value");
const errorMessage = document.getElementById("error-message");


function showError(message) {
    errorMessage.textContent = message;
    errorMessage.classList.remove("hidden");
    resultSection.classList.add("hidden");
}


function hideError() {
    errorMessage.textContent = "";
    errorMessage.classList.add("hidden");
}


form.addEventListener("submit", async (event) => {
    event.preventDefault();

    hideError();
    resultSection.classList.add("hidden");

    const input = {
        Type: document.getElementById("machine-type").value,
        air_temperature: Number(
            document.getElementById("air-temperature").value
        ),
        process_temperature: Number(
            document.getElementById("process-temperature").value
        ),
        rotational_speed: Number(
            document.getElementById("rotational-speed").value
        ),
        torque: Number(
            document.getElementById("torque").value
        ),
        tool_wear: Number(
            document.getElementById("tool-wear").value
        )
    };

    predictButton.disabled = true;
    predictButton.textContent = "Analyzing Machine...";

    try {
        const response = await fetch("/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(input)
        });

        const data = await response.json();

        if (!response.ok) {
            const detail = data.detail;

            const message = Array.isArray(detail)
                ? detail.map(item => item.msg).join(", ")
                : typeof detail === "string"
                    ? detail
                    : "Prediction request failed.";

            throw new Error(message);
        }

        const probability = Number(data.failure_probability);
        const threshold = Number(data.threshold);

        if (
            !Number.isFinite(probability) ||
            !Number.isFinite(threshold)
        ) {
            throw new Error("API returned an invalid probability or threshold.");
        }

        predictionMessage.textContent = data.message;
        failureProbability.textContent =
            `${(probability * 100).toFixed(2)}%`;

        thresholdValue.textContent =
            `${(threshold * 100).toFixed(2)}%`;

        resultSection.classList.remove("hidden");

    } catch (error) {
        console.error("Prediction error:", error);

        showError(
            error.message ||
            "Unable to connect to the prediction API. Please try again."
        );

    } finally {
        predictButton.disabled = false;
        predictButton.textContent = "Predict Machine Failure";
    }
});
