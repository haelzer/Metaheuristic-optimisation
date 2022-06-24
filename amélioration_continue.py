import random
from etat import etat,dessin

n=5;
etat_initial =  [ random.randint(0, n-1) for k in range(n) ]


def amélioration_continue(etat_initial):
    etat_actuel = etat(etat_initial)
    while True:
        meilleur_voisin = etat_actuel.meilleur_etat_voisin()
        print("Cout du meilleur voisin: " + str(meilleur_voisin.cout()) + "\nCout de l'état actuel :" + str(etat_actuel.cout()))
        if meilleur_voisin.cout() >= etat_actuel.cout():
            return etat_actuel.etat
        else:
            etat_actuel = meilleur_voisin
    return etat_actuel.etat

dessin(amélioration_continue(etat_initial))