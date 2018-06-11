# -*- coding: utf-8 -*-
import time

import grovepi
import grovepi3

class flightcommand:
    valeurmillieu=170;
    augmentationmax = 42;
    diminutionmax = 42;
    hauteur=3;
    avancement=3;
    rotation=6;
    slide=5;    

    def allumerEteindreDrone(self):
        self.avancementDrone(0,10);
        self.hauteurDrone(0,10);
        self.slideDrone(0,10);
        self.rotationDrone(1,10);

    def rotationDrone(self,gauchedroite, force):
    ## Valeur pour tourner à gauche : < x
    ## Valeur pour tourner à droite : > x
    ## Valeur pour stabiliser : x
        if not gauchedroite:
            grovepi.analogWrite(self.rotation,self.valeurmillieu-(self.diminutionmax*(force/10)));
        else:
            grovepi.analogWrite(self.rotation,self.valeurmillieu+(self.augmentationmax*(force/10)))

    def stabiliserRotation(self):
        grovepi.analogWrite(self.rotation,self.valeurmillieu)

    def slideDrone(self,gauchedroite, force):
    ## Valeur pour tourner à gauche : < x
    ## Valeur pour tourner à droite : > x
    ## Valeur pour stabiliser : x
        if gauchedroite:
            grovepi.analogWrite(self.slide,self.valeurmillieu-(self.diminutionmax*(force/10)));
        else:
            grovepi.analogWrite(self.slide,self.valeurmillieu+(self.augmentationmax*(force/10)))

    def stabiliserSlide(self):
        grovepi.analogWrite(self.slide,self.valeurmillieu)
        
    def hauteurDrone(self,bashaut, force):
    ## Valeur pour tourner à gauche : < x
    ## Valeur pour tourner à droite : > x
    ## Valeur pour stabiliser : x
        if bashaut:
            print(self.hauteur,self.valeurmillieu-(self.diminutionmax*(force/10)))
            grovepi.analogWrite(self.hauteur,self.valeurmillieu-(self.diminutionmax*(force/10)));
        else:
            grovepi.analogWrite(self.hauteur,self.valeurmillieu+(self.augmentationmax*(force/10)))

    def stabiliserHauteur(self):
        grovepi.analogWrite(self.hauteur,self.valeurmillieu)

    def avancementDrone(self,arriereavant, force):
    ## Valeur pour tourner à gauche : < x
    ## Valeur pour tourner à droite : > x
    ## Valeur pour stabiliser : x
        if not arriereavant:
            valeur = self.valeurmillieu-(self.diminutionmax*(force/10));
            grovepi3.analogWrite(self.avancement,valeur);
        else:
            valeur = self.valeurmillieu+(self.augmentationmax*(force/10))
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
