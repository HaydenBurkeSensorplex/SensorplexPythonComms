'''
This program shows the basic all basic DIO read and writting functions for the EOS using ADLink SDK. For practical examples, see ADLinkEOSDIO.py.
For Orginal sample code by ADLink, see ADLinkE13D.py

The program uses ctypes, which allow python to understand C/c++, c# and .NET library files, allowing you to access
there functions. 

All information for the SDK functions can be found on ADLink website, all can be used in python, just ensure you pass
the equivalent varible types to the equivalent ctype. Example to pass the int "i = 1" into the SDK, you pass "ctypes.c_int(1)"

Documentation: https://www.adlinktech.com/Products/Machine_Vision/VisionSystems/EOS-1300?lang=en

Further documenation for SDK can be found in SDK installtion directory

'''

#Required Libraries for DIO
import ctypes  
import os, sys
import time

#All varibles should stay constant for EOS
#ID value for DIO card. See adlink documentation
PCIe_E13D=49
DINums = 12
DIState = ctypes.c_int(0)
DOState = ctypes.c_int(0)
Port = ctypes.c_int(0)
CardNumber = 0

#Calls ADLink SDK into python. Ensure correct file path is set to installation path of the SDK.
#Once passed correctly all functions found in the .c library can be accessed by python to be used.
dll = ctypes.windll.LoadLibrary('C:\Program Files\ADLINK\PCIe-E13D\Library\PCI-Dask64.dll')

# Register device
# Device must be registered to open communication, it must also be closed after operation, see below
Card_Number = dll.Register_Card(PCIe_E13D, 0)

# The following shows how to use the DIO functions
# Line refers to single DIO and Port referes to all DIO (0-15)

###########################
# DIGITAL INPUT FUNCTIONS #
###########################

##Read DI Line##
#Reads values of DI 0 and stores value in DIState
dll.DI_ReadLine(CardNumber, Port, 0, ctypes.byref(DIState))
print("DI state:  "+ "{0:b}".format(DIState.value).zfill(12))


##Read DI Port##
#Reads all DI values (0-15) 
dll.DI_ReadPort(0, Port, ctypes.byref(DIState))
print("DI state:  "+ "{0:b}".format(DIState.value).zfill(12))

############################
# DIGITAL OUTPUT FUNCTIONS #
###########################

## Write DO Line ##
# Sets DO 0 to high. Passes CardNumber, Port, Line, State 
dll.DO_WriteLine(CardNumber, Port, 0, 1)
time.sleep(0.1)

## Write DO Port ##
#Sets entire port to low i.e DO(0-15), Passes CardNumber, Port, State
dll.DO_WritePort(CardNumber, Port, 0)
time.sleep(0.1)

##Read DO Line##
#Reads State of DO 0 and returns result to DOState
dll.DO_ReadLine(CardNumber, Port, 0, ctypes.byref(DOState))
#Prints DO state as 16bit number. .format to format as 16bit sring. .zfill to fill all other values as 0's
print("DO state:  "+ "{0:b}".format(DOState.value).zfill(12)))

##Read DO Port##
#Reads State of all DO on port and returns to DOState in a byte format
dll.DO_ReadPort(CardNumber, Port, ctypes.byref(DOState))
#Prints DO state as 16bit number. .format to format as 16bit sring. .zfill to fill all other values as 0's
print("DO state:  "+ "{0:b}".format(DOState.value).zfill(12)))

# Release device
dll.Release_Card(0)

#####################
# FURTHER FUNCTIONS #
#####################

#The more advanced SDK functions can be used i.e. Debounce, triggering, PWM or encoder functions as found in the SDK.
#There may be a slowdown in commnuication however with communicating python to the SDK.


