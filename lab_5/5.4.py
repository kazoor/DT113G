import sys
import time
from socket import *

headers = (chr(23) + chr(117) + \
        chr(1) + chr(0) + \
        chr(0) + chr(1) + \
        chr(0) + chr(0) + \
        chr(0) + chr(0) + \
        chr(0) + chr(0)).encode('ascii')

queries = (chr(0) \
        + chr(0) \
        + chr(1) \
        + chr(0) \
        + chr(1)).encode('ascii')

def formatNameFiled(url_in):
    byte_url = b''

    for i in url_in.split("."):
        byte_url += (chr(len(i)) + i).encode('ascii')

    return byte_url

def getFirstDatalength(msg, skip_amount, length, step):
    first_data_len = []
    for i in range(skip_amount, length, step):
        first_data_len.append(msg[i:i+2])
    
    return first_data_len[0]

DNS_server = '130.243.97.77'
DNS_port = 53
timeout = 5
# -----------------------------------------
# Socket initialization
# -----------------------------------------

clientsocket = socket(AF_INET, SOCK_DGRAM)
clientsocket.settimeout(timeout)

DNS_port = int(DNS_port)

url_to_query = 'www.oru.se'
# -----------------------------------------
# Question assembly (YOUR CODE)
# -----------------------------------------
query_to_DNS = headers + formatNameFiled(url_to_query) + queries

#try:

clientsocket.sendto(query_to_DNS, (DNS_server, DNS_port))
message, address = clientsocket.recvfrom(1024)
# print(message)

# -----------------------------------------
# Response parsing (YOUR CODE)
# -----------------------------------------
bytes_to_skip = len(query_to_DNS)
corrected_len = len(message) - bytes_to_skip

byte_counter = 0
message = message[bytes_to_skip:]
ip_addresses = []
data_len = 0
last_count = 0
record_type = 0

while byte_counter < corrected_len:
    if data_len == 0 and byte_counter == 11:
        data_len = message[byte_counter]
        record_type = message[byte_counter - 6]
        last_count = byte_counter

    elif data_len != 0 and record_type == 1 and byte_counter == last_count + (15 + data_len):
        data_len = message[last_count + byte_counter + data_len]
        record_type = message[(last_count + byte_counter + data_len) - 6]
        ip_addresses.append(message[(last_count + byte_counter + data_len) : (last_count + byte_counter + data_len) + data_len])
        #print(message[(last_count + byte_counter + data_len): (last_count + byte_counter + data_len) + data_len])
        last_count = byte_counter
        #print(chr(message[last_count + byte_counter + data_len]).encode('ascii'))
    
    #print(data_len)
    #print(record_type)
    print(last_count)
    byte_counter += 1
#except:
    # -----------------------------------------
    # Exception handling
    # -----------------------------------------
   # print('A timeout has occured, no reply from the DNS server')
