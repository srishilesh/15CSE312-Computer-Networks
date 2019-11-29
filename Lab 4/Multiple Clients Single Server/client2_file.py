import socket 
  
  
def main(): 
    
    host = '127.0.0.1'
    port = 5000
  
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
    s.connect((host,port)) 
    
    while True: 
        inp = input(" >> ")
        message = "From Client 2: "+inp
        
        s.send(message.encode('ascii')) 
  
        data = s.recv(1024) 
        print('Received from the server :',str(data.decode('ascii'))) 
  
        ans = input('\nDo you want to continue(y/n) :') 
        if ans == 'y': 
            continue
        else: 
            break
    #fin = s.recv(1024).decode()
    s.close() 
  
if __name__ == '__main__': 
    main() 
