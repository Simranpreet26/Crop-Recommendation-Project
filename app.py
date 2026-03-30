from flask import Flask, render_template, request
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier

app = Flask(__name__)

# Load dataset
data = pd.read_excel("Crop Recommendation Dataset.xlsx")

# Correct column names
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
        result = model.predict(input_data)[0]

        # clean result
        result = str(result).strip().lower()

        # emoji logic
        emoji = "🌱"

        if "rice" in result:
            emoji = "🌾"
        elif "wheat" in result:
            emoji = "🌾"
        elif "banana" in result:
            emoji = "🍌"
        elif "cotton" in result:
            emoji = "🧵"
        elif "maize" in result:
            emoji = "🌽"
        elif "apple" in result:
            emoji = "🍎"
        elif "kidneybeans" in result:
            emoji = "🫘"
        elif "mango" in result:
            emoji = "🥭"

        return render_template("index.html", prediction=result.title(), emoji=emoji)

    except:
        return render_template("index.html", prediction="Invalid Input", emoji="⚠️")

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
