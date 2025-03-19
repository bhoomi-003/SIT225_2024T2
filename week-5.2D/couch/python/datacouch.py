import requests
import csv

# CouchDB Configuration
COUCHDB_URL = "http://127.0.0.1:5984"
COUCHDB_USER = "Bhoomi"
COUCHDB_PASSWORD = "Bhoominarula3"
DB_NAME = "sit225-5-2d"

# Fetch data from CouchDB with authentication
response = requests.get(f"{COUCHDB_URL}/{DB_NAME}/_all_docs?include_docs=true", auth=(COUCHDB_USER, COUCHDB_PASSWORD))

if response.status_code == 200:
    data = response.json()
    
    # Open CSV file to store data
    with open("gyroscope_data.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["timestamp", "x", "y", "z"])  # Headers
        
        for row in data["rows"]:
            doc = row["doc"]
            writer.writerow([doc.get("timestamp", ""), doc.get("x", ""), doc.get("y", ""), doc.get("z", "")])

    print("✅ CSV file saved successfully!")
else:
    print("❌ Failed to fetch data:", response.status_code, response.json())
