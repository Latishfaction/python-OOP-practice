import socket
s = socket.socket()
print('Socket Created')
s.bind(('localhost', 9999))
s.listen(3)
print('Waiting for connection')

while True:
    c, addr = s.accept()
    print('Connected with', addr)
    c.send(bytes('You are Connected ', 'utf-8'))
    c.close()
