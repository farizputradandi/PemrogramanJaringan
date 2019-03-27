from threading import Thread
import socket
import os

#setting IP and port
TARGET_IP = '127.0.0.1'
TARGET_PORT = 9000

#setting socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((TARGET_IP, TARGET_PORT))
sock.listen(1)
conn,addr=sock.accept()

namafile=["Readme.md"]

#setting nama file gambar
# namafile = ["Readme.md"]

#fungsi buat ngirim gambar
def sendImage(trg_ip, trg_port):
    print("ini namafile2")
    print(namafile)
    print(namafile[0])
    print("ini end file")

    # sock.send("SENDING", (trg_ip, trg_port)) 
    conn.send("SENDING")
     
    for i in namafile:
        #beritahu nama file yang dikirim
        conn.send("START {}" . format(i))
        ukuran = os.stat(i).st_size
        fp = open(i,'rb')
        k = fp.read()
        terkirim=0
        for x in k:
            conn.send(x)
            terkirim = terkirim + 1
            print "\r Terkirim {} of {} " . format(terkirim,ukuran)
        conn.send("DONE")
        fp.close()
    conn.send("END")


def receiveImage(trg_ip, trg_port):
    print("asdflkjas;ldkfjasl;kdfj")
    while True:
        data = sock.recv(1024) 
        print("ampass")
        print(data)
        fp = open(file_name,'wb+')
        fp.write(data)  
        fp.close()
        
                

while True:
    # print "Menunggu koneksi dari client..." 
    data = conn.recv(1024) 
    # print("data diterima server");
    # print(data);

 
    #signal from client
    if (data[:5]=="MINTA"): 
        minta = data[5:]
        print(data[:5]);
        print(minta);

        namafile[0] = minta
        print("ini namafile1 ")
        print(namafile[0])
        # sendImage()
        thread = Thread(target = sendImage, args = (addr))
        thread.start()
    
    if (data[:5]=="UPLOD"): 
        print("ini sending") 
        # receiveImage();
        thread1 = Thread(target = receiveImage, args = (addr))
        thread1.start()
