import socket

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('localhost',9999))

server.listen(1)
client,address=server.accept()

done=False

while not done:
    message=client.recv(1024).decode('utf-8')

    if message=='quit':
        done=True
        break
    else:
        print(message)
        client.send(input('MESSAGE:').encode('utf-8'))

server.close()
client.close()