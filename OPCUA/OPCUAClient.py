'''
Basic OCP client program.
Sample uses Cognex device to communicate with.

Documenation: https://python-opcua.readthedocs.io/en/latest/index.html
GitHub: https://github.com/FreeOpcUa/python-opcua

Cognex OPCUA: https://support.cognex.com/docs/is_592/web/EN/ise/Content/Communications_Reference/OPCUA-Intro.htm?tocpath=Communications%20Reference%7COPC%20UA%7C_____0

OPCUA Sniffer: https://www.unified-automation.com/products/development-tools/uaexpert.html

'''
import time

from opcua import Client
#Simulation server ip
url = "opc.tcp://localhost:4840"
#Cognex ip sample
url = "opc.tcp://192.168.104.109:4840"
#Create client instance on url, create multiple for multiple devices
client = Client(url)
#connect to client instance
client.connect()
print("Client Connected on Server {} ".format(url))


#Gets name of object node
root = client.get_root_node()
print ("Root node: ", root)
#Gets object node
objects = client.get_objects_node()
print("Object Node: ", objects)
#Gets all children variles in node and lists
variables = root.get_children()
print("Node Children: ", variables)

try:
    while True:
        '''
        AcquistionCount = client.get_node("ns=2;s=Job.Inspection_Count")
        result = AcquistionCount.get_value()
        print("Acquisition Count: ", result)
        '''
        #To get data back node and object must be passed. To get node number check in doumentation or OPC sniffer.
        #object can be passed as int (e.g. i = 2555) or string (e.g. s=time).
        #For Cogex the string is equal to the OPC cell name set in inight
        PassCount = client.get_node("ns=2;s=Job.Pass_Count")
        #Gets value of node
        result = PassCount.get_value()
        print("Pass Count: ", result)

        FailCount = client.get_node("ns=2;s=Job.Fail_Count")
        result = FailCount.get_value()
        print("Fail Count: ", result)

        '''
        cognexTime = client.get_node("ns=2;i=2258")
        result = cognexTime.get_value()
        print("Time: ", result)
        '''
        time.sleep(1)

finally:
    client.disconnect()