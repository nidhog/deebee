# -*- coding: utf-8 -*-
"""
DeeBee
deebee module
 
@author: ielouafiq
"""

import sys
import socket
import settings
from twisted.internet.protocol import Protocol 

socket_object = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# store success and failure statistics
stats = {
	'PUT'	:{'success':0, 'error':0}, 
	'GET'	:{'success':0, 'error':0}, 
	'DELETE':{'success':0, 'error':0}
	}

# handle basic commands: put, get and delete
commands = {
	'PUT': handle_put,
	'GET':handle_get,
	'DELETE':handle_delete,
	}
# store the data
data = {}

#TODO
class DeeBeeClient(Protocol):
	"""To implement later in a client-server model
	"""
	def __init__(self, deeProxy):
		"""
		"""
		self.clientProxy = deeProxy
	def connectionMade(self):
		"""
		"""
		self.clientProxy.connectionSuccess()
	def sendRequest(self, data):
		"""
		"""
		self.transport.write(data)
		
	def dataReceived(self, data):
		"""
		"""
		pass
		
	def connectionLost(self, reason):
		"""
		"""
		pass

#TODO
class DeeBeeServer(Protocol):
	"""To implement later in a client-server model
	"""
	#
	def __init__(self, mode):
		"""
		"""
		self.mode = mode
	#
	def dataRecevied(self, data):
		"""
		"""
		self.transport.write(data)
		
def parse_message(data):
	return 0, 0, 0
def update_stats(command, success):
    """Update the statistics dictionnary
    """
    if success:
        STATS[command]['success'] += 1
    else:
        STATS[command]['error'] += 1


def handle_put(key, value):
    return (True, 0)

def handle_get(key):
    return (True, 0)
    
def handle_delete(key):
    return (True, 0)
    
def main():
	#TODO :: Go Twisted instead of socket
	SOCKET.bind((settings.DEFAULT_HOST, settings.DEFAULT_PORT))
	SOCKET.listen()
	while 1:
		connection, address = SOCKET.accept()
		data = connection.recv(4096).decode()
		command, key, value = parse_message(data)
		if command in commands.keys():
			if command == 'PUT':
				response = commands[command](key, value)
			else:
				response = commands[command](key)
		else:
			response = (False, 'Command not handled : '+ format(command))
		connection.sendall('{};{}'.format(response[0], response[1]))
		connection.close()
	pass
	
if __name__=="__main__":
	sys.exit(main())