from flask import Flask, render_template, request
import joblib
import numpy as np
import os
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
app = Flask(__name__)

# load model
data = pd.read_excel("Crop Recommendation Dataset.xlsx")
print(data.columns)
X = data[['temperature', 'humidity', 'ph', 'rainfall']]
y = data['label']

model = RandomForestClassifier()
model.fit(X, y)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        temp = float(request.form['temperature'])
        humidity = float(request.form['humidity'])
        ph = float(request.form['ph'])
        rainfall = float(request.form['rainfall'])

        input_data = np.array([[temp, humidity, ph, rainfall]])

        if model is None:
            result = "Model not loaded"
        else:
            result = model.predict(input_data)[0]

        return render_template("index.html", prediction=result)

    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
