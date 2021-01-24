import socket
import threading
from _thread import *


printing_lock = threading.Lock()

s = socket.socket()

s.bind(('',1234))

def send_recv(c,addr):
    while True:
        data = c.recv(1024).decode()
        if not data:
            print("Bye")
            printing_lock.release()
            break
        print("From Client ",addr," : ",data)
        #conn.append(addr)
        inp = input(" -> ")
        c.send(str(inp).encode())
    c.close()

s.listen(5)
print("Server listening ... ")
conn = []
while True:
    c,addr = s.accept()
    printing_lock.acquire()
    print("Connect with ",addr)
    start_new_thread(send_recv,(c,addr))
s.close()

