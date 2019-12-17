import socket

s = socket.socket()

s.connect(('127.0.0.1',1234))
inp = input(" -> ")

while inp.lower().strip() != 'bye':
    s.send(str(inp).encode())
    data = s.recv(1024).decode()
    print("From server: ",data)
    inp = input(" -> ")
s.close()
