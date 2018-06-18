# -*- coding: utf-8 -*-
## CODE DE TEST, POUR PLUS D INFORMATION VOIR LES COMMENTAIRES DU FICHIER SHUTTLEPEDESTRIANDETECTION ET SHUTTLEFLIGHTCONTROLLER
## Permet de tester la détection de personne, créer une image avec le rectangle autour d'une personne si présente, et affichage dans la console des valeurs en x et y
from shuttlePersondetection import persondetection
from shuttleCaptorManagement import *
from shuttleSendMissionControllData import *
from shuttleCommManagement import *
from multiprocessing import Queue
from picamera.array import PiRGBArray
from picamera import PiCamera
from imutils.object_detection import non_max_suppression
from imutils import paths
import time
import cv2
import numpy as np
import argparse
import imutils
stop = 0;
camera = PiCamera()
rawCapture = PiRGBArray(camera)
camera.capture(rawCapture, format="bgr")
image = rawCapture.array
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
image = imutils.resize(image, width=min(400, image.shape[1]))
(rects, weights) = hog.detectMultiScale(image, winStride=(4, 4),padding=(8, 8), scale=1.05)
rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)
for (xA, yA, xB, yB) in pick:
	cv2.rectangle(image, (xA, yA), (xB, yB), (0, 255, 0), 2)
print(pick)
cv2.imwrite('/home/pi/Desktop/test.jpg',image)



