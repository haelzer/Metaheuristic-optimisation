import random
from etat import etat,dessin

n=8;
etat_initial =  [ random.randint(0, n-1) for k in range(n) ]


def recherche_tabou(etat_initial,taille_file):
    etat_actuel = etat(etat_initial)
    visités=[False]*taille_file #file FIFO de l'historique des voisins visités
    visités.append(etat_initial)
    meilleur_voisin = etat_actuel.meilleur_etat_voisin_tabou(visités)
    compteur_taille_file=1 #Pour représenter le caractère FIFO de la file, on garde en mémoire un compteur modulo la taille de la file qui représente l'indice auquel il faut insérer le nouvel élément.
    cout_actuel=etat_actuel.cout()
    while cout_actuel > 0 and meilleur_voisin != False:
        print("\nétat actuel: " + str(etat_actuel.etat))
        #print("Cout de l'état actuel :" + str(etat_actuel.cout()) + "\nCout du meilleur voisin non déja visité: " + str(meilleur_voisin.cout()))
        print("\nmeilleur voisin: " + str(meilleur_voisin.etat))
        print("\nvisités: "+str(visités))
        visités[compteur_taille_file%taille_file]=meilleur_voisin.etat
        compteur_taille_file+=1
        etat_actuel = meilleur_voisin
        cout_actuel = etat_actuel.cout()
        meilleur_voisin = etat_actuel.meilleur_etat_voisin_tabou(visités)
    print("\nCout de la solution: " + str(etat_actuel.cout()))
    return etat_actuel.etat

dessin(recherche_tabou(etat_initial,2*n))