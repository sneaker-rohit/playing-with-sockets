# The program is intented to get used familarised with the sockets. 
# The server here implements multi threading. Multiple clients connect to the server. The server handles 
# each client in a new thread. It simply echoes back message to the client.
# Author:  Rohit P. Tahiliani


import socket
from threading import Thread  
import sys 

# Making it available to all the interfaces
HOST = ''		
# Using any non-privileged port													 
PORT = 23000	
backlog = 5
receiveBuffer = 1024
threads = []

class ClientThread (Thread):
	def __init__(self,host,port):
		Thread.__init__(self)
		self.host = host 
		self.port = port
		print "New client connecting! Address is " + host + " Port is " + str(port) 

	def run (self):
		while True:
			data = clientSocket.recv (receiveBuffer)
			if not data:
				print "No data obtained from client"
			break
			clientSocket.send ("You are now connected to the server. ")
			clientSocket.send ("Message from server " + data)

try:
	serverSocket = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
	#REUSEADDR flag is set. This allows kernel to reuse a local socket in TIME_WAIT state 
	serverSocket.setsockopt (socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  
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
		clientSocket, (remoteHost, remotePort) = serverSocket.accept ()
		newThread = ClientThread (remoteHost,remotePort)
		newThread.start()
		threads.append (newThread)
	except socket.error, err:
		print "Error in connection " + err
  		sys.exit(1)

# Wait for the threads to execute
for t in threads:
	t.join()

