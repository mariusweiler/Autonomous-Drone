import socket

from shuttleCaptorManagement import *

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('weilerpi.local', 9051))
i=1;

val ='%16s' %getAltitude();
client_socket.sendall(val);
client_socket.sendall(val);
client_socket.sendall(val);
client_socket.sendall(val);
client_socket.sendall(val);


