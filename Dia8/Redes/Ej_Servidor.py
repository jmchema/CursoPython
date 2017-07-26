# Ejemplo de servidor, usando sockets:

import socket # Import socket module

s = socket.socket() # Create a socket object

host = socket.gethostname() # Get local machine name

port = 12345 # Reserve a port for your service.

s.bind((host, port)) # Bind to the port

s.listen(5) # Now wait for client connection.

cont = 0
while True:
    c, addr = s.accept() # Establish connection with client.
    cont += 1
    print('Got connection from {}'.format(addr))
    c.send(bytes('Gracias por venir. Eres el visitante numero {}'.format(cont),encoding="utf-8"))
    c.close() # Close the connection
  