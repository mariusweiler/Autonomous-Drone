# -*- coding: utf-8 -*-

# import des fonctions pour la gestion des capteurs
from captormanagement import *
# import des fonctions de controle de vol pour le drone
from flightcommand import *
# import des fonctions de temps pour faire des pauses
import time
# import des fonctions d'open cv
import cv2
# import de notre class communicationmanagement
from communicationManagement import socketCommManagement
# import de notre class flightserver
from flightserver import *
# import de la classe Queue
from multiprocessing import Queue
# Declaration des variables du script
## Variable permettant de savoir si on a déjà tiré.
tireffectuer=False;
## variable permettant de connaitre la position du milieu de l'image pour aligner la cible
valeurmillieu=200;
## variable permettant de savoir si l'atterrissage a été effectué
atterrissageok=0;
## variable gardant les commandes de vol
fc = flightcommand();
# initialisations en début de script
## On écrit sur l'ecran LCD
lcdWrite('- Attente connexion drone -');
## on créer un nouveau socketflightserver
sfs=socketFlightServer();
## on créer une queue
laqueue=Queue();
## on creer un socketcommmanagement et on lui transmet la queue qui permet de communiquer avec lui
scm=socketCommManagement(laqueue);
# PHASE -1 - PREPARATION DU VOL
## on écrit à l'écran
lcdWrite('Demarrage du drone d attaque.');
## on attend 4 secondes
time.sleep(4);
## on lance la stabilisation car lors de l'allumage il faut que les valeurs du milieu soit envoyées pour pouvoir l allumer ensuite
fc.stabiliser();
## on écrit a l ecran
lcdWrite('Calibrez le GPS, puis appuyez sur le btn');
## on attend que l'utilisateur presse sur le bouton
waitButtonPress();
## on écrit a l ecran
lcdWrite('Appuyez sur le btn pour demarrer.');
## on attend que l'utilisateur presse sur le bouton
waitButtonPress();
## on écrit a l ecran
lcdWrite('Cest parti mon KIKI !');
time.sleep(1);
## on écrit a l ecran
lcdWrite('Reculez - demar. dans 3');
## on attend 1 seconde
time.sleep(1);
## on écrit a l ecran
lcdWrite('Reculez - demar. dans 2');
## on attend 1 seconde
time.sleep(1);
## on écrit a l ecran
lcdWrite('Reculez - demar. dans 1');
## on attend 1 seconde
time.sleep(1);
# PHASE 0 - ALLUMAGE DU DRONE
## on écrit a l ecran
lcdWrite('Attaque en cours - Allumage');
## on lance la fonction d allumage de drone
fc.allumerEteindreDrone();
## on dis a shuttle control que l'on veut une hauteur
laqueue.put('0');
## on attend 5 secondes
time.sleep(5);
# PHASE 1 - DECOLLAGE DE QUELQUE METRE
## on écrit a l ecran
lcdWrite('Attaque en cours - Decollage');
## tant que l'on a pas tiré
while not tireffectuer:
# PHASE 2 - STABILISATION ALTITUDE A 1M50 ET GYROSCOPE
## on écrit a l ecran
    lcdWrite('Attaque en cours - Stabil.')
## on lance la commande de decollage a 6 sur 20 (peu fort)
    fc.decollage(6);
## on attend de recevoir la valeur de hauteur atteinte (1m) par le drone
    sfs.waitHeightOk();
## drone a la bonne hauteur, on stabilise
    fc.stabiliser();
# PHASE 3 - RECHERCHE ET ALIGNEMENT DE CIBLE
## on écrit a l ecran
    lcdWrite('Attaque en cours - Recherche.')   
## on dis a shuttle control que l'on veut une position 
    laqueue.put('1');
## on attend 0.3 secondes pour laisser le temps a shuttle d'envoyer la position non plus la hauteur
    time.sleep(0.3);
## on reprend uniquement les valeurs en x car y ne sont pas utiles
    xA,xB=sfs.getPersonPosition();
## si personne n a été trouvé par la detection
    if xA == 999999999 and xB == 999999999:
        fc.rotationDrone(0,5)
        time.sleep(0.7)
        fc.stabiliser();
## Sinon, s'il y'a quelqu'un
    else:
## si il est trop à gauche
        if xA+25 < valeurmillieu and xB-25 <= valeurmillieu:
## rotation vers la gauche à 5 sur 20 (doucement)
            fc.rotationDrone(0,5)
## on attend 0.7 s
            time.sleep(0.7)
## on stabilise
            fc.stabiliser();
## sinon si c'est trop à droite
        elif xA+25 >= valeurmillieu and xB-25 >= valeurmillieu:
## rotation vers la gauche à 5 sur 20 (doucement)
            fc.rotationDrone(0,5)
            time.sleep(0.7)
## on attend 0.7 s
            fc.stabiliser();
## on stabilise
## sinon si la personne est bien centrée
        else:
# PHASE 5 - TIR
## on affiche a l ecran
            lcdWrite('Attaque en cours - FEUER FREI.')
## on informe shuttle control qu'il faut tirer
            laqueue.put('2');
## on lance la methode de tir
            activatePistol()
## Le tir a ete fait, on change la variable tireffectuer    
            tireffectuer = True
## fin de la boucle, on redemande la hauteur pour la prochaine stabilisation
    laqueue.put('0');
# PHASE 6 - ATTERRISSAGE
## on lance l'atterissage
lcdWrite('Attaque en cours - Atterrissage.')
while not atterrissageok:
    if getAltitude() < 40:
        fc.atterissage(3);
        time.sleep(0.3)
    else:
        fc.atterissage(8);
        time.sleep(0.5)
    if getAltitude()==1:
        fc.stabiliser();
        time.sleep(1)
        atterissage=true;
# PHASE 7 - ARRET DU DRONE
## on affiche a l ecran
lcdWrite('Attaque en cours - Arret.');
## on arrete le drone
fc.allumerEteindreDrone();
## on ferme le scm qu'il faut fermer la connexion
laqueue.put('3');
## on laisse un peu de temps pour que shuttle control ferme la connexion
time.sleep(2);
## on ferme la connexion du sfs
sfs.closeSocket();
## on affiche a l ecran
lcdWrite('Attaque terminee...')