# -*- coding: utf-8 -*-
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

# initialisation de la camera
print('ok');
camera = PiCamera()
print('ok1');
rawCapture = PiRGBArray(camera)
print('ok2');
camera.capture(rawCapture, format="bgr")
print('ok3');
image = rawCapture.array
print('ok4');
 # initialize the HOG descriptor/person detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
        # load the image and resize it to (1) reduce detection time
        # and (2) improve detection accuracy
image = imutils.resize(image, width=min(400, image.shape[1]))
        # detect people in the image
(rects, weights) = hog.detectMultiScale(image, winStride=(4, 4),padding=(8, 8), scale=1.05)
        # apply non-maxima suppression to the bounding boxes using a
        # fairly large overlap threshold to try to maintain overlapping
        # boxes that are still people
rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)
        # draw the final bounding boxes
for (xA, yA, xB, yB) in pick:
        cv2.rectangle(image, (xA, yA), (xB, yB), (0, 255, 0), 2)
print(pick)

cv2.imwrite('/home/pi/Desktop/test.jpg',image)
cv2.namedWindow('preview')
cv2.startWindowThread()

print('okokokokok')
cv2.imshow("After NMS", image)
print('okokokokok')
cv2.waitKey(0)
print('ok5');
print('tab');
print(tab);
print('ok6');
rawCapture.truncate()
print('ok7');
rawCapture.seek(0)
print('ok8');



