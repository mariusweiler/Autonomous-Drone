# -*- coding: utf-8 -*-
import time

import grovepi
import grovepi3
from operator import truediv

class flightcommand:
    valeurmillieu=164;
    augmentationmax = 40;
    diminutionmax = 47;
    hauteur=3;
    avancement=3;
    rotation=6;
    slide=5;    

    def allumerEteindreDrone(self):
        self.avancementDrone(0,20);
        self.hauteurDrone(0,20);
        self.slideDrone(0,20);
        self.rotationDrone(1,20);

    def rotationDrone(self,gauchedroite, force):
    ## Valeur pour tourner à gauche : < x
    ## Valeur pour tourner à droite : > x
    ## Valeur pour stabiliser : x
        if not gauchedroite:
            print(int(self.valeurmillieu-(self.diminutionmax*(truediv(force,20)))))
            grovepi.analogWrite(self.rotation,int(self.valeurmillieu-(self.diminutionmax*(truediv(force,20)))))
        else:
            print(int(self.valeurmillieu+(self.augmentationmax*(truediv(force,20)))))
            grovepi.analogWrite(self.rotation,int(self.valeurmillieu+(self.augmentationmax*(truediv(force,20)))))

    def stabiliserRotation(self):
        grovepi.analogWrite(self.rotation,self.valeurmillieu)

    def slideDrone(self,gauchedroite, force):
    ## Valeur pour tourner à gauche : < x
    ## Valeur pour tourner à droite : > x
    ## Valeur pour stabiliser : x
        if gauchedroite:
            print(int(self.valeurmillieu-(self.diminutionmax*(truediv(force,20)))))
            grovepi.analogWrite(self.slide,int(self.valeurmillieu-(self.diminutionmax*(truediv(force,20)))))
        else:
            print(int(self.valeurmillieu+(self.augmentationmax*(truediv(force,20)))))
            grovepi.analogWrite(self.slide,int(self.valeurmillieu+(self.augmentationmax*(truediv(force,20)))))

    def stabiliserSlide(self):
        grovepi.analogWrite(self.slide,self.valeurmillieu)
        
    def hauteurDrone(self,bashaut, force):
    ## Valeur pour tourner à gauche : < x
    ## Valeur pour tourner à droite : > x
    ## Valeur pour stabiliser : x
        if bashaut:
            print(int(self.valeurmillieu-(self.diminutionmax*(truediv(force,20)))))
            grovepi.analogWrite(self.hauteur,int(self.valeurmillieu-(self.diminutionmax*(truediv(force,20)))));
        else:
            print(int(self.valeurmillieu+(self.augmentationmax*(truediv(force,20)))))
            grovepi.analogWrite(self.hauteur,int(self.valeurmillieu+(self.augmentationmax*(truediv(force,20)))))

    def stabiliserHauteur(self):
        grovepi.analogWrite(self.hauteur,self.valeurmillieu)

    def avancementDrone(self,arriereavant, force):
    ## Valeur pour tourner à gauche : < x
    ## Valeur pour tourner à droite : > x
    ## Valeur pour stabiliser : x
        if not arriereavant:
            valeur = int(self.valeurmillieu-(self.diminutionmax*(truediv(force,20))))
            grovepi3.analogWrite(self.avancement,valeur);
        else:
            print(int(self.valeurmillieu+(self.augmentationmax*(truediv(force,20)))))
            valeur = int(self.valeurmillieu+(self.augmentationmax*(truediv(force,20))))
            grovepi3.analogWrite(self.avancement,valeur)

    def stabiliserAvancement(self):
        grovepi3.analogWrite(self.avancement,self.valeurmillieu)

    def decollage(self,valeur):
        self.stabiliserAvancement();
        self.stabiliserSlide();
        self.stabiliserRotation();
        self.hauteurDrone(1,valeur);

    def atterrissage(self,valeur):
        self.stabiliserAvancement();
        self.stabiliserSlide();
        self.stabiliserRotation();
        self.hauteurDrone(0,valeur);

    def stabiliser(self):
        self.stabiliserAvancement();
        self.stabiliserHauteur();
        self.stabiliserSlide();
        self.stabiliserRotation();

    def stabiliser2(self):
        self.stabiliserAvancement();
        self.stabiliserHauteur2();
        self.stabiliserSlide();
        self.stabiliserRotation();
