import socket

DEFAULT_HOST = 'localhost'
DEFAULT_PORT = 50505
socket_object = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
stats = {'PUT'	:{'success':0, 'error':0}, 
		'GET'	:{'success':0, 'error':0}, 
		'DELETE':{'success':0, 'error':0}
		}
