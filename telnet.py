import sys
import  telnetlib

Host = "stackoverflow.com"
Port_1 = "80"
Port_2 = "443"

print("opening telnet")

Tn_1 = telnetlib.Telnet(Host, Port_1)
Tn_2 = telnetlib.Telnet(Host, Port_2)

print("established telnet")
#
# msg_1 = ("GET /questions HTTP/1.0\r\nHost: stackoverflow.com\r\n\r\n").encode('ascii')
msg_1 = ("GET /questions HTTP/1.0\r\nHost:"+Host+"\r\n\r\n").encode('ascii')

#
print("write telnet")
Tn_1.write(msg_1)
print("read telnet")
output=Tn_1.read_all()
print(output)
with open('output_80.txt', 'w') as f:
    f.write(str(output))
print("close telnet")
Tn_1.close()

#
# print("write telnet")
# Tn_2.write(msg_1)
# print("read telnet")
# output=Tn_2.read_all()
# print(output)
# print("close telnet")
# Tn_2.close()
