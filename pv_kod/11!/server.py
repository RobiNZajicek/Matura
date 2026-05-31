import socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('localhost',5000))
server.listen()
print('Server posloucha')
client,adress = server.accept()
print("Ahoj",adress)
data = client.recv(1024)
print(data.decode())
client.send('Ahoj Kliente'.encode())
server.close()