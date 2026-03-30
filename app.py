from flask import Flask, render_template, request
import joblib
import numpy as np
import os

app = Flask(__name__)

# load model
model = None

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    temp = float(request.form['temperature'])
    humidity = float(request.form['humidity'])
    ph = float(request.form['ph'])
    rainfall = float(request.form['rainfall'])

    input_data = np.array([[temp, humidity, ph, rainfall]])

    if model is None:
        prediction = ["Model not loaded"]
    else:
        prediction = model.predict(input_data)

    return render_template("index.html", prediction=prediction[0])


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
