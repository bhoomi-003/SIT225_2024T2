import pymongo
import pandas as pd

# MongoDB Atlas Connection URI
client = pymongo.MongoClient("mongodb+srv://bhoomi_narula:Bhoominarula3@5-2d-sit225.3oki7.mongodb.net/?retryWrites=true&w=majority&appName=5-2D-SIT225")
db = client["SIT225-5-2D"]
collection = db["arduino/gyroscope"]

# Fetch all documents
data = list(collection.find({}, {"_id": 0}))  # Exclude _id

# Convert to DataFrame
df = pd.DataFrame(data)

# Save as CSV
df.to_csv("gyroscope_data.csv", index=False)

print("Data exported successfully!")
