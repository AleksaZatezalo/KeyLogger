
import socket
host = socket.gethostname()
port = 12345
s = socket.socket()		# TCP socket object

s.connect((host,port))

#s.sendall(('This will be sent to server').encode('utf-8'))    # Send This message to server