'''
Syntax: 's = socket.socket (socket_family, socket_type, protocol=0)'



'''
import socket
s = socket.socket()
host = socket.gethostname()
port = 22
s.bind((host, 22))
s.listen(5)
while True:
    c, addr = s.accept()
    print('Connection to', addr)
    c.send('root')
    c.send('MixedVc')
    c.close()


