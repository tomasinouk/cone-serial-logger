#!/usr/bin/python           # This is client.py file

import socket               # Import socket module

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         # Create a socket object
# host = socket.gethostname() # Get local machine name
host = "10.0.26.1"
port = 4001                # Reserve a port for your service.

s.connect((host, port))
# print s.recv(1024)

# Look for the response
amount_received = 0    
while 1:
    data = s.recv(1024)
    amount_received += len(data)
    print 'received "%s"' % data

# s.close                     # Close the socket when done