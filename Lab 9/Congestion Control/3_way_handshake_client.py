import socket
import random

s = socket.socket()
s.connect(('127.0.0.1',3000))

while True:
    con = s.recv(1024).decode("utf-8")
    if(con=="200"):
        print("Connected to Server")
        print("Do you wish to transfer data with the server(Y/N): ")
        response = input()
        if(response=='Y'):
            r = random.randint(0,1000)
            segment = "1 0 "+str(r)
            s.send(bytes(str(segment),"utf-8"))

            print("Acknowledged message from server",s.recv(1024).decode("utf-8"))

            r = random.randint(0,1000)
            segment = "1 0 "+str(r)
            s.send(bytes(str(segment),"utf-8"))

            print()
            print("Acknowledged message from server",s.recv(1024).decode("utf-8"))
            
            print()
            print("3 way handshake established with server")
            break




