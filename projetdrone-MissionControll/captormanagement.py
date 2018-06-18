import time
import grovepi
import grovepi3
from lcdcontroll import *
def lcdWrite(text):
    setText(text)
    setRGB(0,128,64)
def waitButtonPress():
	## tant que le bouton n est pas pressé on attend
    while not grovepi.digitalRead(2):
        time.sleep(0.2)
def activatePistol():
    grovepi.digitalWrite(7,1)
    time.sleep(3);
    grovepi.digitalWrite(7,0)
def getAltitude():
    return grovepi.ultrasonicRead(4);
    






