import socket

port = 20001
buffer = 1024

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.bind(('',port))

#s.listen(5)
print("UDP Server listening ... ")

while True:
    bytesAddPair = s.recvfrom(buffer)
    message = bytesAddPair[0]
    address = bytesAddPair[1]
    clientMsg = "Message from Client:{}".format(message)
    clientIP  = "Client IP Address:{}".format(address)
    
    print(clientMsg)
    print(clientIP)

    s.sendto(str("Hello UDP Client").encode(),address)
