# -*- coding: utf-8 -*-

# import de la fonction permettant de detecter une personne
# et de renvoyer ses coordonnées
from shuttlePersondetection import persondetection
# import des fonctions pour la gestion des capteurs
from shuttleCaptorManagement import *

from shuttleSendMissionControllData import *

# import des fonctions de temps pour faire des pauses
import time
# import des fonctions d'open cv
import cv2

from shuttleCommManagement import *

from multiprocessing import Queue

from picamera.array import PiRGBArray
from picamera import PiCamera

# initialisations en début de script



laqueue=Queue();
ssmcd=socketSendMissionControllData(laqueue);
time.sleep(3);
scm=socketCommManagement();



stop = 0;

# initialisation de la camera
camera = PiCamera()
rawCapture = PiRGBArray(camera)

while not stop:
    wts=scm.whatToSend();
##  on nettoie ce que lon a recu
    wts=wts.lstrip(' ');
    wts=int(wts)
    if wts == 0:
        ssmcd.sendHeight();
    elif wts==1:
        print('okokok');
        camera.capture(rawCapture, format="bgr")
        image = rawCapture.array
        tab=persondetection(image);
        print('tab');
        print(tab);
        ssmcd.sendXY(tab);
        rawCapture.truncate()
        rawCapture.seek(0)
    elif wts==2:
        self.stop=1;

