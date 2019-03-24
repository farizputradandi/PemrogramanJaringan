import socket
import time
import sys

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
buf = 1024
# file_name = sys.argv[1] 
# file_name=["lala.txt","lili.txt","lulu.txt"]; 
file_name=["kucing1.jpg","kucing2.jpg","kucing3.jpg","kucing4.jpg"];
# print(file_name[0]);

for x in file_name: 
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	sock.sendto(x, (UDP_IP, UDP_PORT))
	print "Sending %s ..." % x

	f = open(x, "rb")
	data = f.read()
	while(data):
	    if(sock.sendto(data, (UDP_IP, UDP_PORT))):
	        data = f.read()
	        # time.sleep(0.02) # Give receiver a bit time to save

	sock.close()
	f.close()
	time.sleep(10)