import socket
import time
import sys

# UDP_IP = "127.0.0.1"
UDP_IP=["127.0.0.1","127.0.0.2","127.0.0.3","127.0.0.4",];
UDP_PORT = 9000
buf = 1024
# file_name = sys.argv[1] 
# file_name=["lala.txt","lili.txt","lulu.txt"]; 
file_name=["kucing1.jpg","kucing2.jpg","kucing3.jpg","kucing4.jpg"];
# file_name=["kucing1.jpg"];
# print(file_name[0]);
for UDEP in UDP_IP: 
	for x in file_name: 
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

		sock.sendto(x, (UDEP, UDP_PORT))
		print "Sending %s ..." % x

		f = open(x, "rb")
		data = f.read()
		while(data):
		    if(sock.sendto(data, (UDEP, UDP_PORT))):
		        data = f.read()
		        # time.sleep(0.02) # Give receiver a bit time to save

		sock.close()
		f.close()
		time.sleep(10)