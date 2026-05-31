import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('localhost',5000))
client.send('Ahoj servere'.encode())
data = client.recv(1024)
print(data.decode())
client.close()