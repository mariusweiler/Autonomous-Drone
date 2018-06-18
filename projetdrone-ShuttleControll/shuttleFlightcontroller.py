# -*- coding: utf-8 -*-
# import de la fonction permettant de detecter une personne
# et de renvoyer ses coordonnées
from shuttlePersondetection import persondetection
# import des fonctions pour la gestion des capteurs
from shuttleCaptorManagement import *
# impor de la class pour envoyer des donnes a mission control
from shuttleSendMissionControllData import *
# import des fonctions de temps pour faire des pauses
import time
# import des fonctions d'open cv
import cv2
# import de la class pour recevoir les infos de mission control
from shuttleCommManagement import *
# import de la class queue
from multiprocessing import Queue
# imports pour la camera
from picamera.array import PiRGBArray
from picamera import PiCamera
# initialisations en début de script
## On créer une connexion pour envoyer des données puis on attend quelques secondes que mission control créer l'autre connexion de réception puis on s'y connecte également
ssmcd=socketSendMissionControllData();
time.sleep(3);
scm=socketCommManagement();
stop = 0;
# initialisation de la camera
camera = PiCamera()
rawCapture = PiRGBArray(camera)
while not stop:
    ## on regarde ce que mission control demande
    wts=scm.whatToSend();
    ##  on nettoie ce que lon a recu
    wts=wts.lstrip(' ');
    wts=int(wts)
    ## si mission control demande la hauteur
    if wts == 0:
        ssmcd.sendHeight();
    ## sinon s'ils demande la position
    elif wts==1:
        ## on capture une image
        camera.capture(rawCapture, format="bgr")
        image = rawCapture.array;
        ## on demande le tableau de position a la fonction de reconnaissance
        tab=persondetection(image);
        ## on envoie les données a mission control
        ssmcd.sendXY(tab);
        ## on remet la camera a zero
        rawCapture.truncate()
        rawCapture.seek(0)
    ## sinon s'ils demande de tirer
    elif wts==2:
        ## on active le relay pour tirer
        activatePistol()
    ## sinon s'ils demandent d'arrêter
    elif wts==3:
        self.stop=1;
        ## on ferme le socket de reception
        scm.closeSocket();


