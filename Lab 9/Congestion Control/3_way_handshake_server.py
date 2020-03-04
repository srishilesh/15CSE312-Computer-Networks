import socket
import random

s = socket.socket()
s.bind(('',3000))
s.listen(5)

while True:
    c,addr = s.accept()
    print('Connected with client',c)
    c.send(bytes("200","utf-8"))

    data1 = c.recv(1024).decode("utf-8")
    print("Data from client: ",data1)
    seg1 = data1.split()
    seg1[1] = 1
    seg1[2] = int(seg1[2]) + 1
    new_message1 = seg1[0]+" "+str(seg1[1])+" "+str(seg1[2])

    c.send(bytes(str(new_message1),"utf-8"))

    data2 = c.recv(1024).decode("utf-8")
    print("Data from client: ",data2)
    seg2 = data2.split()
    seg2[1] = 1
    seg2[2] = int(seg2[2]) + 1
    new_message2 = seg2[0]+" "+str(seg2[1])+" "+str(seg2[2])

    c.send(bytes(str(new_message2),"utf-8"))
    print("3 way Handshake established with client")
    print()
    
    print("Add more clients? Y/N")
    x = input()
    if(x=='y' or x=='Y'):
        continue
    else:
        break
