import time
import grovepi
def activatePistol():
	## on ouvre le relai, on attend 1 seconde pour que le pistolet tir, puis on le referme
    grovepi.digitalWrite(7,1)
    time.sleep(1);
    grovepi.digitalWrite(7,0)
def getAltitude():
    return grovepi.ultrasonicRead(4);
    






