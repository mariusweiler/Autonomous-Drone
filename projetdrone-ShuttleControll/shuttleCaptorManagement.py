import time
import grovepi

def activatePistol():
    grovepi.digitalWrite(7,1)
    grovepi3.digitalWrite(2,1)
    time.sleep(3);
    grovepi.digitalWrite(7,0)
    grovepi3.digitalWrite(2,0)

def getAltitude():
    return grovepi.ultrasonicRead(4);
    






