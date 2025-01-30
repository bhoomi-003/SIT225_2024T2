#define LED_PIN 13  // Built-in LED on most Arduino boards

void setup() {
  Serial.begin(9600);  // Initialize serial communication
  pinMode(LED_PIN, OUTPUT);  // Set LED_PIN as output
}

void loop() {
  if (Serial.available() > 0) {
    int blinkCount = Serial.parseInt();  // Read number of blinks from serial

    // Blink the LED specified number of times
    for (int i = 0; i < blinkCount; i++) {
      digitalWrite(LED_PIN, HIGH);  // Turn LED on
      delay(500);                   // Wait for 500ms
      digitalWrite(LED_PIN, LOW);   // Turn LED off
      delay(500);                   // Wait for 500ms
    }

    // Send a delay time back to Python
    int delayTime = random(1, 5);  // Random delay time between 1 and 5 seconds
    Serial.println(delayTime);      // Send delay time to Python
  }
}