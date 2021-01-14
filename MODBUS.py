'''
Documentation: https://minimalmodbus.readthedocs.io/en/stable/apiminimalmodbus.html
'''

import minimalmodbus

port = #COMx
slaveaddress = #1 to 247
mode = 'rtu' #rtu or ascii

sensor = minimalmodbus.Instrument(port, slaveaddress, mode)


value = sensor.read_register(,1) # Registernumber, number of decimals
print("Value: ", value)

sensor.write_register()# Registernumber, value, number of decimals for storage
