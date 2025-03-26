from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file into a DataFrame
df = pd.read_csv("data.csv")


# Convert timestamp to numerical values (e.g., seconds since start)
df["timestamp_num"] = np.arange(len(df))

# Create and train the model
model = LinearRegression()
X = df["timestamp_num"].values.reshape(-1, 1)  # Independent variable (reshaped for sklearn)
y = df["humidity"].values  # Dependent variable
model.fit(X, y)

# Predict values
df["humidity_pred"] = model.predict(X)

# Plot actual vs predicted
plt.figure(figsize=(10, 5))
plt.scatter(df["timestamp"], df["humidity"], label="Actual Humidity", marker="s")
plt.plot(df["timestamp"], df["humidity_pred"], label="Predicted Humidity (Regression)", color="red")
plt.xlabel("Timestamp")
plt.ylabel("Humidity (%)")
plt.legend()
plt.xticks(rotation=45)
plt.title("Humidity Over Time with Linear Regression")
plt.grid(True)
plt.show()