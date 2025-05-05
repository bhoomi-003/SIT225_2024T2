import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Folder containing the accelerometer data CSV file
data_folder = "D:\SEM2\SIT225\Task 8.3D\python\data"

# Function to extract statistical features
def extract_features(data):
    # Extract features: mean, standard deviation, max, min for x, y, z
    features = {
        'mean_x': np.mean(data['x']),
        'mean_y': np.mean(data['y']),
        'mean_z': np.mean(data['z']),
        'std_x': np.std(data['x']),
        'std_y': np.std(data['y']),
        'std_z': np.std(data['z']),
        'max_x': np.max(data['x']),
        'max_y': np.max(data['y']),
        'max_z': np.max(data['z']),
        'min_x': np.min(data['x']),
        'min_y': np.min(data['y']),
        'min_z': np.min(data['z']),
    }
    return features

# Create a DataFrame to store all features
feature_data = []

# Iterate through the data folder and process each CSV file
for filename in os.listdir(data_folder):
    if filename.endswith('.csv'):
        # Load the accelerometer data
        data_path = os.path.join(data_folder, filename)
        data = pd.read_csv(data_path)

        # Extract statistical features
        features = extract_features(data)
        features['filename'] = filename
        feature_data.append(features)

# Convert the list of features to a DataFrame
feature_df = pd.DataFrame(feature_data)

# Show the extracted feature for each file
print(feature_df)

# You can also visualize the features to see if there's a pattern
feature_df.plot(kind='bar', x='filename', figsize=(12, 6))
plt.title('Statistical Features of Accelerometer Data')
plt.xlabel('Filename')
plt.ylabel('Feature Value')
plt.show()