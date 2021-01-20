'''
This program simulates an OPC UA server for use of debugging when creating a OPC client.
The program creates an OPC server of localhost:4840 on node 1 named parameters, and 3 varibles Temperature, pressure and time that are randomly
generated.
Devices that are to communicated with host their own OPCUA server that a client needs to connect too.

'''

import datetime
import random
import time

from opcua import ua, Server

server = Server()

url = "opc.tcp://localhost:4840"
server.set_endpoint(url)

name = "OPCUA Simulation Server"
addressSpace = server.register_namespace(name)

node = server.get_objects_node()

Param = node.add_object(addressSpace, "Parameters")

Temp = Param.add_variable(addressSpace, "Temperature", 0)
Press = Param.add_variable(addressSpace, "Pressure", 0)
Time = Param.add_variable(addressSpace, "Time", 0)

Temp.set_writable()
Press.set_writable()
Time.set_writable()

server.start()

print("Simulation Server Started at {}".format(url))

while True:
    Temperature = random.randint(10, 50)
    Pressure = random.randint(10, 500)
    currentTime = datetime.datetime.now()

    print(Temperature, Pressure, currentTime)

    Temp.set_value(Temperature)
    Press.set_value(Pressure)
    Time.set_value(currentTime)

    time.sleep(1)