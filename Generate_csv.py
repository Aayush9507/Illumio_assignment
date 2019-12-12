import random
import socket
import struct


# Script to generate sample csv.
directions = ["inbound", "outbound"]
csv = open("test.csv", "w")
protocol = ["udp", "tcp"]
port_high = 65535
ipHalf = 2147483647


def randomIP(low=1, high=0xffffffff):
    return socket.inet_ntoa(struct.pack('>I', random.randint(low, high)))


for x in range(random.randint(0, 500000)):
    row = directions[random.randint(0, 1)] + "," + protocol[random.randint(0, 1)] + ","
    row += str(random.randint(1, port_high)) + "," + str(randomIP()) + "\n"
    csv.write(row)

# Populate ip ranges
for x in range(random.randint(0, 250000)):
    row = directions[random.randint(0, 1)] + "," + protocol[random.randint(0, 1)] + ","
    row += str(random.randint(1, port_high)) + ","
    row += str(randomIP(1, ipHalf)) + "-" + str(randomIP(ipHalf)) + "\n"
    csv.write(row)

# Populate port ranges
for x in range(random.randint(0, 10000)):
    row = directions[random.randint(0, 1)] + "," + protocol[random.randint(0, 1)] + ","
    row += str(random.randint(1, 30000)) + "-" + str(random.randint(30000, port_high)) + ","
    row += str(randomIP()) + "\n"
    csv.write(row)

csv.close()


#https://stackoverflow.com/questions/21014618/python-randomly-generated-ip-address-of-the-string