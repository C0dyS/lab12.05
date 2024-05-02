#client

import socket


client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect(('127.0.0.1',8080))

country = input("Enter the country: ")
city = input("Enter the city: ")


data = f"{country},{city}"
client.send(data.encode())


response = client.recv(1024).decode()
print(response)

client.close()