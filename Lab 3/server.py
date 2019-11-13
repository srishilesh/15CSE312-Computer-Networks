import pandas as pd
import socket 

s = socket.socket()
port = 5003
host = socket.gethostname()
s.bind((host,port))
s.listen(5)
file = pd.read_csv("Y:/6th sem/Networking/Lab 2/data.txt")

print("Server Running ...")
conn,addr = s.accept()
print("Connected at ",addr)
for i in range(file.shape[0]):
    source = file["Source_IP"][i]
    dest = file["Dest_IP"][i]
    send = (file["Packets_sent"][i])
    receive = (file["Packets_recv"][i])
    transmission = file["Source_IP"].value_counts()
    #print(source," ",dest," ",send," ",receive)
    #print(file["Source_IP"].value_counts())
   
    conn.send(bytes(source,"utf-8"))
    conn.send(bytes(dest,"utf-8"))
    conn.send(bytes(send))
    conn.send(bytes(receive))
    conn.send(bytes(transmission))
# # print(file)
# conn.send(bytes(file))

conn.close()
