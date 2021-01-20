
from cpppo.server.enip.get_attribute import proxy_simple, proxy

ip = '192.168.104.109'

vendor, product_name, test = proxy_simple(ip).read([('@1/1/1','INT'),('@1/1/7','SSTRING'),('@0x79/1/0x06','BOOL')])
for x in range (50):
    print(proxy_simple(ip).write([('@0x79/1/0x10',True)]))
    print(proxy_simple(ip).write([('@0x79/1/0x10',False)]))

print(vendor)
print(product_name)

print(test)





