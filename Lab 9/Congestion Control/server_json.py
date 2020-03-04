import socket
import json

s = socket.socket()

s.bind(('',3000))
s.listen(5)

forward = dict()
ind = 0

while True:
    c, addr = s.accept()
    if(c not in forward.values()):
        forward[ind]=c
        ind+=1
    
    print("Connected to the client")
    print(c)
    
    c.send(bytes("200","utf-8"))
    
    msg = c.recv(1024).decode("utf-8")
    tcp = json.loads(msg)
    
    print("Recieved SYN packet from the client")
    print(tcp)
    
    tcp['ack']+=1
    tcp['seq']+=1
    
    print("Sending SYN-ACK packet ...")
    c.send(bytes(json.dumps(tcp),"utf-8"))
    
    msg = c.recv(1024).decode("utf-8")
    tcp = json.loads(msg)
    
    print("Recieved ACK packet from the client")
    print(tcp)
    
    print("Successful 3 - way handshake established!")
    
    print("Do you want to continue Y/N")
    x = input()
    if(x == 'y' or x == 'Y'):
        continue 
    else:
        break
    
    
    