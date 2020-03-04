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
        print("Do you want to transfer data from the server?(Y/N)")
        x = input()
        print("Establishing connnection ... ")

        if(x == 'Y' or x == 'y'):
            r1 = random.randint(0,1000)
            tcp['seq'] = r1
            tcp['syn'] = 1
            msg = json.dumps(tcp)
            
            s.send(bytes(msg,"utf-8"))
            
            msg = s.recv(1024).decode("utf-8")
            
            tcp_ = json.loads(msg)
            if(tcp_['syn'] == 1 and tcp_['ack'] == 1 and tcp_['seq'] == tcp['seq']+1):
                print("Received packets from server")
                print(msg)
                print()
                tcp_['syn'] = 0
                tcp_['seq'] = random.randint(0,1000)
                print("Sending ACK packet ...")
                s.send(bytes(json.dumps(tcp_),"utf-8"))
                print("3-way handshake established with the server")
                
                print()
                print("Do you wish to access the database?(Y/N)")
                resp = input()
                if(resp=='N' or resp=='n'):
                    break
                else:
                    no = int(input("Number of data you wish to access: "))
                    s.send(bytes(str(no),"utf-8"))
                    window = int(input("Enter Window size: "))
                    s.send(bytes(str(window),"utf-8"))
                    for i in range(no):
                        print("Accessing data ",(i+1))
                        row = input("Enter the row number: ")
                        col = input("Enter the column number: ")
                        s.send(bytes(row,"utf-8"))
                        s.send(bytes(col,"utf-8"))

                        print("Data retrieved from the database: ",end="")
                        recv_data = str(s.recv(1024).decode("utf-8"))
                        if("None" in recv_data):
                            print(recv_data)
                            print()
                            continue
                        recv_data_len = len(str(recv_data))
                        i = 0
                        while i<recv_data_len:
                            print(recv_data[i:i+window])
                            i+=window
                        print()
                print("Total Round Trip Time is ",s.recv(1024).decode("utf-8")," seconds")
            else:
                print("Error!")
                
    break