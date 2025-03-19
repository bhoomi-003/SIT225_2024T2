import paho.mqtt.client as mqtt
import requests
import json
from datetime import datetime
import ssl

# CouchDB Configuration
COUCHDB_URL = "http://127.0.0.1:5984"
COUCHDB_USER = "Bhoomi"
COUCHDB_PASSWORD = "Bhoominarula3"
DB_NAME = "sit225-5-2d"

# Use Basic Authentication
COUCHDB_AUTH = (COUCHDB_USER, COUCHDB_PASSWORD)

# Ensure Database Exists
db_response = requests.put(f"{COUCHDB_URL}/{DB_NAME}", auth=COUCHDB_AUTH)
if db_response.status_code == 401:
    print("❌ ERROR: Unauthorized! Check CouchDB credentials.")
    exit()
elif db_response.status_code == 201:
    print("✅ Database created successfully.")
elif db_response.status_code == 412:
    print("✅ Database already exists.")

# MQTT Configuration
MQTT_BROKER = "2d5ddc2ad5ef44fcbbe35b046a38cd6c.s1.eu.hivemq.cloud"
MQTT_PORT = 8883  # Secure MQTT port
MQTT_TOPIC = "arduino/gyroscope"
MQTT_USERNAME = "bhoomi_narula"  # Change this
MQTT_PASSWORD = "Bhoominarula3"  # Change this

# Callback when a message is received
def on_message(client, userdata, msg):
    try:
        payload = msg.payload.decode("utf-8")
        data = json.loads(payload)

        # Create document for CouchDB
        document = {
            "timestamp": datetime.now().isoformat(),
            "x": data.get("x"),
            "y": data.get("y"),
            "z": data.get("z"),
        }

        # Store in CouchDB
        response = requests.post(f"{COUCHDB_URL}/{DB_NAME}", json=document, auth=COUCHDB_AUTH)

        if response.status_code == 201:
            print("✅ Data stored successfully:", document)
        else:
            print("❌ Failed to store data:", response.status_code, response.json())

    except Exception as e:
        print("❌ Error processing MQTT message:", e)

# Setup MQTT Client
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)  # Set credentials for HiveMQ
client.tls_set(cert_reqs=ssl.CERT_NONE)  # Use TLS encryption
client.on_message = on_message

try:
    print("🔗 Connecting to MQTT broker...")
    client.connect(MQTT_BROKER, MQTT_PORT, keepalive=120)
    print("✅ Connected to MQTT broker.")

    client.subscribe(MQTT_TOPIC)
    print(f"📡 Subscribed to topic: {MQTT_TOPIC}")

    client.loop_forever()

except Exception as e:
    print("❌ MQTT Connection Error:", e)
