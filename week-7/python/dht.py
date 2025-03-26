import serial
import csv
import time
import re

# Serial Port Configuration (Change according to your system)
SERIAL_PORT = "COM4"  
BAUD_RATE = 9600
OUTPUT_FILE = "data.csv"

# Open serial connection
ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
time.sleep(2)  # Allow time for connection

# Open CSV file and write header
with open(OUTPUT_FILE, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["timestamp", "temperature", "humidity"])  # Column headers

    try:
        print("Collecting data... Press Ctrl+C to stop.")
        while True:
            line = ser.readline().decode("utf-8").strip()
            if line:
                print(line)
                # Extract temperature and humidity using regex
                match = re.search(r"Humidity:\s*([\d.]+)%,\s*Temp:\s*([\d.]+)\s*Celsius", line)
                if match:
                    humidity = float(match.group(1))
                    temperature = float(match.group(2))
                    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")  # Get current timestamp
                    writer.writerow([timestamp, temperature, humidity])
    except KeyboardInterrupt:
        print("Data collection stopped.")
    finally:
        ser.close()
