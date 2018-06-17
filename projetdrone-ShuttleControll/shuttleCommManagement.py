import socket

import threading

class socketCommManagement():
  def __init__(self):
    self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.client_socket.connect(('weilerpi.local', 9051))

  def whatToSend(self):
    data = self.client_socket.recv(32)
    return data;

  def closeSocket(self):
    self.client_socket.close()
