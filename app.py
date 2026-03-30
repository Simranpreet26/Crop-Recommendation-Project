from flask import Flask, render_template, request
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

app = Flask(__name__)

data = pd.read_excel("Crop Recommendation Dataset.xlsx")

X = data[['Temperature', 'Humidity', 'pH', 'Rainfall']]
y = data['Label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/predict', methods=['POST'])
def predict():

    try:
        city = request.form['city']

        temp = float(request.form['temperature'])
        humidity = float(request.form['humidity'])
        ph = float(request.form['ph'])
        rainfall = float(request.form['rainfall'])

        # ✅ city-based adjustment (FIXED PLACE)
        if city == "punjab":
            temp += 2
            humidity += 5
        elif city == "delhi":
            temp += 3
            humidity -= 2
        elif city == "mumbai":
            temp += 1
            humidity += 10

        input_data = np.array([[temp, humidity, ph, rainfall]])
        result = model.predict(input_data)[0]

        result = str(result).strip().lower()

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

        image = f"https://source.unsplash.com/300x200/?{result}"

        return render_template(
            "index.html",
            prediction=result.title(),
            emoji=emoji,
            image=image,
            acc=round(accuracy * 100, 2)
        )

    except Exception as e:
        return render_template("index.html", error=str(e))


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
