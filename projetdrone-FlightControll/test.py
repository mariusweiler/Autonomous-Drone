import socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('172.20.10.6', 9051))
server_socket.listen(1)  # allow only 1 connection
connection, client_address = server_socket.accept()
client_socket, client_address = server_socket.accept()

print(client_address, "has connected")
while 1==1:
    recvieved_data = client_socket.recv(16)
    print(recvieved_data)
