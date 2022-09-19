"""
Description: A Basic Python Socket That Prints Data It Recives.
Date: September 2022
Author: Aleksa Zatezalo
"""

import socket

# Create Socket
host = socket.gethostname()
port = 12345
s = socket.socket()		# TCP socket object
s.bind((host,port))
s.listen(5)

# Accept Client Connection
print("Waiting for client...")
conn,addr = s.accept()	        # Accept connection when client connects
print("Connected by " + addr[0])

# Print Client Data
while True:
	data = conn.recv(1024)	    # Receive client data
	if  data:
         print(data.decode('utf-8'))