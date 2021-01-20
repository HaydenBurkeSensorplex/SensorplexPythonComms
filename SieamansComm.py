'''
Python Comms with Sieamns STEP-7 plc
Documentation: https://python-snap7.readthedocs.io/en/latest/
To install library pip install python-snap7 then download: https://sourceforge.net/projects/snap7/files/1.4.2/
placing the x64 or x32 version (dependent on PC) snap.dll and snap.lib files in enviroment varible folder 

Ensure PLC protection is setup correctly according to this: http://snap7.sourceforge.net/snap7_client.html#1200_1500 or you will get a 
CPU non response error.
'''

import snap7

ip = '192.168.0.1'


#Connect to PLC Server
plc = snap7.client.Client()
plc.connect(ip, 0, 0)

#Get curent connection status of plc 
connection_status = plc.get_connected()
print("Connection Status: ", connection_status)

#Read PLC database 
print(plc.db_read(1 ,0, 100))

#disconnect from plc
plc.plc_stop()
