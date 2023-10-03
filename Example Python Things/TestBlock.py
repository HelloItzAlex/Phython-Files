from serial.tools import list_ports
import serial
import time
import csv


print("bruh")
ports = list_ports.comports()
for port in ports:
    print(port)

# Create CSV file
f = open("data.csv","w",newline='')
f.truncate()

# Open the serial com
serialCom = serial.Serial('COM19',115200)

# Toggle DTR to reset the Arduino
serialCom.setDTR(False)
time.sleep(1)
serialCom.flushInput()
serialCom.setDTR(True)

writer = csv.writer(f, delimiter=",")

# How many data points to record
kmax = 200
prev_byte = 0; 
for k in range(kmax):
    try:
        print("bruh1")
        s_bytes = serialCom.readline()
        decoded_bytes = s_bytes.decode("utf-8").strip('\r\n')
        decoded_bytes = int(decoded_bytes)
        writer.writerow([decoded_bytes])

        if ((prev_byte+1) != decoded_bytes):
            print('bruh momement')
            print(prev_byte,'-', decoded_bytes)

        prev_byte = decoded_bytes

    except:
        print("Error")