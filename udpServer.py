import socket
import os
port=8800
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('',port))
print('Waiting for command...')
while True:
    path='/applications/'
    command,_=s.recvfrom(1024)
    app=command.decode()+'.app'
    path+=app
    os.system('open '+path)
    