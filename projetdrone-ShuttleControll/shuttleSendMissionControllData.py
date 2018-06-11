import socket

from shuttleCaptormanagement import *

class socketCommManagement(self,laqueue):
  def __init__(self):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('weilerpi.local', 9051))

  def sendHeight(self):
    val ='%16s' %getAltitude();
    client_socket.sendall(val);

  def sendXY(self,tab):
    val ='%16s' %tab();
    client_socket.sendall(val);

  def closeSocket():
  	client_socket.close()
