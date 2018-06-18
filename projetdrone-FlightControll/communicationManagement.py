# -*- coding: utf-8 -*-
import socket
import threading
import Queue
import time
class socketCommManagement(threading.Thread):
  ## initialisation des variables et démarrage du thread
  def __init__(self,laqueue):
    self.laqueue=laqueue;
    super(socketCommManagement,self).__init__();
    thread=threading.Thread(target=self.run,args=())
    thread.start();
  ## méthode qui se lance au demarrage du thread
  def run(self):
    ## initialisation des variables pour lancer le socket puis démarrage du socket (du canal de communication))
    self.stop=0;
    self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.server_socket.bind(('172.20.10.7', 9051))
    self.server_socket.listen(1)
    self.connection, client_address = self.server_socket.accept()
    ## tant que l'on ne demande pas d'arrêter
    while not self.stop:
      ## si la queue n'est pas vide
      if not self.laqueue.qsize() == 0:
        ## on reprend la valeur de la queue
        valll=self.laqueue.get();
        self.sendHeight=int(valll)
        ## si la valeur est 0 ou 1 ou 2, on envoie 0 ou 1 ou 2 pour demander la hauteur au drone
        if self.sendHeight==0 or self.sendHeight==1 or self.sendHeight==2:
          val = '%32s' %self.sendHeight;
          self.connection.sendall(val);
        elif self.sendHeight==3:
          ## on arrête d envoyer en sortant de cette boucle
          self.stop=1;
    ## on ferme la connexion
    self.server_socket.close();
    self.connection.close();
