from serial.tools import list_ports
import serial
import time
import csv
#Print COM Ports
print("Test Start")
ports = list_ports.comports()
for port in ports:
    print(port)
#Wait for user input for the com port # 
ComPort = input("Which COM Port is the TestBlock? ")
ComPort = 'COM' + ComPort
print(ComPort)
# Open to open the serial com port
try:
    serialCom = serial.Serial(ComPort,115200)
#Fail if there is no comport 
except:
    print('NO COM PORT SPECIFIED HERE')
    exit() 
# wait for the unser to input a file name
FileName = input("What is the .csv file name? ")
FileName = FileName + '.csv'
print(FileName)
# Create CSV file
try:
    f = open(FileName,"w",newline='')
    f.truncate()
except:
    print('CANT OPEN FILE')
    exit() 


# Toggle DTR to reset the Arduino
serialCom.setDTR(False)
time.sleep(1)
serialCom.flushInput()
serialCom.setDTR(True)
time.sleep(1)

writer = csv.writer(f, delimiter=",")
# How many data points to record
kmax = 1000
prev_byte = 0; 
for k in range(kmax):
    try:
        print("bruh1")
        #serialCom.write(b'A')
        s_bytes = serialCom.readline()
        decoded_bytes = s_bytes.decode("utf-8").strip('\r\n')
        decoded_bytes = int(decoded_bytes)
        writer.writerow([decoded_bytes])

        #if ((prev_byte+1) != decoded_bytes):
            #print('bruh momement')
            #print(prev_byte,'-', decoded_bytes)

        #prev_byte = decoded_bytes

    except:
        print("Error")