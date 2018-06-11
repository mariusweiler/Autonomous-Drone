import socket

import threading

class socketSendMissionControllData():
  client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  client_socket.connect('weilerpi.local', 9050)
  self.stop=0;

  def whatToSend(self):
    data = client_socket.recv(1024)
    return data;

  def closeSocket():
    client_socket.close()