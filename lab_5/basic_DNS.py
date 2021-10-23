# -----------------------------------------------------------
# -----------------------------------------------------------
# Lab 5: DNS client
# General structure
# -----------------------------------------------------------
# -----------------------------------------------------------
import sys
import time
from socket import *


# -----------------------------------------
# URL formatting function (YOUR CODE)
# -----------------------------------------
def formatNameFiled(url_in):
    byte_url = b''

    for i in url_in.split("."):
        byte_url += chr(len(i)).encode('ascii') + \
            i.encode('ascii')

    return byte_url + chr(0).encode('ascii') \
        + chr(0).encode('ascii') \
        + chr(1).encode('ascii') \
        + chr(0).encode('ascii') \
        + chr(1).encode('ascii')


DNS_server = ''
DNS_port = 53
timeout = 5
# -----------------------------------------
# Socket initialization
# -----------------------------------------

clientsocket = socket(AF_INET, SOCK_DGRAM)
clientsocket.settimeout(timeout)

DNS_port = int(DNS_port)


url_to_query = 'www.oru.se'
formatted_url = formatNameFiled(url_to_query)
additional_info = b''
# -----------------------------------------
# Question assembly (YOUR CODE)
# -----------------------------------------
query_to_DNS = additional_info+formatted_url

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
