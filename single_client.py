# import socket

# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# s.connect(('127.0.0.1',12345))

# print(s.recv(1024).decode())

# s.close()

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

