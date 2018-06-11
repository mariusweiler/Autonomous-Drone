## Melody
## (cleft) 2005 D. Cuartielles for K3
## 
## This example uses a piezo speaker to play melodies.  It sends
## a square wave of the appropriate frequency to the piezo, generating
## the corresponding tone.
## 
## The calculation of the tones is made following the mathematical
## operation:
##       timeHigh = period / 2 = 1 / (2 * toneFrequency)
## 
##  where the different tones are described as in the table:
## 
## note  frequency  period  timeHigh
## c          261 Hz          3830  1915  
## d          294 Hz          3400  1700  
## e          329 Hz          3038  1519  
## f          349 Hz          2864  1432  
## g          392 Hz          2550  1275  
## a          440 Hz          2272  1136  
## b          493 Hz          2028 1014 
## C         523 Hz         1912  956
## 
## http://www.arduino.cc/en/Tutorial/Melody

import time

import grovepi3


def playSong():
    length = 15;
    notes = ['g','c','d','e','g','c','d','e','g','c','d','e','g','c','d'];
    beats = [2, 2, 2, 4, 2, 2, 2, 4, 2, 2, 2, 4, 2, 2, 2];
    tempo = 150;
    for i in range(1,length):
        if notes[i] == ' ':
            time.sleep(beats[i] * tempo * 0.001);
        else:
            playNote(notes[i], beats[i] * tempo);
    time.sleep((tempo / 2)*0.001); 


def playTone(tone, duration):
    for i in range(1,duration*1000,tone*2):
        grovepi3.digitalWrite(6,1);
        time.sleep(tone*0.000001);
        grovepi3.digitalWrite(6,0);
        time.sleep(tone*0.000001);

def playNote(note, duration):
    names = ['c', 'd', 'e', 'f', 'g', 'a', 'b', 'C'];
    tones = [1915, 1700, 1519, 1432, 1275, 1136, 1014, 956];
    for i in range(0,7):
        if names[i] == note:
            playTone(tones[i], duration);

def initialisebuzzer():
    grovepi3.pinMode(6, 'OUTPUT');




