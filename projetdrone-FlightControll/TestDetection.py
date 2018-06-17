# -*- coding: utf-8 -*-

# import des fonctions pour la gestion des capteurs
from captormanagement import *
# import de la fonction pour faire gerer le buzzer
from buzzer import *
# import des fonctions de controle de vol pour le drone
from flightcommand import *
# import des fonctions de temps pour faire des pauses
import time
# import des fonctions d'open cv
import cv2

from communicationManagement import socketCommManagement

from multiprocessing import Queue


from flightserver import *
# Declaration des variables du script
## Variable permettant de savoir si on a déjà tiré.
tireffectuer=False;
## variable permettant de connaitre la position du milieu de l'image pour aligner la cible
valeurmillieu=206;
## variable permettant de savoir si l'atterrissage a été effectué
atterrissageok=0;
## variable gardant les commandes de vol
fc = flightcommand();
# initialisations en début de script
## initialisation du buzzer
initialisebuzzer();

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
