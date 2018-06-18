# -*- coding: utf-8 -*-
## CLASSE DE TEST, VOIR CLASS FLIGHTCONTROLLER POUR DES COMMENTAIRES SUR LE CODE
## Permet de tester la connexion entre drone et l'echange de position de la personne detectée (999999999 si personne sur l image) les valeurs sont printées dans la console
from captormanagement import *
from buzzer import *
from flightcommand import *
import time
import cv2
from communicationManagement import socketCommManagement
from multiprocessing import Queue
from flightserver import *
tireffectuer=False;
lcdWrite('- Attente connexion drone -');
sfs=socketFlightServer();
laqueue=Queue();
scm=socketCommManagement(laqueue);
while not tireffectuer:
    lcdWrite('Recherche personne')    
    laqueue.put('1');
    xA,xB=sfs.getPersonPosition();
    print('les valeurs :');
    print(xA);
    print(xB);
