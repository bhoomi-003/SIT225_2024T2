import pandas as pd
import os
import matplotlib.pyplot as plt

# Folder containing the accelerometer data CSV file
data_folder = "D:\SEM2\SIT225\Task 8.3D\python\data"

# Iterate through the files in the data folder
for filename in os.listdir(data_folder):
    if filename.endswith('.csv'):
        # Load the accelerometer data
        data_path = os.path.join(data_folder, filename)
        data = pd.read_csv(data_path)

        # Check if the CSV contains accelerometer data (x,y,z)
        if 'x' in data.columns and 'y' in data.columns and 'z' in data.columns:
            # Plot the accelerometer data
            plt.figure(figsize=(10, 6))
            plt.plot(data['x'], label='X-axis', color='red')
            plt.plot(data['y'], label='Y-axis', color='green')
            plt.plot(data['z'], label='Z-axis', color='blue')

            # Title and Lables
            plt.title(f'Accelerometer Data from {filename}')
            plt.xlabel('Time (s)')
            plt.ylabel('Acceleration (g)')
            plt.legend()

            # Show the plot
            plt.show()