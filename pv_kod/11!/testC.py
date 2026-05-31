import socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('localhost',5000))

server.listen()
print('Server is listening ')
clinet,address = server.accept()

print("pripojil se",address)
data = clinet.recv(1024)
print(data.decode())
print('Ahoj kliente'.encode())