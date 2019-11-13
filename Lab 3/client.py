import socket
import pandas as pd
s = socket.socket()
host = socket.gethostname()
port = 5003
s.connect((host,port))


source = s.recv(1024).decode("utf-8")
dest = s.recv(1024).decode("utf-8")
sent = s.recv(1024).decode()
receive = s.recv(1024).decode()
transmission = s.recv(1024).decode("utf-8")

# loss = int(sent) - int(receive)
# throughput = int(receive)/int(sent)
print("Source IP: ",source)
print("Destination IP: ",dest)
# print("Sent: ",sent)
# print("Packet Loss: ",loss)
# print("Throughput: ",throughput)
print("Number of transmissions: ",transmission)


# file = s.recv(1024).decode("utf-8")
# li = file.split("\n")
# for i in li:
#     string = li.split(" ")
#     source = string[0]
#     dest = string[1]
#     send = string[2]
#     receive = string[3]
#     transmission = string[3]
#     print(source," ",dest," ",send," ",receive)
    
# for i in range(3):
    # source = file["Source_IP"][i]
    # dest = file["Dest_IP"][i]
    # send = (file["Packets_sent"][i])
    # receive = (file["Packets_recv"][i])
    # transmission = file["Source_IP"].value_counts()
#     print(source," ",dest," ",send," ",receive)
s.close()

