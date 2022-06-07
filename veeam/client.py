# Import socket module
import socket

# Create a socket object
s = socket.socket()

# Define the port on which you want to connect
port = 8000

# connect to the server on local computer
s.connect(('127.0.0.1', port))
s.sendall(b"Hello, world")

# receive data from the server and decoding to get the string.
print(s.recv(1024).decode())
data = s.recv(1024)
print(f"Received {data!r}")
# close the connection
s.close()



