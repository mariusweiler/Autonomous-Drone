# -*- coding: utf-8 -*-
import socket

class socketFlightServer():
    def __init__(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(('172.20.10.7', 9052))
        self.server_socket.listen(1)  # allow only 1 connection
        self.connection, client_address = self.server_socket.accept()

    def waitHeightOk(self):
        self.heightOk=0;
  	while not self.heightOk:
   	    data = self.connection.recv(32)
   	    data = int(data.lstrip(' '));
            print('Hauteur reçue par mission controll :')
            print(data)
            if data < 85:
                self.heightOk=1;

    def getPersonPosition(self):
   	self.positionReceived=0;
  	while not self.positionReceived:
   	    data1 = self.connection.recv(32)
   	    data1=int(data1.lstrip(' '));
   	    data2 = self.connection.recv(32)
   	    data2=int(data2.lstrip(' '));
            self.positionReceived=1;
   	return data1,data2;

    def closeSocket():
        self.server_socket.close()
   	self.connection.close()

