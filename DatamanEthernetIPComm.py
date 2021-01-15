'''
Ethernet/IP Communication using the CIP protocol

Documentation: https://python-snap7.readthedocs.io/en/latest/client.html
'''

from pycomm3 import CIPDriver

ip = '192.168.105.128'

device = CIPDriver(ip)

print("Device Open: ", device.open())
print("Device Identity: ", device.list_identity(ip), "\n")


service_code = b'\x0E'
class_code = b'\x79'
instance = b'\x0E'

msg = device.generic_message(service_code, class_code, instance)
print(msg)
device.close()






