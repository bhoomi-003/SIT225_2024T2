import paho.mqtt.client as mqtt

# MQTT Broker details
BROKER = "2d5ddc2ad5ef44fcbbe35b046a38cd6c.s1.eu.hivemq.cloud"
PORT = 8883  # Secure MQTT Port (TLS)
TOPIC = "arduino/gyroscope"
USERNAME = "bhoomi_narula"
PASSWORD = "Bhoominarula3"

# Create MQTT Client
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

# Enable TLS and set authentication
client.tls_set()
client.username_pw_set(USERNAME, PASSWORD)

# Connect to broker
try:
    client.connect(BROKER, PORT, 60)
    print("✅ Connected to MQTT Broker!")
except Exception as e:
    print(f"❌ Connection failed: {e}")
    exit(1)

# Create and publish message
message = '{1.23, -0.45, 0.67}'
result = client.publish(TOPIC, message, qos=1)  # QoS 1 for reliability

if result.rc == mqtt.MQTT_ERR_SUCCESS:
    print(f"📤 Message sent: {message}")
else:
    print("❌ Failed to send message")

# Disconnect
client.disconnect()
