import time
import grovepi
import grovepi3
from lcdcontroll import *

def lcdWrite(text):
    setText(text)
    setRGB(0,128,64)

def waitButtonPress():
    while not grovepi.digitalRead(2):
        time.sleep(0.2)

def activatePistol():
    grovepi.digitalWrite(7,1)
    grovepi3.digitalWrite(2,1)
    time.sleep(3);
    grovepi.digitalWrite(7,0)
    grovepi3.digitalWrite(2,0)

def getAltitude():
    return grovepi.ultrasonicRead(4);
    






