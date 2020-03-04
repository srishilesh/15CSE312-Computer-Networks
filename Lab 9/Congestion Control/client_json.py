import socket
import json
import random
s = socket.socket()
s.connect(('127.0.0.1',3000))

tcp = {'syn':0, 'ack':0, 'seq':0 }
while True:
    conf = s.recv(1024).decode("utf-8")
    
    if(conf == "200"):
        print("Connected to the Server")
        print("Do you want to request for some data form the server? Y/N")
        x = input()
        
        if(x == 'Y' or x == 'y'):
            r1 = random.randint(0,1000)
            tcp['seq'] = r1
            tcp['syn'] = 1
            msg = json.dumps(tcp)
            
            s.send(bytes(msg,"utf-8"))
            
            msg = s.recv(1024).decode("utf-8")
            
            tcp_ = json.loads(msg)
            if(tcp_['syn'] == 1 and tcp_['ack'] == 1 and tcp_['seq'] == tcp['seq']+1):
                print("Recieved Appriopriate headers")
                print(msg)
                tcp_['syn'] = 0
                tcp_['seq'] = random.randint(0,1000)
                print("Sending ACK packet ...")
                s.send(bytes(json.dumps(tcp_),"utf-8"))
                print("3 - way handshake established with the server")
                
            else:
                print("Error!")
                
    break