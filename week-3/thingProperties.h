// Code generated by Arduino IoT Cloud, DO NOT EDIT.

#include <ArduinoIoTCloud.h>
#include <Arduino_ConnectionHandler.h>

const char SSID[]     = "BHOOMI 6845";    // Network SSID (name)
const char PASS[]     = "bhoominarula";    // Network password (use for WPA, or use as key for WEP)

void onUltrasonicChange();

float ultrasonic;

void initProperties(){

  ArduinoCloud.addProperty(ultrasonic, READWRITE, ON_CHANGE, onUltrasonicChange);



}

WiFiConnectionHandler ArduinoIoTPreferredConnection(SSID, PASS);
