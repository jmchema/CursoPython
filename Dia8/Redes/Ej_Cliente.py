# Ejemplo de cliente, usando sockets:

import socket # Import socket module

s = socket.socket() # Create a socket object

host = "192.168.7.105" # Get local machine name Hemos puesto la del profe

port = 12345 # Reserve a port for your service.

s.connect((host, port))

print(str(s.recv(1024),encoding="utf-8"))

s.close() # Close the socket when done