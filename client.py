# -*- coding: utf-8 -*-
#!/usr/bin/python                       # This is client.py file

import socket                           # Import socket module
 
s = socket.socket()                     # Create a socket object
host = socket.gethostname()             # Get local machine name
port = 55555                            # Reserve a port for your service.
 
print 'Connecting to ', host, port
s.connect((host, port))
 
while True:
    msg = raw_input('CLIENT >> ')
    msg = msg.encode("UTF-8")
    s.send(msg)
    #s.close                            #Close the socket when done
    continue
