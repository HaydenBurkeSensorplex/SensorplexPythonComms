'''
This is a sample program for communication with the EOS DIO card using the ADLink SDk
Ensure SDK has been downloaded and installed, recording the install path for library.

The program itself turns all DO on, then waits 1 second, then turns them off for 1 second.

The program uses ctypes, which allow python to understand C/c++, c# and .NET library files, allowing you to access
there functions. 

All information for the SDK functions can be found on ADLink website, all can be used in python, just ensure you pass
the equivalent varible types to the equivalent ctype.

'''
import ctypes  
import os, sys
import time

PCIe_E13D=49
#Load number of DIO pins
DINums = 12
#Used to get current state of DI
DIState = ctypes.c_int(0)
#Used to get current state of DO
DOState = ctypes.c_int(0)
#Port for DIO card. Always 0 for EOS card
Port = ctypes.c_int(0)

#Calls ADLink SDK into python. Ensure correct file path is set to installation path of the SDK.
#Once passed correctly all functions found in the .dll can be accessed by python to be used.
dll = ctypes.windll.LoadLibrary('C:\Program Files\ADLINK\PCIe-E13D\Library\PCI-Dask64.dll')

# Register device
Card_Number = dll.Register_Card(PCIe_E13D, 0)


while True:
    for i in range(16):
        print(f"Set DO {i} On")
        dll.DO_WriteLine(0, Port, i, 1)
        time.sleep(0.1)
    time.sleep(1)

    for i in range(16):
        print(f"Set DO {i} Off")
        dll.DO_WriteLine(0, Port, i, 0)
        time.sleep(0.1)
    time.sleep(1)


# Release device
dll.Release_Card(0)
