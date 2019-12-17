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
