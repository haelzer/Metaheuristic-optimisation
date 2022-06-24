import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Nous créons une classe d'objets pour représenter l'état de notre échiquier.
#Un état de l'échiquier désigne la position des n reines sur l'échiquier n*n
#On structure l'espace avec la solution n°2 du cours: chaque reine est sur une colonne différente Il y a n reines et l'échiquier est de taille n*n.
#L'état d'un échiquier est représenté par une liste d'entiers entre 0 et (n-1). etat[k] donne la position de la k-ème reine (située sur la k-ème colonne) dans cette colonne. etat[k]=j siginifie que la k-ème reine est placée sur la j-ème case de la k-ème colonne.
#Un état voisin est un état dans lequel on a bougé une seule reine sur la colonne dans laquelle elle est, c'est-à-dire vers le haut ou vers le bas.
#Le cout d'un état désigne le nombre d'attaques possibles entre des reines dans l'état actuel de l'échiquier.
#Notre classe possède  deux fonctions de classe : une fonction cout et une fonction meilleur_etat_voisin. La fonction cout retourne le cout de l'état actuel de l'échiquier, la fonction meilleur_etat_voisin retourne l'état voisin de cout minimal. On a écrit une version alternative de la fonction meilleur_etat_voisin pour le cas de la recherche tabou, qui prend en entrée une liste de voisins déjà visités et qui ne sont pas à considérer.

class etat:
    
    def __init__(self, etat_initial): #initialisation de l'état par une liste
        self.etat = etat_initial
        
    def cout(self):     #Fonction qui donne le cout d'un échiquier
        c = 0 #compteur
        n= len(self.etat) #taille de l'échiquier
        for elem in self.etat: #On compte le nombre d'attaques via déplacement sur une ligne
            if self.etat.count(elem) > 1: #S'il y a plusieurs reines sur la même ligne -> une attaque est possible
                c += 1                
        for i in range(n): #On compte le nombre d'attaques via déplacement diagonal
            for j in range(i+1, n):
                if abs(j-i) == abs(self.etat[j] - self.etat[i]): #si les deux reines sont sur la même diagonale -> une attaque est possible
                       c += 1 
        return c
    
    def meilleur_etat_voisin(self): #retourne le meilleur état voisin
        n= len(self.etat) #taille de l'échiquier
        voisins = np.full((n,n), None) #tableau des coûts des états voisins. voisins[i][j] donne le coût de l'état voisin dans lequel on a déplacé la i_ème reine sur la j_ème case de sa colonne.
        for i in range(n):
            for j in range(n):
                if j != self.etat[i]: # pour qu'il y ait effectivement déplacement
                    nouvel_etat = self.etat.copy()
                    nouvel_etat[i] = j #nouvelle position de la i_ème reine
                    nouvel_etat = etat(nouvel_etat)
                    voisins[i][j] = (nouvel_etat).cout()

        meilleur_voisin = (0,1)
        cout_min = -1 #on initialise le cout minimal par une valeur distinguée, négative
        
        #Recherche du voisin de cout minimal
        for i in range(n):
            for j in range(n):
                if (voisins[i][j] != None) :
                    c=voisins[i][j]
                    if c < cout_min or cout_min<0 :
                        cout_min=c
                        meilleur_voisin=(i,j)            
                        
        (i,j)=meilleur_voisin
        nouvel_etat = self.etat.copy()
        nouvel_etat[i] = j
        return (etat(nouvel_etat)) #retourne le meilleur état voisin
    
    def meilleur_etat_voisin_tabou(self,visités): #retourne le meilleur état voisin non déja visité
        n= len(self.etat) #taille de l'échiquier
        voisins = np.full((n,n), None) #tableau des coûts des états voisins. voisins[i][j] donne le coût de l'état voisin dans lequel on a déplacé la i_ème reine sur la j_ème case de sa colonne.
        for i in range(n):
            for j in range(n):
                if j != self.etat[i]: # pour qu'il y ait effectivement déplacement
                    nouvel_etat = self.etat.copy()
                    nouvel_etat[i] = j #nouvelle position de la i_ème reine
                    if nouvel_etat not in visités :
                        nouvel_etat = etat(nouvel_etat)
                        voisins[i][j] = (nouvel_etat).cout()

        meilleur_voisin = (0,1)
        cout_min = -1 #on initialise le cout minimal par une valeur distinguée, négative
        
        #Recherche du voisin de cout minimal
        for i in range(n):
            for j in range(n):
                if (voisins[i][j] != None) :
                    c=voisins[i][j]
                    if c < cout_min or cout_min<0 :
                        cout_min=c
                        meilleur_voisin=(i,j)            
        if cout_min<0: 
            return False
        else:
            (i,j)=meilleur_voisin
            nouvel_etat = self.etat.copy()
            nouvel_etat[i] = j
            return (etat(nouvel_etat)) #retourne le meilleur état voisin
    
#Fonction donnant le dessin de l'échiquier basé sur un état donné en entrée (sous forme de liste)
def dessin(etat):
    print(etat) #on affiche la liste
    n=len(etat)
    echiquier = [ [0]*n for k in range(n)]
    for i in range(n):
        echiquier[etat[i]][i] = 1
    l = range(1,n+1)
    plt.figure(figsize=(7,7))
    sns.heatmap(echiquier, linewidths=.8,cbar=False,cmap='Set1',xticklabels=l,yticklabels=l) 