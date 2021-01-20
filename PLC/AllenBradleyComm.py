from pycomm3 import LogixDriver

'''
This script shows how to use the pycomm3 library to communicate with a ControlLogix PLC.
The library can also be used for Ethernet/IP communication using the CIP protocol, for examples of this 
see DatamanEthernetIPComm.py

Documentation 
https://pycomm3.readthedocs.io/en/latest/usage.html

'''

#Use the "with" statment for all commands, as it ensures connection with plc is closed after all tasks are complete
with LogixDriver('192.168.10.111') as plc:
    #Print Basic info about the PLC 
    print(plc)

    #######################                    
    # Get Tag Information #
    #######################

    #Gets a list of all tags currently on plc, and information related to them.
    tag_list = plc.get_tag_list()
    print(f"Tag List: {0}", tag_list)

    #Takes the list of tags and only prints their names.
    i=0
    for tag in tag_list:
        i += 1 
        tag_names = tag['tag_name']
        print(i, tag_names)

    ##########################                      
    # Reading PLC tag values #
    ##########################

    #Reads the information about passed tag, name of tag needs to be passed and will return all
    #information currently stored in tag, including, value, varible type, error code. Single Components can be sliced out however.
    tag_read = plc.read('test_io')
    #Shows all tag information
    print("Tag Read: ", tag_read)
    #Sliced tag information 
    print("Tag Value: ", tag_read.value)
    print("Tag Type: " ,tag_read.type)
    print("Tag Error: " ,tag_read.error)


    ##########################                      
    # Writing PLC tag values #
    ##########################

    #Writes required data to plc tag. Data type written to plc must match data type of the plc, see examples below

    #Writes int to tag
    plc.write(('test_int', 100))
    #Writes bool to output pin
    plc.write(('test_o_8', True))
    #Write to multiple tags at once
    plc.write(('test_float', 25.2), ('test_string', 'A test for writing to a string.'))

    #######################
    # Advanced Techniques #
    #######################

    #Filtering Tag Search

    # PIDs are structures, the data_type attribute will be a dict with data type definition.
    # For tag types of 'atomic' the data type will a string, we need to skip those first.
    # Then we can just look for tags whose data type name matches 'PID'
    pid_tags = [
        tag
        #plc.tags.items() returns two items so we need a tag and _def varible 
        for tag, _def in plc.tags.items()
        if _def['tag_type'] == 'struct' and _def['data_type']['name'] == 'PID'
    ]

    print(pid_tags)