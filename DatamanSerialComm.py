'''
Basic serial communication script for reading and writing over com port.
Tested for DataMan 8700 USB.

Documentation: https://pyserial.readthedocs.io/en/latest/
'''

import serial
import binascii
import time

#Initialise new serial object
#This can be any device that communicates over serial port, just ensure
#correct port and buad rate are supplied
ser = serial.Serial(
    port='COM3',
    baudrate=9600,
    timeout=5
)

if ser.isOpen():
    print("Connected to Device")
else:
    print("Not Connected")

time.sleep(0.5)

#Message to device, needs to be encoded to a byte format to send to devices over serial,
#this can be done in 2 ways, by using the .encode() method at end of string or writting int eh following format b"MY STRING"
#Message needs to be in format required by device manufacturer.

#Sample messages for dataman, for other types of serial communication, use decvice manufactures style
msg = "||>GET DEVICE.TYPE\r\n".encode()
msg = "||>SET DVALID.GS1-FORMAT <AI05>\r\n".encode()
msg = "||>SET DVALID.TYPE 5\r\n".encode()
msg = "||>trigger off\r\n".encode()
w
#Write serial message to serial port
ser.write(msg)
time.sleep(0.5)

#Read response back from device, pass length of expented response, for dynamic array use in_waiting method
response = ser.read(ser.in_waiting)
#decode the response from bytes to string 
print(response.decode('utf-8'))

time.sleep(1)

count = 0

#Keep reading serial port and prints any results when they occur
while True:
    response = ser.read(ser.in_waiting)
    if response:
        count += 1
        print(count, 'Response: ', response)
    
ser.close()