import socket

#Create socket 
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1', 5000))                                         
s.listen()
#Accept connection
conn,addr = s.accept()
#Receive name of client
name = conn.recv(1024).decode("utf-8")
print(name + ' '+ 'is now' +' '+ 'connected')
while True :
    #Receive command 
    command = conn.recv(1024).decode(("utf-8"))
    #Check the command and send correct response 
    if command == 'ping':
        conn.send('pong'.encode("utf-8"))
    elif command == 'hello server':
        conn.send(f'hello {name}'.encode("utf-8"))
    else :
        conn.send(name.encode("utf-8")) 
    