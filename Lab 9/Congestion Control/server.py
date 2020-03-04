import socket
import json
import pandas as pd
import numpy as np

data = pd.read_csv("E:/Amrita University/Academics/3rd year 2019-20/6th Semester/Computer Networks/Lab/Lab 9/data.csv") # Read data from the file
data_flag = np.zeros((5,4))     # Checksum flags 

# Timing for each operation 
open_time = 3
close_time = 3
req_time = 1
flag_time = 1
rtt = open_time + close_time

s = socket.socket() # Create socket

s.bind(('',3000))   # Bind socket
s.listen(5)         # Listen socket connection


while True:
    c, addr = s.accept()        # Accept the connection
    
    print("Connected to the client")
    print(c)
    
    c.send(bytes("200","utf-8"))
    
    msg = c.recv(1024).decode("utf-8")
    tcp = json.loads(msg)
    
    print("Received SYN packet from the client")
    print(tcp)
    print()
    
    tcp['ack']+=1
    tcp['seq']+=1
    rtt+=flag_time
    
    print("Sending SYN-ACK packet ...")
    c.send(bytes(json.dumps(tcp),"utf-8"))
    
    msg = c.recv(1024).decode("utf-8")
    tcp = json.loads(msg)
    
    print("Received ACK packet from the client")
    print(tcp)
    print()
    rtt+=flag_time
    
    print("3-way handshake established with the client")
    
    no = int(c.recv(1024).decode("utf-8"))
    window = int(c.recv(1024).decode("utf-8"))

    temp_rtt = rtt
    for i in range(no):
        row = int(c.recv(1024).decode("utf-8"))
        col = int(c.recv(1024).decode("utf-8"))
        if(data_flag[row][col]==0):
            if(row>0 and row<6 and col>=0 and col<=3):
                info = data.iloc[row-1][col-1]
                c.send(bytes(str(info),"utf-8"))
                data_flag[row][col] = 1
            else:
                c.send(bytes("Data not found","utf-8"))
        else:
            msg = "None: Data already accessed (Failure condition)"
            c.send(bytes(msg,"utf-8"))
        temp_rtt+=req_time
    c.send(bytes(str(rtt),"utf-8"))


    print("Do you want to continue? (Y/N)")
    x = input()
    if(x == 'y' or x == 'Y'):
        continue 
    else:
        break
    
    
    