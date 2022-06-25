Réalisé sur Python 3.7.4

Ont été réalisés 3 algorithmiques de résolution du problème des n reines basées sur les métaheuristiques:
-Amélioration continue
-Recuit simulé
-Recherche tabou

Les fichiers fournis sont au nombre de 4:
etat.py
amélioration_continue.py
recuit_simulé.py
recherche_tabou.py

Le fichier etat.py introduit une classe représentant l'état de l'échiquier et les fonctions de classes que sont le calcul du cout d'un état et la détermination du meilleur état voisin.
Les détails de la modélisations sont précisés en commentaire du fichier etat.py.
Afin de visualiser les solutions, une fonction dessin a été écrite au sein du fichier etat.py qui permet de représenter graphiquement l'échiquier avec une heatmap.

Dans les tests préprogrammés, l'état initial est randomisé à chaque fois. Le taille n de l'échiquier peut être modifiée.
Pour le recuit simulé, on prend également en entrée un paramètre T, qui correspond à une valeur limite. Il contrôle directement le nombre d'itération, et plus on l'augmente plus on a de chance d'éviter de rester bloqué dans un minimum local.
Pour la recherche tabou, on prend également en entrée un paramètre représentant la taille maximale de la file de stockage de l'historique des voisins. Il faut une taille raisonnable pour éviter de former des circuits de voisins. On a pris dans notre test un multiple de n, par exemple 2*n, qui permet de ne pas augmenter la complexité en espace de l'algorithme (2n listes de n éléments = O(n²), même complexité que le stockage des voisins d'un état) tout en fournissant assez d'historique pour éviter les circuits de voisins, en général.
