# The program is intented to get used familarised with the sockets. 
# The server here implements multi threading. Multiple clients connect to the server. The server handles 
# each client in a new thread. It simply echoes back message to the client.
# Author:  Rohit P. Tahiliani


import socket
from threading import Thread  
import sys 

# Making it available to all the interfaces
HOST = ''		
# Using any non-privileged port	if the port is not specified												 
if len(sys.argv) > 1:
	PORT = int(sys.argv[1])
else:	
	PORT = 23000	

backlog = 5
receiveBuffer = 1024
threads = []

class ClientThread (Thread):
	def __init__(self,clientSocket,host,port):
		Thread.__init__(self)
		self.host = host 
		self.port = port
		self.clientSocket = clientSocket
		print "[+] New client connecting! Address is " + host + " Port is " + str(port) 

	def run (self):
		while True:
			data = clientSocket.recv (receiveBuffer)
			data = self.handleMessages(data)
			self.clientSocket.sendall (data)
			self.clientSocket.close ()
			break

	def handleMessages(self,data):
		if data[:4] == "HELO":
			return data + "\n" + "IP:" + str(self.host) + "\n" + "Port:" + str(self.port)
		elif data == "KILL_SERVER": 
			serverSocket.close ()
			return "Killing the server"
		else:
			return "Disconnecting."

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
		print "[+] Waiting for the incoming connections..."
		clientSocket, (remoteHost, remotePort) = serverSocket.accept ()
		newThread = ClientThread (clientSocket,remoteHost,remotePort)
		newThread.start()
		threads.append (newThread)
	except KeyboardInterrupt:
		serverSocket.close ()
		print "[-] Server shutting down..."
  		sys.exit()

# Wait for the threads to execute
for t in threads:
	t.join()