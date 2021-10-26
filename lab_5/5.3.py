import sys
import time
from socket import *


def formatNameFiled(url_in):
    byte_url = b''
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

    for i in url_in.split("."):
        byte_url += (chr(len(i)) + i).encode('ascii')

    return headers + byte_url + queries


DNS_server = '1.1.1.1'
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
query_to_DNS = formatNameFiled(url_to_query)

try:

    clientsocket.sendto(query_to_DNS, (DNS_server, DNS_port))
    message, address = clientsocket.recvfrom(1024)
    print(message)
    # -----------------------------------------
    # Response parsing (YOUR CODE)
    # -----------------------------------------

except:
    # -----------------------------------------
    # Exception handling
    # -----------------------------------------
    print('A timeout has occured, no reply from the DNS server')
