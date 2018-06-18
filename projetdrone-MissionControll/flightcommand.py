# -*- coding: utf-8 -*-
# import des fonctions de temps pour attendre
import time
## import de grovepi adresse 4
import grovepi
## import du grovepi adresse 3
import grovepi3
## import de la division reele qui retourne un chiffre a virgule
from operator import truediv
class flightcommand:
    ## initialisation des variables de classe
    ## variable des valeurs PWM
    valeurmillieu=164;
    augmentationmax = 40;
    diminutionmax = 47;
    ## variables de pin grovepi
    hauteur=3;
    avancement=3;
    rotation=6;
    slide=5;    
    ## fonction d'allumage et d'arret du drone qui envoie les commandes nécessaire à l'allumage du drone soit en bas à droite pour le joystick de gauche et en bas a gauche pour le joystick de droite
    def allumerEteindreDrone(self):
        self.avancementDrone(0,20);
        self.hauteurDrone(0,20);
        self.slideDrone(0,20);
        self.rotationDrone(1,20);
    ## fonction de rotation
    def rotationDrone(self,gauchedroite, force):
        ## en fonction de gauche/droite ou bas/haut (premier 0 second 1)
        if not gauchedroite:
            ## on envoie au drone une diminution ou augmentation de la valeur du millieu en fonction du sens, changement que l'on definit comme suit : valeurmin ou max * (force_demandée_entre_1_et_20) / 20) on utilise truediv car sans cela python ne prend pas en charge les virgules pour des int -> 0.5 = 0
            grovepi.analogWrite(self.rotation,int(self.valeurmillieu-(self.diminutionmax*(truediv(force,20)))))
        else:
            ## on envoie au drone une diminution ou augmentation de la valeur du millieu en fonction du sens, changement que l'on definit comme suit : valeurmin ou max * (force_demandée_entre_1_et_20) / 20) on utilise truediv car sans cela python ne prend pas en charge les virgules pour des int -> 0.5 = 0
            grovepi.analogWrite(self.rotation,int(self.valeurmillieu+(self.augmentationmax*(truediv(force,20)))))
    ## fonction de stabilisation de la rotation
    def stabiliserRotation(self):
        grovepi.analogWrite(self.rotation,self.valeurmillieu)
    def slideDrone(self,gauchedroite, force):
        ## en fonction de gauche/droite ou bas/haut (premier 0 second 1)
        if gauchedroite:
        ## on envoie au drone une diminution ou augmentation de la valeur du millieu en fonction du sens, changement que l'on definit comme suit : valeurmin ou max * (force_demandée_entre_1_et_20) / 20) on utilise truediv car sans cela python ne prend pas en charge les virgules pour des int -> 0.5 = 0            grovepi.analogWrite(self.slide,int(self.valeurmillieu-(self.diminutionmax*(truediv(force,20)))))
        else:
        ## on envoie au drone une diminution ou augmentation de la valeur du millieu en fonction du sens, changement que l'on definit comme suit : valeurmin ou max * (force_demandée_entre_1_et_20) / 20) on utilise truediv car sans cela python ne prend pas en charge les virgules pour des int -> 0.5 = 0            grovepi.analogWrite(self.slide,int(self.valeurmillieu-(self.diminutionmax*(truediv(force,20)))))
            grovepi.analogWrite(self.slide,int(self.valeurmillieu+(self.augmentationmax*(truediv(force,20)))))
    ## fonction de stabilisation du slide
    def stabiliserSlide(self):
        grovepi.analogWrite(self.slide,self.valeurmillieu)
    def hauteurDrone(self,bashaut, force):
        ## en fonction de gauche/droite ou bas/haut (premier 0 second 1)
        if bashaut:
        ## on envoie au drone une diminution ou augmentation de la valeur du millieu en fonction du sens, changement que l'on definit comme suit : valeurmin ou max * (force_demandée_entre_1_et_20) / 20) on utilise truediv car sans cela python ne prend pas en charge les virgules pour des int -> 0.5 = 0            grovepi.analogWrite(self.slide,int(self.valeurmillieu-(self.diminutionmax*(truediv(force,20)))))
            grovepi.analogWrite(self.hauteur,int(self.valeurmillieu-(self.diminutionmax*(truediv(force,20)))));
        else:
        ## on envoie au drone une diminution ou augmentation de la valeur du millieu en fonction du sens, changement que l'on definit comme suit : valeurmin ou max * (force_demandée_entre_1_et_20) / 20) on utilise truediv car sans cela python ne prend pas en charge les virgules pour des int -> 0.5 = 0            grovepi.analogWrite(self.slide,int(self.valeurmillieu-(self.diminutionmax*(truediv(force,20)))))
            grovepi.analogWrite(self.hauteur,int(self.valeurmillieu+(self.augmentationmax*(truediv(force,20)))))
   ## fonction de stabilisation de la hauteur
    def stabiliserHauteur(self):
        grovepi.analogWrite(self.hauteur,self.valeurmillieu)
    def avancementDrone(self,arriereavant, force):
        ## en fonction de gauche/droite ou bas/haut (premier 0 second 1)
        if not arriereavant:
        ## on envoie au drone une diminution ou augmentation de la valeur du millieu en fonction du sens, changement que l'on definit comme suit : valeurmin ou max * (force_demandée_entre_1_et_20) / 20) on utilise truediv car sans cela python ne prend pas en charge les virgules pour des int -> 0.5 = 0            grovepi.analogWrite(self.slide,int(self.valeurmillieu-(self.diminutionmax*(truediv(force,20)))))
            valeur = int(self.valeurmillieu-(self.diminutionmax*(truediv(force,20))))
            grovepi3.analogWrite(self.avancement,valeur);
        else:
        ## on envoie au drone une diminution ou augmentation de la valeur du millieu en fonction du sens, changement que l'on definit comme suit : valeurmin ou max * (force_demandée_entre_1_et_20) / 20) on utilise truediv car sans cela python ne prend pas en charge les virgules pour des int -> 0.5 = 0            grovepi.analogWrite(self.slide,int(self.valeurmillieu-(self.diminutionmax*(truediv(force,20)))))
            valeur = int(self.valeurmillieu+(self.augmentationmax*(truediv(force,20))))
            grovepi3.analogWrite(self.avancement,valeur)
    ## fonction de stabilisation de l avancement
    def stabiliserAvancement(self):
        grovepi3.analogWrite(self.avancement,self.valeurmillieu)
    ## fonction de decollage
    def decollage(self,valeur):
        self.stabiliserAvancement();
        self.stabiliserSlide();
        self.stabiliserRotation();
        self.hauteurDrone(1,valeur);
    ## fonction d aterrisage
    def atterrissage(self,valeur):
        self.stabiliserAvancement();
        self.stabiliserSlide();
        self.stabiliserRotation();
        self.hauteurDrone(0,valeur);
    ## fonction de stabilisation complete
    def stabiliser(self):
        self.stabiliserAvancement();
        self.stabiliserHauteur();
        self.stabiliserSlide();
        self.stabiliserRotation();
