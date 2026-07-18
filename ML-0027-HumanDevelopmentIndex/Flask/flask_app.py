
from flask import Flask, render_template, request
import pickle
import numpy as np


# Load trained model
import os

model_path = os.path.join(os.path.dirname(__file__), "hdi_model.pkl")

with open(model_path, "rb") as file:
    model = pickle.load(file)


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    life_expectancy = float(request.form["life_expectancy"])
    expected_schooling = float(request.form["expected_schooling"])
    mean_schooling = float(request.form["mean_schooling"])
    gni = float(request.form["gni"])

    input_data = np.array([
        life_expectancy,
        expected_schooling,
        mean_schooling,
        gni
    ]).reshape(1, -1)


    prediction = model.predict(input_data)


    return render_template(
        "index.html",
        prediction_text=f"Predicted HDI Score: {prediction[0]:.3f}"
    )


if __name__ == "__main__":
    app.run(debug=True)