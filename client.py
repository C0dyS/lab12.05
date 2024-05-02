#client

import socket


client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect(('127.0.0.1',8080))


while True:
    data = input('type:')
    client.send(data.encode())

    if data == 'exit' :
        break

    response = client.recv(1024).decode()
    print(response)

client.close()