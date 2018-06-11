# -*- coding: utf-8 -*-

# import de la fonction permettant de detecter une personne
# et de renvoyer ses coordonnées
from shuttlePersondetection import persondetection
# import des fonctions pour la gestion des capteurs
from shuttleCaptormanagement import *

from socketSendMissionControllData import *
# import de la fonction pour faire gerer le buzzer
from buzzer import *
# import des fonctions de controle de vol pour le drone
from flightcommand import *
# import des fonctions de temps pour faire des pauses
import time
# import des fonctions d'open cv
import cv2

from shuttleCommManagement import *

import Queue


from flightserver import *

# initialisations en début de script
scm=shuttleCommManagement();
laqueue=Queue();
ssmcd=socketSendMissionControllData(laqueue);
scm.start();
stop = 0;

# initialisation de la camera
camera = PiCamera()
rawCapture = PiRGBArray(camera)

while not stop:
    wts=scm.whatToSend();
    if wts == 0:
        ssmcd.sendHeight();
    elif wts==1:
        camera.capture(rawCapture, format="bgr")
        image = rawCapture.array
        ssmcd.sendXY(image);
    elif wts==2:
        self.stop=1;

