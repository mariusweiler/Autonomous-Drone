# -*- coding: utf-8 -*-
import socket

class socketFlightServer():
    ## fonction qui se lance au demarrage du thread
    def __init__(self):
        ## initialisation des variables et démarrage du thread
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(('172.20.10.7', 9052))
        self.server_socket.listen(1)  # allow only 1 connection
        self.connection, client_address = self.server_socket.accept()
    ## fonction qui attend que la hauteur soit ok pour se terminer
    def waitHeightOk(self):
      self.heightOk=0;
      ## tant que la hauteur n'est pas ok
      while not self.heightOk:
        ## on recoit la valeur de hauteur codée sur 32 bits
   	    data = self.connection.recv(32)
        ## on enlève les espace de debut dûs au 32 bits et l'on transforme la valeur string en int
   	    data = int(data.lstrip(' '));
        ## si la hauteur est plus grande que 100 on arrête la boucle on est assez haut (nécessite une montée en douceur pour que l'échange d'information ait le temps de se faire et que le drone ne monte pas trop pendant ce temps) 
        if data > 100:
          self.heightOk=1;
    ## fonction recevant les valeurs de position xA et xB de la personne detectée sur l'image
    def getPersonPosition(self):
   	self.positionReceived=0;
  	while not self.positionReceived:
      ## on recoit les 2 positions et on les nettoie de leur espaces au debut dus au 32 bits puis on ferme la boucle en changeant le boolean
   	  data1 = self.connection.recv(32)
   	  data1=int(data1.lstrip(' '));
   	  data2 = self.connection.recv(32)
   	  data2=int(data2.lstrip(' '));
      self.positionReceived=1;
    ## on retourne les 2 valeurs
   	return data1,data2;

## methode qui ferme la connexion
    def closeSocket():
      self.server_socket.close()
   	  self.connection.close()

