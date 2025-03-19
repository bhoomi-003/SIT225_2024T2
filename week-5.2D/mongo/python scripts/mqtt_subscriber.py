import paho.mqtt.client as mqtt

# MQTT Broker details
BROKER = "2d5ddc2ad5ef44fcbbe35b046a38cd6c.s1.eu.hivemq.cloud"
PORT = 8883  # MQTT Secure Port (TLS)
TOPIC = "arduino/gyroscope"
USERNAME = "bhoomi_narula"
PASSWORD = "Bhoominarula3"

# Callback when connected to MQTT broker
def on_connect(client, userdata, flags, rc, properties):
    if rc == 0:
        print("✅ Connected to MQTT Broker!")
        client.subscribe(TOPIC, qos=1)  # QoS 1 ensures message delivery
        print(f"📡 Subscribed to topic: {TOPIC}")
    else:
        print(f"❌ Connection failed with code {rc}")

# Callback when a message is received
def on_message(client, userdata, msg):
    print(f"📩 Received `{msg.payload.decode()}` from `{msg.topic}`")

# Create MQTT client instance
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

# Enable TLS and set authentication
client.tls_set()
client.username_pw_set(USERNAME, PASSWORD)

# Assign callback functions
client.on_connect = on_connect
client.on_message = on_message

# Connect to the broker
try:
    client.connect(BROKER, PORT, 60)
    print("🔌 Connecting...")
except Exception as e:
    print(f"❌ Connection failed: {e}")
    exit(1)

# Keep listening for messages
client.loop_forever()
