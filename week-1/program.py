import serial
import random
import time

baud_rate = 9600   # baud rate of arduino

s = serial.Serial('COM10', baud_rate, timeout=1)  # open serial port

time.sleep(2)  # wait for arduino to reset

while True :
    random_blink = random.randint(1,10)
    s.write(bytes(str(random_blink),'utf-8'))
    print(f"sent >>> {random_blink} blinks")
    time.sleep(1)

    reply= s.readline().decode('utf-8').strip()
    if reply.isdigit():
        delay = int(reply)
        print(f"received <<< {delay} seconds")
        print (f"sleep for {delay} seconds")
        time.sleep(delay)
        print ("-----------------------------------")