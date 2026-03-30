import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_excel("Crop Recommendation Dataset.xlsx")

print(data.head())

# graph 1: crop distribution
sns.countplot(x='Label', data=data)
plt.xticks(rotation=90)
plt.title("Crop Distribution")
plt.show()

# graph 2: rainfall vs temperature
sns.scatterplot(x='Rainfall', y='Temperature', hue='Label', data=data)
plt.title("Rainfall vs Temperature")
plt.show()
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# features (input)
X = data[['Temperature', 'Humidity', 'pH', 'Rainfall']]

# target (output)
y = data['Label']

# split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# prediction
pred = model.predict(X_test)

# accuracy
print("Accuracy:", accuracy_score(y_test, pred))

# =========================
# USER INPUT PREDICTION
# =========================

temp = float(input("Enter Temperature: "))
hum = float(input("Enter Humidity: "))
ph = float(input("Enter pH: "))
rain = float(input("Enter Rainfall: "))

result = model.predict([[temp, hum, ph, rain]])

print("Recommended Crop is:", result[0])

import joblib

joblib.dump(model, "model.pkl")

print("MODEL SAVED SUCCESSFULLY")
