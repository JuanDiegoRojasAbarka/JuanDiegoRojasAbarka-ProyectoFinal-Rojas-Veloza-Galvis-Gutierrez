import numpy as np
import pandas as pd
from flask import Flask, request, render_template
from flask import redirect, url_for
import joblib

app = Flask(__name__)

grid_or_model = joblib.load("../Models/final_model.pkl")
scaler = joblib.load("../Models/scaler.pkl")
columns = joblib.load("../Models/columns.pkl")

model = grid_or_model.best_estimator_ if hasattr(grid_or_model, "best_estimator_") else grid_or_model

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST", "GET"])
def predict():
    if request.method == "GET":
        return redirect(url_for("home"))
    input_data = []
    for col in columns:
        value = float(request.form.get(col))
        input_data.append(value)

    df_new = pd.DataFrame([input_data], columns=columns)

    df_new_scaled = scaler.transform(df_new)

    pred_class = model.predict(df_new_scaled)[0]          
    pred_prob = model.predict_proba(df_new_scaled)[0, 1]  

    label = "ALTO RIESGO (Default)" if pred_class == 1 else "BAJO RIESGO (No Default)"

    return render_template(
        "index.html",
        prediction_text=f"Resultado: {label}",
        probability_text=f"Probabilidad de default: {pred_prob:.2%}"
    )


if __name__ == "__main__":
    app.run(debug=True)
