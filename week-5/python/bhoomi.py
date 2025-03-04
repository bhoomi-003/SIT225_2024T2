import serial
import time
import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate(r"D:\SEM2\SIT225\\Task 5.1\python\serviceAccountKeys.json")  
firebase_admin.initialize_app(cred, {"databaseURL": "https://bhoomi3-a4e88-default-rtdb.asia-southeast1.firebasedatabase.com/"})  


ref = db.reference("gyroscope_data")

ser = serial.Serial("COM4", 9600, timeout=1)  
time.sleep(2)  

csv_file_path = "D:\\SEM2\\SIT225\\Task 5.1\\python\\bhoomi.csv"
with open(csv_file_path, "w") as file:
    file.write("timestamp,x,y,z\n")  


start_time = time.time()
duration = 1800  

while time.time() - start_time < duration:
    try:
        line = ser.readline().decode("utf-8").strip() 
        if line:
            values = line.split(",") 

            if len(values) == 3: 
                x, y, z = map(float, values)  
                timestamp = time.strftime("%Y-%m-%d %H:%M:%S")  

                data = {"timestamp": timestamp, "x": x, "y": y, "z": z}

                ref.push(data)

                with open(csv_file_path, "a") as file: 
                    file.write(f"{timestamp},{x},{y},{z}\n")

                print(f"{timestamp}, {x}, {y}, {z}")

    except Exception as e:
        print("Error:", e)

ser.close()
print(f" Data collection complete! CSV saved at: {csv_file_path}")