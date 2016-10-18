# The program is intented to get used familarised with the sockets. 
# The server here simply echoes back the data sent by the client
# Server side implementation. Below are the set of steps needed to setup a server
# 1. Create a TCP/UDP Socket
# 2. Bind the socket to the address
# 3. Listen to the incoming connections
# 4. Accept the incoming connections
# 5. Close the socket
# Server Socket is used for accepting the connections
# Client Socket is used for sending the data back to the client 
# Author:  Rohit p. Tahiliani

import socket
import sys 

# Making it available to all the interfaces
HOST = ''		
# Using any non-privileged port													 
PORT = 23000	
backlog = 5
try:
	serverSocket = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
	#REUSEADDR flag is set. This allows kernel to reuse a local socket in TIME_WAIT state 
	serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  
	serverSocket.bind ((HOST, PORT))
	# Enable the server to accept multiple connections
	serverSocket.listen (backlog)
except socket.error, errorMessage:
	print "Error performing socket operations: %s" %errorMessage
	sys.exit(1)

#Setting up the server to be alive forever
while True:
	try:
		# Server Socket will be reused to listen to new connections
		clientSocket, (remoteHost, remotePort) = serverSocket.accept()
		print "Connection received from " + remoteHost
		data = clientSocket.recv (100)
		if not data:
			print "No data recieved from the client"
			break
		clientSocket.send ("You are now connected to the server. ")
		clientSocket.send (data)
		clientSocket.close ()
	except KeyboardInterrupt:
		print "Aborting!! Server shutting down"
  		sys.exit(0)