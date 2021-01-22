import ctypes  
import os, sys
import time

PCIe_E13D=49
DINums = 12
DIState = ctypes.c_int(0)
Port = ctypes.c_int(0)

#The following code shows how to call the sdk library in the python
# Load C library from .dll
dll = ctypes.windll.LoadLibrary('C:\Program Files\ADLINK\PCIe-E13D\Library\PCI-Dask64.dll')

# Register device
Card_Number = dll.Register_Card(PCIe_E13D, 0)

# Get DI
dll.DI_ReadPort(0, Port, ctypes.byref(DIState))
print("DI state:  "+ "{0:b}".format(DIState.value).zfill(12))
print("")

# Set DO0 Enable
dll.DI_ReadPort(0, Port, ctypes.byref(DIState))
print("Before DI state:  "+ "{0:b}".format(DIState.value).zfill(12))

print("Set DO 0 Enable")
dll.DO_WriteLine(0, Port, 0, 1)
time.sleep(0.1)
dll.DI_ReadPort(0, Port, ctypes.byref(DIState))
print("After DI state:  "+ "{0:b}".format(DIState.value).zfill(12))
print("")

# Set DO0 Disable
dll.DI_ReadPort(0, Port, ctypes.byref(DIState))
print("Before DI state:  "+ "{0:b}".format(DIState.value).zfill(12))

print("Set DO 0 disable")
dll.DO_WriteLine(0, Port, 0, 0)
time.sleep(0.1)
dll.DI_ReadPort(0, Port, ctypes.byref(DIState))
print("After DI state:  "+ "{0:b}".format(DIState.value).zfill(12))

# Release device
dll.Release_Card(0)