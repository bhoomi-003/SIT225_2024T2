
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# 1. Read the CSV (with robust error handling)
filename = "data.csv"  # Or your actual file name
try:
    df = pd.read_csv(filename)
except FileNotFoundError:
    print(f"Error: File '{filename}' not found. Check the path.")
    exit()
except Exception as e:
    print(f"Error reading CSV: {e}")
    print("Check if the file is open in another program or if the encoding is incorrect.")
    exit()

# 2. Data Cleaning and Conversion
# Convert Timestamp to datetime, handling errors
df['Timestamp'] = pd.to_datetime(df['Timestamp'], format='%Y%m%d%H%M%S', errors='coerce')

# Drop rows with invalid timestamps or NaN values
df.dropna(inplace=True)

# 3. Set Timestamp as Index
df = df.set_index('Timestamp')

# 4. Check if DataFrame is empty after cleaning
if df.empty:
    print("Error: DataFrame is empty after cleaning. Check your data and cleaning steps.")
    exit()

# 5. Plotting with correct date and time formatting
fig, ax = plt.subplots(figsize=(12, 6))

# Plot Temperature
ax.plot(df.index, df['Temperature'], label='Temperature (°C)', color='tab:red', marker='.', linestyle='-')  # Added markers

# Plot Humidity
ax.plot(df.index, df['Humidity'], label='Humidity (%)', color='tab:blue', marker='.', linestyle='-')  # Added markers

# Labels, Title, Legend
ax.set_xlabel('Time', fontsize=12)
ax.set_ylabel('Values', fontsize=12)
ax.set_title('Temperature and Humidity over Time', fontsize=14)
ax.legend(fontsize=10)

# Improved x-axis date and time formatting (THE FIX!)
ax.xaxis.set_major_locator(mdates.MinuteLocator(interval=5))  # Adjust interval as needed (e.g., 1 for each minute)
ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))  # Format as HH:MM:SS (include seconds)
plt.xticks(rotation=45, ha='right', fontsize=10)

plt.tight_layout()
plt.show()

# 6. Print Data Types and Head (for verification)
print(df.dtypes)
print(df.head())

# 7. Data Analysis and Comments
print("\nAnalysis and Comments:")
# ... (Your observations and interpretations)




























































# import serial
# import random
# import time 
# baud_rate = 9600

# s = serial.Serial('COM11',baud_rate,timeout=5 )
# time.sleep(1)

# while True :
#     no_of_blink = random.randint(1,10)
#     s.write(bytes(str(no_of_blink),'utf-8'))
#     print(f"sent >>> {no_of_blink} blinks")
#     time.sleep(1)

#     reply= s.readline().decode('utf-8').strip()
#     if reply.isdigit():
#         delay = int(reply)
#         print(f"received <<< {delay} seconds")
#         print (f"sleep for {delay} seconds")
#         time.sleep(delay)
#         print ("-------------------------------------")








# import serial
# s = serial.Serial('COM10', 9600, timeout=5)  # Adjust COM port
# while True:
#     print(s.readline().decode('utf-8').strip())  # Print what Arduino sends

