import pandas as pd
import socket
from _thread import *
import threading
import random
import string

print_lock = threading.Lock()

def randomString(stringLength=5):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def createData(n_rows,n_cols):
    data = []
    for i in range(n_rows):
        #for j in range(n_cols):
        li = []
        a = int(input("Enter the type of data: "))
        b = input("Enter the data: ")
        li.append(a)
        li.append(b)
        data.append(li)
    return data

def threaded(c,addr,fin,n_data):
    x = 0
    y = n_data+1
    while True:
        data = c.recv(1024)
        print(str(data.decode()))
        if not data:
            print('DISCONNECTED FROM THE CLIENT')
            print_lock.release()
            break
        
        #data = open("E:/Amrita University/Academics/3rd year 2019-20/6th Semester/Computer Networks/Lab/Lab 3/data.txt","r")
        #data = "To Client "+ str(addr[1])
        data = fin[x:y]
        x = y
        y = y+n_data
        c.send(str(data).encode())
    c.close()

def main():
    print("SERVER INITIALIZATION")
    print("--------------------------------")
    n_clients = int(input("Enter the Number of Clients: "))
    n_cols = int(input("Enter the Number of Columns: "))
    n_rows = int(input("Enter the Number of Rows: "))

    print("0:char \n1:int \n2:string \n3:bool \n4:float ")
    data = createData(n_rows,n_cols)

    n_data = int(n_rows/n_clients)
    s = socket.socket()
    port = 5000
    host = ""
    # host = socket.gethostbyname()
    s.bind((host,port))
    s.listen(5)
    conn = []
    # data = pd.read_csv("E:/Amrita University/Academics/3rd year 2019-20/6th Semester/Computer Networks/Lab/Lab 4/data.csv")
    print("SERVER RUNNING .... ")
    x = 0
    y = n_data+1
    while True:
        c,addr = s.accept()
        print_lock.acquire()
        conn.append(c)
        print('Connected to :', addr[0], ':', addr[1]) 
        
        start_new_thread(threaded, (c,addr,data,n_data)) 

        
     c.close()
    

if __name__=='__main__':
    main()
