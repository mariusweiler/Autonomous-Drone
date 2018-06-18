import socket

class socketSendMissionControllData():
  def __init__(self):
    ## initialisation des variables et démarrage de la connexion
    self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.client_socket.connect(('172.20.10.7', 9052))
  ## methode d'envoi de la hauteur
  def sendHeight(self):
    val ='%32s' %getAltitude();
    self.client_socket.sendall(val);
## methode d'envoi de la position
  def sendXY(self,tab):
    ## si le tableau est vide on envoie 999999999 dans les deux valeurs
    if not len(tab):
      tt=999999999;
      val ='%32s' %tt;
      self.client_socket.sendall(val);
      self.client_socket.sendall(val);
    ## sinon on envoie les 2 valeurs du tableau soit xA et xB
    else:
      val ='%32s' %tab[0][0];
      self.client_socket.sendall(val);
      val ='%32s' %tab[0][2];
      self.client_socket.sendall(val);
  ## methode pour fermer la connexion
  def closeSocket(self):
    self.client_socket.close()
