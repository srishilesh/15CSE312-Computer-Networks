import pandas as pd
import socket 

s = socket.socket()
port = 5003
host = socket.gethostname()
s.bind((host,port))
s.listen(3)
file = open("E:/Amrita University/Academics/3rd year 2019-20/6th Semester/Computer Networks/Lab/Lab 3/data.txt","r")
data = file.read()
print("Server Running ...")
while True:
    conn,addr = s.accept()
    print("Connected with ",addr)
    conn.send(data.encode("utf-8","ignore"))
conn.close()
