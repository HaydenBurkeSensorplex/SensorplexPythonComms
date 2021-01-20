'''
Ethernet/IP Communication using the CIP protocol

Documentation: https://python-snap7.readthedocs.io/en/latest/client.html
'''

from pycomm3 import CIPDriver

ip = '192.168.105.128'

device = CIPDriver(ip)

print("Device Open: ", device.open())
print("Device Identity: ", device.list_identity(ip), "\n")


'''
All 3 codes need to be set in order to access a CIP function, refer to Dataman Ethernet/IP documentation for codes, as some codes are
specific to a vendor see: http://www.htz.com.tw/files/cognex/manual/dataman_CommunicationsAndProgramming.pdf page 18.

For generic CIP codes follow the standardised codes, see: https://pycomm3.readthedocs.io/en/latest/cip_constants.html

A combination of the 3 codes will result in a function being executed.
'''

service_code = b'\x0E'
class_code = b'\x79'
instance = b'\x0E'

msg = device.generic_message(service_code, class_code, instance)
print(msg)
device.close()






