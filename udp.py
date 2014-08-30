import thread
import time
import socket
from sys import argv

myId = argv[1]


def fn_client(args):
	udpIP = '127.0.0.1'
	udpPort = args
	mssg = "Hi!!!"
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.sendto(mssg, (udpIP,udpPort))

def fn_server(args):
	udpIP = '127.0.0.1'
        udpPort = args
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.bind((udpIP, udpPort))
	while True:
		data, addr = sock.recvfrom(1024)
		print "Received: ", data
	
#if __name__=='__main__':
    				
try:
	thread.start_new_thread(fn_client, (myId,))
        thread.start_new_thread(fn_server, (myId,))
except :
        print "error"

while 1:
	pass
