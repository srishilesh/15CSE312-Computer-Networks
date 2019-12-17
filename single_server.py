# import socket 
# import sys

# s = socket.socket()
# hostname = '127.0.0.1'
# port = 12345

# s.bind(('',port))

# s.listen(5)
# print("Socket is listening")

# while True:
#     c,addr = s.accept()
#     print("Connected with ",addr)
#     c.send(str("Thanks for connectin").encode())
#     c.close()


import socket

s = socket.socket()

s.bind(('',1234))

s.listen(5)
print('Chatroom is started')
c,addr = s.accept()
print("Connected from ",addr)

while(True):
    data = c.recv(1024).decode()
    if not data:
        break
    print("From Client: ",data)
    inp = input(" -> ")
    c.send(str(inp).encode())
c.close()
