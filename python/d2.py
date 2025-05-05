import os
import csv
import cv2

# Folder containg your CSV and image files
data_folder = "D:\SEM2\SIT225\Task 8.3D\python\data" 

# CSV file name to store annotated data
annotation_file = "annotated_data.csv"

# Open the CSV file to write annotation
with open(annotation_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['filename', 'activity'])  # Header for the CSV file

    # Iterate through your data folder to create annotations
    for filename in os.listdir(data_folder):
        if filename.endswith('.csv'):
            # Get the corresponding image file (same name as CSV)
            image_filename = filename.replace('.csv', '.jpg')
            image_path = os.path.join(data_folder, image_filename)

            print(f"Checking image file: {image_filename} at path {image_path}")

            # Initialize activity label with a default value
            activity_label = 0 # Default to no activity

            # Check if the image exists before attempting to load it
            if os.path.exists(image_path):
                # Read and display the image
                img = cv2.imread(image_path)
                cv2.imshow('Image', img)
                key = cv2.waitKey(0) & 0xFF

                # Assign activity label based on user input
                if key == ord('1'):
                    activity_label = 1  # Activity 1 (Waving)
                elif key == ord('2'):
                    activity_label = 2  # Activity 2 (Shaking)
                elif key == ord('0'):
                    activity_label = 0  # No activity (default)
                
            else:
                print(f"Warning: The image '{image_filename}' does not exist at {image_path}. Skipping annotation.")

            # Write the filename and activity label to the annotation file
            writer.writerow([filename, activity_label])

cv2.destroyAllWindows() 