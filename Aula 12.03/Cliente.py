# Cliente
import socket

HOST = "192.168.246.190"
PORT = 9003

#cria o socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((HOST, PORT))
s.sendall(b"ola socket")
print(s.recv(1024).decode())

s.close()

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.connect((HOST, PORT))
#     s.sendall(b"ola socket")
#     print(s.recv(1024).decode())