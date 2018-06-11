import socket

import threading

import Queue

class socketCommManagement():
  def __init__(self,laqueue):
    self.laqueue=laqueue;
    
  def start():
    self.stop=0;
    self.queue = laqueue;
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind('dex02.local', 9060)
    server_socket.listen(1)
    connection, client_address = server_socket.accept()
    self.sendHeight=0;
    self.lastSend=0;
    while not stop:
      self.sendHeight=queue.get();
      if queue:
        if self.sendHeight==0:
          server_socket.sendall('0');
        elif self.sendHeight==1:
          server_socket.sendall('1');
        elif self.sendHeight==2:
          self.stop=1;
        self.lastSend=self.sendHeight;
      else:
        if self.lastSend==0:
          server_socket.sendall('0');
        elif self.lastSend==1:
          server_socket.sendall('1');
    server_socket.close();
    connection.close();

