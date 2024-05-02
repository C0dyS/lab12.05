#server

import json
import socket

server = socket.socket(socket.AF_INET,
                       socket.SOCK_STREAM
                       )

server.bind(('127.0.0.1',8080))
server.listen(1)

with open(r'C:\pyProj\lab12.05\weather_2.json', 'r') as file:
    weather_data = json.load(file)
with open(r'C:\pyProj\lab12.05\cities_2.json', 'r') as file:
    cities_data = json.load(file)

while True:
    print('waiting')





    client,address = server.accept()
    print(f'{address} connected')
    while True:
        data = client.recv(1024).decode()
        print(data)
        country, city = data.split(',')
        if country in cities_data:
            if city in cities_data[country]:
                response = weather_data.get(city, 'Weather data not found')
                client.send(response.encode())

        else:
            response = 'no such city found'
            client.send(response.encode())

        if data == 'exit' :
            break



    client.close()
