import socket
import pandas as pd
s = socket.socket()
host = socket.gethostname()
port = 5003
s.connect((host,port))
i=0

print("Received: ")
fromip = []
toip = []
sentpack = []
recvpack = []
data = s.recv(1024).decode("utf-8")
data = data.split("\n")
length = len(data)
for i in range(1,len(data)):
    data[i] = data[i].split(",")
    fromip.append(data[i][0])
    toip.append(data[i][1])
    sentpack.append(data[i][2])
    recvpack.append(data[i][3])

print("from ip \t to ip \t packet loss")
filewr = "from ip \t to ip \t packet loss \n"
for i in range(0,length-1):
    filewr+=str(fromip[i])+" \t "+str(toip[i])+" \t "+str(int(recvpack[i])-int(sentpack[i]))+"\n"
    print(str(fromip[i])," \t ",str(toip[i])," \t ",str(int(recvpack[i])-int(sentpack[i])))


print("\nNumber of Transmission")
filewr+="\nNumber of Transmission\n"
for i in set(fromip):
    filewr+=str(i)+"\t"+str(fromip.count(i))+"\n"
    print(i,"\t",fromip.count(i))

print("Throughput ")

file = open('written.txt','w')
file.write(filewr)

s.close()



