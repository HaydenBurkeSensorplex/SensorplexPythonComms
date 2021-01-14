from pycomm3 import LogixDriver
'''
Documentation 
https://pycomm3.readthedocs.io/en/latest/usage.html


'''
with LogixDriver('192.168.10.111') as plc:
    print(plc)

    tag_list = plc.get_tag_list()
    print(f"Tag List: {0}", tag_list)

    #List names of All tags
    i=0
    for tag in tag_list:
        i += 1 
        tag_names = tag['tag_name']
        print(i, tag_names)

    #Reading PLC tag values
    tag_read = plc.read('test_io')
    print("Tag Read: ", tag_read)
    print("Tag Value: ", tag_read.value)
    print("Tag Type: " ,tag_read.type)

    #Write 
    plc.write(('test_int', 100))
    plc.write(('test_o_8', True))
    #Write muliple
    plc.write(('REAL2', 25.2), ('STRING3', 'A test for writing to a string.'))