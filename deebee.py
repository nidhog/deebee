# -*- coding: utf-8 -*-
"""
DeeBee
deebee module
 
@author: ielouafiq
"""

import sys
import socket

socket_object = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
stats = {'PUT'	:{'success':0, 'error':0}, 
		'GET'	:{'success':0, 'error':0}, 
		'DELETE':{'success':0, 'error':0}
		}

def main():
	pass
	
if __name__=="__main__":
	sys.exit(main())