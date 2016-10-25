# The program is intented to get used familarised with the sockets. 
# The client here sends a message to the server and prints the response received
# Client side implementation. Below are the set of steps needed for the client to connect
# 1. Connect to the address
# 2. Send a message to the server 
# Author:  Rohit P. Tahiliani

import socket 

PORT = 1000	
HOST = '127.0.0.1'
# Maximum amount of data to be received at once.  
receiveBuffer = 4096 
# Creating a Socket
clientSocket = socket.socket (socket.AF_INET,socket.SOCK_STREAM)
# Connect to the remote server using appropriate address
clientSocket.connect ((HOST,PORT))
print "[+] Connected to the server..."
# Send a message to the server
message = raw_input ("Enter the message/Quit: ") 
while message != "Quit":
	clientSocket.send (message)
	data = clientSocket.recv (receiveBuffer)
	print "[+] Message from server..."
	if data:
		print data 
	else: 
		print "No data received from the client"
	message = raw_input ("Enter the message/Quit: ")
# Close the connection
print "[-] Terminating the connection to server..."
clientSocket.close ()
