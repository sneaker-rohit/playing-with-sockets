# The program is intented to get used familarised with the sockets. 
# The client here sends a message to the server and prints the response received
# Client side implementation. Below are the set of steps needed for the client to connect
# 1. Connect to the address
# 2. Send a message to the server 
# Author:  Rohit p. Tahiliani

import socket 

PORT = 23000	
HOST = ''
# Maximum amount of data to be received at once.  
receiveBuffer = 4096 
# Creating a Socket
clientSocket = socket.socket (socket.AF_INET,socket.SOCK_STREAM)
# Connect to the remote server using appropriate address
clientSocket.connect ((HOST,PORT))
# Send a message to the server 
clientSocket.send ("Hey there server!")
print clientSocket.recv (receiveBuffer)
# Close the connection
clientSocket.close ()
