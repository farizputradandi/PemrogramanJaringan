import socket
import os
import sys

save_path ='C:/Users/FARIZ PUTRA DANDI/Desktop/Tugas 2/Client 1'
# os.mkdir(save_path)
 
minta1="x"
UPLOAD="x"
#port
TARGET_IP = "127.0.0.1"
TARGET_PORT = 9000

command = sys.argv[1] 
mintafile = sys.argv[2] 
#socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((TARGET_IP, TARGET_PORT)) 

#sending signals to the server if the client is ready

if(command=="rq"):  
    minta1 = "MINTA" + mintafile

if(command=="up"):  
    minta1 = "UPLOD" + mintafile    
    UPLOAD=minta1[5:]
    sock.send(UPLOAD)

    fp = open(mintafile,'rb')
    k = fp.read()
    terkirim=0
    for x in k:
        sock.send(x) 
        print("terkirim")


    
# print(minta1)

# sock.send(str(minta1), (TARGET_IP, TARGET_PORT))
# sock.send(str(minta1), (TARGET_IP, TARGET_PORT))

sock.send(minta1)
# sock.send(TARGET_IP, TARGET_PORT)
counter = 1

 

def receiveImage():
    while True:
        data = sock.recv(1024) 
        print("ini data")
        print(data)
        if(data[0:5]=="START"):
            print "full data ",data
            file_name=os.path.join(save_path,data[5:])

            print "Menerima ",data[5:]
            fp = open(file_name,'wb+')
            ditulis = 0
        elif(data=="DONE"):
            fp.close()
        elif(data=="END"):
            break
        else:
            print "Blok ", len(data), data[0:10]
            fp.write(data)      
       
while True: 
    data = sock.recv(1024)  

    if(data=="SENDING"):
        print("ini sending")
        receiveImage()
        counter = 0 

    



       
    
             


