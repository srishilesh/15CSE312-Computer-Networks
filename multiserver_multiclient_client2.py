import socket

print("Server 1: 1234\nServer 2: 2345")
port = int(input())
s = socket.socket()
s.connect(('127.0.0.1',port))
inp = input(" -> ")
while True:
    s.send(str(inp).encode())
    data = s.recv(1024).decode()
    print("From Server: ",data)
    inp = input(" -> ")
    ans = input('\nDo you want to continue(y/n) :') 
    if ans == 'y': 
        continue
    else: 
        break
s.close()
