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
        print('A new request has been received...')
        print(message)

        data_received = message.split(b'\r\n')

        # Convert the bytes to a string and then split the first line in the data by space to get the requested page.
        requested_resource = str(data_received[0]).split(' ')[1]
        print(requested_resource)

        try:
            f = open(requested_resource[1:], 'rb')
            outputdata = f.read()
            connectionSocket.sendall(outputdata)
        except IOError:
            data = 'HTTP/1.0 404 NOT FOUND\n\n<h1>404 File Not Found </h1>'
            connectionSocket.send(data.encode(encoding='utf_8'))

        # Close the client connection socket
        connectionSocket.close()

    except IOError:
        # ----------------------------------
        #       I/O Error handling
        # ----------------------------------
        connectionSocket.close()
 #       else:
 #               print('An exception has occured')

serverSocket.close()
