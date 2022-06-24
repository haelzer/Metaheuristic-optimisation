import random
from math import exp
from etat import etat,dessin

n=8;
etat_initial =  [ random.randint(0, n-1) for k in range(n) ]

def choix(t,delta): #fonction retournant vrai avec une probabilité de exp(-delta*t)
     r = random.random()
     return (r <= exp(-delta*t))
     

def recuit_simulé(T,etat_initial):
    etat_actuel = etat(etat_initial)
    t = 1
    while t <= T:
        meilleur_voisin = etat_actuel.meilleur_etat_voisin()
        delta= meilleur_voisin.cout() - etat_actuel.cout()
        if delta < 0 : #le voisin est meilleur que l'état actuel
            etat_actuel = meilleur_voisin
        else : #le voisin est pire que l'état actuel
            if choix(t,delta) : 
               etat_actuel = meilleur_voisin
        t += 1
    return etat_actuel.etat 

dessin(recuit_simulé(100,etat_initial))