import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load your CSV file
df = pd.read_csv("data.csv")

# Find min and max temperature values
min_temp = df["temperature"].min()
max_temp = df["temperature"].max()

# Generate 100 equally spaced temperature values between min and max
test_temperatures = np.linspace(min_temp, max_temp, 100).reshape(-1, 1)

# Create and train the linear regression model (predicting humidity from temperature)
model = LinearRegression()
X = df["temperature"].values.reshape(-1, 1)  # Independent variable (temperature)
y = df["humidity"].values  # Dependent variable (humidity)

model.fit(X, y)  # Train the model

# Predict humidity for the 100 test temperature values
predicted_humidity = model.predict(test_temperatures)

# Plot temperature vs humidity (Actual and Predicted)
plt.figure(figsize=(10, 5))
plt.scatter(df["temperature"], df["humidity"], label="Actual Data", marker="o", color="blue")
plt.plot(test_temperatures, predicted_humidity, label="Predicted Humidity", color="red")
plt.xlabel("Temperature (°C)")
plt.ylabel("Humidity (%)")
plt.legend()
plt.title("Humidity Prediction Based on Temperature")
plt.grid(True)
plt.show()