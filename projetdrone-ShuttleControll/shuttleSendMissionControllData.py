import socket

from shuttleCaptorManagement import *

class socketSendMissionControllData():
  def __init__(self,laqueue):
    self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.client_socket.connect(('172.20.10.7', 9052))

  def sendHeight(self):
    val ='%32s' %getAltitude();
##    print('shuttle envoie val :')
##    print(val)
    self.client_socket.sendall(val);

  def sendXY(self,tab):
    
    if not len(tab):
      tt=999999999;
      val ='%32s' %tt;
      self.client_socket.sendall(val);
      self.client_socket.sendall(val);
    else:
      val ='%32s' %tab[0][0];
      print('shuttle envoie x :')
      print(val)
      self.client_socket.sendall(val);
      val ='%32s' %tab[0][2];
      print('shuttle envoie y :')
      print(val)
      self.client_socket.sendall(val);

  def closeSocket(self):
    self.client_socket.close()
