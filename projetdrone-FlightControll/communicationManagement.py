# -*- coding: utf-8 -*-
import socket

import threading

import Queue

import time

class socketCommManagement(threading.Thread):
  def __init__(self,laqueue):
    self.laqueue=laqueue;
    super(socketCommManagement,self).__init__();
    thread=threading.Thread(target=self.run,args=())
    thread.start();
    
    
  def run(self):
    self.stop=0;
    self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.server_socket.bind(('172.20.10.7', 9051))
    self.server_socket.listen(1)
    self.connection, client_address = self.server_socket.accept()
    self.sendHeight=0;
    while not self.stop:
      if not self.laqueue.qsize() == 0:
        valll=self.laqueue.get();
        self.sendHeight=int(valll)
        if self.sendHeight==0 or self.sendHeight==1:
          val = '%32s' %self.sendHeight;
          self.connection.sendall(val);
        elif self.sendHeight==2:
          self.stop=1;
          print('pas ok frerr')
    self.server_socket.close();
    self.connection.close();

    def stop():
      print('0');
