from flask import Flask, render_template, request
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier

app = Flask(__name__)

# Load dataset
data = pd.read_excel("Crop Recommendation Dataset.xlsx")

# Correct column names (IMPORTANT)
X = data[['Temperature', 'Humidity', 'pH', 'Rainfall']]
y = data['Label']

# Train model
model = DecisionTreeClassifier()
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
        prediction = model.predict(input_data)

        return render_template("index.html", prediction=prediction[0])

    except:
        return render_template("index.html", prediction="Invalid Input")

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
