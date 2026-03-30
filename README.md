# 🌱 Crop Recommendation System (ML Flask App)

## 📌 Project Name

Crop Recommendation System using Machine Learning (Decision Tree + Flask Web App)



## 🚀 Features

* Predict best crop based on soil and weather conditions
* Inputs: Temperature, Humidity, pH, Rainfall
* City-based environmental adjustment (Punjab, Delhi, Mumbai)
* Machine Learning model using Decision Tree Classifier
* Shows prediction with emoji support 🌾🍌🍎🌽
* Displays crop-related image dynamically
* Shows model accuracy score
* Simple and interactive web interface using Flask



## 🛠️ Tech Used

* Python 🐍
* Flask 🌐
* Pandas 📊
* NumPy 🔢
* Scikit-learn 🤖
* HTML / CSS (Frontend)
* Excel Dataset (.xlsx)



## 📊 Machine Learning Model

* Algorithm: Decision Tree Classifier
* Train-Test Split: 80/20
* Features Used:

  * Temperature
  * Humidity
  * pH
  * Rainfall



## 🖥️ How It Works

1. User enters environmental parameters
2. System adjusts values based on selected city
3. ML model predicts suitable crop
4. Result is displayed with emoji + image



## 📂 Project Structure

project/
│── app.py
│── Crop Recommendation Dataset.xlsx
│── templates/
│     └── index.html
│── static/
│     └── style.css
│     └── screenshot.png


##  ⭐ Future Improvements

* Add real-time weather API integration 🌦️
* Improve model accuracy with Random Forest / XGBoost
* Deploy on Render / Heroku
* Add map-based crop suggestion


