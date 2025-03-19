#include <WiFiNINA.h>
#include <PubSubClient.h>
#include <Arduino_LSM6DS3.h>

// WiFi credentials
const char* ssid = "bhoomi";
const char* password = "bhoominarula";

// MQTT Broker settings (HiveMQ Cloud)
const char* mqttServer = "2d5ddc2ad5ef44fcbbe35b046a38cd6c.s1.eu.hivemq.cloud";
const int mqttPort = 8883;  // Secure TLS port
const char* mqttUser = "bhoomi_narula";
const char* mqttPassword = "Bhoominarula3";

// MQTT Topic
const char* topic = "arduino/gyroscope";

// WiFi & MQTT Clients
WiFiSSLClient wifiClient; 
PubSubClient client(wifiClient);

// Function Prototypes
void connectWiFi();
void connectMQTT();

void setup() {
    Serial.begin(115200);
    while (!Serial);
    
    // Initialize IMU sensor
    if (!IMU.begin()) {
        Serial.println("Failed to initialize IMU!");
        while (1);
    }
    
    // Connect to WiFi
    connectWiFi();

    // Configure MQTT Server
    client.setServer(mqttServer, mqttPort);

    // Connect to MQTT Broker
    connectMQTT();
}

void loop() {
    if (!client.connected()) {
        connectMQTT();
    }

    client.loop(); // Maintain MQTT connection

    // Read Gyroscope data
    float x, y, z;
    if (IMU.gyroscopeAvailable()) {
        IMU.readGyroscope(x, y, z);
        
        // Corrected JSON message format
        char message[100];
        snprintf(message, sizeof(message), "{\"x\": %.2f, \"y\": %.2f, \"z\": %.2f}", x, y, z);

        // Publish data to MQTT topic
        client.publish(topic, message);
        Serial.println("Published: " + String(message));
    }

    delay(500); // Adjust delay as needed
}

// Function to connect WiFi
void connectWiFi() {
    Serial.print("Connecting to WiFi...");
    while (WiFi.begin(ssid, password) != WL_CONNECTED) {
        Serial.print(".");
        delay(1000);
    }
    Serial.println("Connected to WiFi!");
}

// Function to connect MQTT
void connectMQTT() {
    Serial.print("Connecting to MQTT...");
    while (!client.connected()) {
        if (client.connect("ArduinoClient", mqttUser, mqttPassword)) {
            Serial.println("Connected to MQTT!");
        } else {
            Serial.print("Failed with state: ");
            Serial.println(client.state());  // Show error code
            delay(5000);
        }
    }
}
