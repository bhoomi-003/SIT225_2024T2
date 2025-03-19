import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv("gyroscope_data.csv")

# Ensure proper column names (CSV might have spaces or unexpected names)
df.columns = [col.strip() for col in df.columns]

# Extract variables
timestamps = df['timestamp']
x_values = df['x']
y_values = df['y']
z_values = df['z']

# Plot X, Y, and Z separately
plt.figure(figsize=(12, 6))

plt.subplot(3, 1, 1)
plt.plot(timestamps, x_values, label="X-axis", color='r')
plt.xlabel("Timestamp")
plt.ylabel("X Value")
plt.title("Gyroscope X-axis Data")
plt.legend()

plt.subplot(3, 1, 2)
plt.plot(timestamps, y_values, label="Y-axis", color='g')
plt.xlabel("Timestamp")
plt.ylabel("Y Value")
plt.title("Gyroscope Y-axis Data")
plt.legend()

plt.subplot(3, 1, 3)
plt.plot(timestamps, z_values, label="Z-axis", color='b')
plt.xlabel("Timestamp")
plt.ylabel("Z Value")
plt.title("Gyroscope Z-axis Data")
plt.legend()

plt.tight_layout()
plt.show()

# Plot all three in a single graph
plt.figure(figsize=(12, 5))
plt.plot(timestamps, x_values, label="X-axis", color='r')
plt.plot(timestamps, y_values, label="Y-axis", color='g')
plt.plot(timestamps, z_values, label="Z-axis", color='b')
plt.xlabel("Timestamp")
plt.ylabel("Gyroscope Values")
plt.title("Gyroscope Data (X, Y, Z)")
plt.legend()
plt.show()
