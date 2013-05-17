# -*- coding: utf-8 -*-                                                                # Document as UTF-8 Document.
#!/usr/bin/python                                                                      # This is server.py file

import socket                                                                          # Import the Sockets...
import time                                                                            # Import the time Module.
import sys                                                                             # Import the System Module.
import urllib2

sys.path.append("Modules/guess_language")                                            # Get Language Function
import check_language                                                                  # Import Language Function
sys.path.append("Modules/SL4A")
import android
sys.path.append("Functions/Weather")                                                     # Get Weather Module Location.
import Weather                                                                         # Import the Weather module.
sys.path.append("Functions/Logger")                                                      # Get Weather Module Location.
import logit                                                                           # Import the Logger Module.
#sys.path.append("Functions/GoogleTTS")
#import GoogleTTS

print("***************************************************")
print("*   _        _______  _______  _______  _         *")
print("*  | \    /\(  ____ \(  ____ )(  ____ \( (    /|  *")
print("*  |  \  / /| (    \/| (    )|| (    \/|  \  ( |  *")
print("*  |  (_/ / | (__    | (____)|| (__    |   \ | |  *")
print("*  |   _ (  |  __)   |     __)|  __)   | (\ \) |  *")
print("*  |  ( \ \ | (      | (\ (   | (      | | \   |  *")
print("*  |  /  \ \| (____/\| ) \ \__| (____/\| )  \  |  *")
print("*  |_/    \/(_______/|/   \__/(_______/|/    )_)  *")
print("*                                                 *")
print("***************************************************")

def Main():

         print '[-] Waiting for clients...' 
         s.listen(5)                                                                   # Now wait for client connection.
         c, addr = s.accept()                                                          # Establish connection with client.
         print '[-] Got connection from', addr[0]     
         logit.logger("Info","New Connection from: " + addr[0])                        # Log New Connection

         while True:                                                                   # While Client Not Disconnected.
            try:                                                                       # Try to do something.
               msg = (c.recv(1024).decode("UTF-8"))                                    # Recieve Socket Message
               print "[" + addr[0] + "]", ' >> ' + "New Request Recieved, Logged."     # Log Message
               msg = (msg.encode("UTF-8"))
               logit.logger("Req","New Request:  " + msg + " From: " + addr[0])        # Log New Client Connection
               if(msg == ""):
                  print '[-] Client Disconnected...'
                  logit.logger("Info","Client Disconnected: " + addr[0])
                  Main()
               else:
                  language = check_language.checkLanguage(msg)                         # Check For the Request Language
                  continue                                                             # Don't stop, Continue
            except:                                                                    # If Client disconnect, then....
               print '[-] Client Disconnected...'
               logit.logger("Info","Client Disconnected: " + addr[0])
               time.sleep(1)
               Main()
               continue               

exception = 0

# droid = android.Android(('0.0.0.0', 6789))                                           # Make contct with the android Public Server.

s = socket.socket()                                                                    # Create a socket object
Server_HOST = socket.gethostname()                                                     # Get local machine name
Server_PORT = 44444                                                                    # Reserve a port for your service
         
print '[-] Server started!'                                                            # Server Started Message
time.sleep(1)                                                                          # Sleep 1 Second.                                                    # Waiting for Clients...
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((Server_HOST, Server_PORT))                                                     # Bind to the port
Main()

while(exception == 0):
   try:

      Main()                                                 # Continue to do the same in loop.

   except (KeyboardInterrupt, SystemExit):                                             # If Server Crashed then...
      
      print("[!] Server Interuppted Or Crashed Down ...")
      time.sleep(1)
      logit.logger("Fatal","Server Crashed Unexpectualy.")
      time.sleep(1)
      print("[-] Reconnecting to the server ...")
      time.sleep(1)
      print '[-] Server started!'                                                      # Server Started Message
      time.sleep(1)                                                                    # Sleep 1 Second.
      print '[-] Waiting for clients...'                                               # Waiting for Clients...

      
   continue                                                                            # Power back the server, Again.
