# Servidor
import socket

HOST = "0.0.0.0"
PORT = 9002

#cria o socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#solicita a porta ao SV
s.bind((HOST, PORT))
s.listen(1)

#Aguarda conexões
print ("Aguardando Cliente 1")
s.listen(1)
conn1, addr1 = s.accept()
print("Cliente:",(addr1))

print ("Aguardando Cliente 2")
s.listen(1)
conn2, addr2 = s.accept()
print("Cliente:",(addr2))

# data=conn.recv(1024)
# conn.sendall(b"OK: " + data)

conn1.close()
conn2.close()

s.close()




# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.bind((HOST, PORT))
#     s.listen(1)
#     conn, addr = s.accept()
#     with conn:
#         data = conn.recv(1024)
#         conn.sendall(b"OK: " + data)