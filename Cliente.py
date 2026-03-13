# Cliente
import socket

HOST = "127.0.0.1"
PORT = 9002

#cria o socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.conecct((HOST, PORT))
s.sendall(b"ola socket")
print(s.recv(1024).decode())

s.close()

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.connect((HOST, PORT))
#     s.sendall(b"ola socket")
#     print(s.recv(1024).decode())