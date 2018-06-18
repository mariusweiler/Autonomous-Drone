import socket
import threading

class socketCommManagement():
## initialisation des variables et démarrage de la connexion
  def __init__(self):
    self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.client_socket.connect(('weilerpi.local', 9051))
## permet de recevoir ce qui est demandé par mission controll
  def whatToSend(self):
    data = self.client_socket.recv(32)
    return data;
## fermer la connexion
  def closeSocket(self):
    self.client_socket.close()
