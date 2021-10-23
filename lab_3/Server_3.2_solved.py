# Import socket module
from socket import *

# Create a TCP server socket
# (AF_INET is used for IPv4 protocols)
# (SOCK_STREAM is used for TCP)

serverSocket = socket(AF_INET, SOCK_STREAM)

# Assign a port number
serverPort = 80

# Bind the socket to server address and server port
serverSocket.bind(("", serverPort))

# Listen to at most 1 connection at a time
serverSocket.listen(1)

while True:
    print('Waiting for requests ...')
    # Set up a new connection from the client
    connectionSocket, addr = serverSocket.accept()
    # If an exception occurs during the execution of try clause
    # the rest of the clause is skipped
    # If the exception type matches the word after except
    # the except clause is executed
    try:
        message = connectionSocket.recv(1024)
        # -------------------------------------------
        #       Request handling Section
        # -------------------------------------------
        data_received = message.split(b'\r\n')

        # Convert the bytes to a string and then split the first line in the data by space to get the requested page.
        requested_resource = str(data_received[0]).split(' ')[1]

        # Open and send the file requested from the browser input.
        f = open(requested_resource[1:], 'rb')
        outputdata = f.read()

        # Make sure to close the file handle
        f.close()

        # Send the data to client.
        connectionSocket.sendall(outputdata)

    except IOError:
        # ----------------------------------
        #       I/O Error handling
        # ----------------------------------
        connectionSocket.close()
    except IndexError:
        print('Index error exception')
serverSocket.close()
