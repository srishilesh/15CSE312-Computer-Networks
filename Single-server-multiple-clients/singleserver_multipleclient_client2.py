import socket

s = socket.socket()
s.connect(('127.0.0.1',12345))
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
