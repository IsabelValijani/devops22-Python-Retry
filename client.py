import socket 

#create socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#Connecting to the same IP as server.
s.connect(('127.0.0.1', 5000))
#Get name and sending it to server 
name = str(input('Enter your name:'))
s.send(name.encode())
#list of commands
commands = ['ping', 'who am i', 'hello server']
#Checking if the commands are present in the list 
while True :
    command = str(input('Enter the command:'))
    if command in commands :
        #If command is present , then send it 
        s.send(command.encode())
    else :
         #If its NOT ask again 
         continue
    #Recieving and printing response
    response = s.recv(1024).decode()
    print(response)
