import socket, sys, random, select, time
from check import ip_checksum

HOST = ''
PORT = 8888

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	print 'Socket Created'
except socket.error, msg:
	print 'failed to create socket. Error Code : '+ str(msg[0]) + ' Message ' + msg[1]
	sys.exit()

try:
	s.bind((HOST,PORT))
except socket.error, msg:
	print 'Bind Failed. Error Code : ' + str(msg[0]) + ' Message ' + msg([1])
	sys.exit()

print 'Socket bind complete.'

