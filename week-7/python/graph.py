import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file into a DataFrame
df = pd.read_csv("data.csv")

# Convert 'timestamp' column to datetime format (if not already in correct format)
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Create a figure with two subplots
fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(10, 10), sharex=True)

# Plot Temperature over Time
axes[0].plot(df["timestamp"], df["temperature"], label="Temperature (°C)", color="red")
axes[0].set_ylabel("Temperature (°C)")
axes[0].set_title("Temperature Readings Over Time")
axes[0].legend()
axes[0].grid(True)

# Plot Humidity over Time
axes[1].plot(df["timestamp"], df["humidity"], label="Humidity (%)", color="blue")
axes[1].set_xlabel("Timestamp")
axes[1].set_ylabel("Humidity (%)")
axes[1].set_title("Humidity Readings Over Time")
axes[1].legend()
axes[1].grid(True)

# Rotate timestamps for better visibility
plt.xticks(rotation=45)

# Show the plots
plt.tight_layout()
plt.show()

# Plot Temperature and Humidity over Time together
plt.figure(figsize=(10, 5))
plt.plot(df["timestamp"], df["temperature"], label="Temperature (°C)", color="red")
plt.plot(df["timestamp"], df["humidity"], label="Humidity (%)", color="blue")
plt.xlabel("Timestamp")
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.title("Temperature and Humidity Over Time")
plt.show()

# Calculate average temperature and humidity
avg_temp = df["temperature"].mean()
avg_humidity = df["humidity"].mean()
print(f"Average Temperature: {avg_temp:.2f}°C")
print(f"Average Humidity: {avg_humidity:.2f}%")

# Average Temperature: 26.65°C
# Average Humidity: 61.02%

# Calculate minimum and maximum temperature and humidity
min_temp = df["temperature"].min()
max_temp = df["temperature"].max()
min_humidity = df["humidity"].min()
max_humidity = df["humidity"].max()

print(f"Min Temperature: {min_temp:.2f}°C")
print(f"Max Temperature: {max_temp:.2f}°C")
print(f"Min Humidity: {min_humidity:.2f}%")
print(f"Max Humidity: {max_humidity:.2f}%")

# Min Temperature: 26.10°C
# Max Temperature: 27.20°C
# Min Humidity: 58.40%
# Max Humidity: 62.40%