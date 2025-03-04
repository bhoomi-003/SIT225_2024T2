import serial

try:
    ser = serial.Serial('COM4', 9600, timeout=1)
    print("Port opened successfully!")
except Exception as e:
    print(f"Error opening port: {e}")
