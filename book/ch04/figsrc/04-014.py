import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(76); ax.set_ylim(1,77)  # cadre resserré sur le contenu (y 4→73), coordonnées de la spec inchangées
# e1 : un petit cube seul, unité
cubes(ax,[(0,0,0)],(40,62),5.5,'fixe')
text(ax,47,67,'1 petit cube : côté 1','fixe','s',ha='left')
# e2 : caisse de côté 2, couche par couche (de bas en haut)
for k,role in ((0,'sujet'),(1,'varie')):
    cubes(ax,[(i,j,k) for i in (0,1) for j in (0,1)],(20,22),5.5,role)
# e3 : caisse de côté 3, couche par couche (de bas en haut)
for k,role in ((0,'sujet'),(1,'varie'),(2,'sujet')):
    cubes(ax,[(i,j,k) for i in (0,1,2) for j in (0,1,2)],(62,22),5.5,role)
# e4 : côtés sous chaque caisse
text(ax,20,17,'côté 2','fixe','s')
text(ax,62,17,'côté 3','fixe','s')
# e5 : nombre de couches et de cubes par couche
text(ax,20,11.5,'2 couches de 4 cubes','varie','s')
text(ax,62,11.5,'3 couches de 9 cubes','varie','s')
# e6 : résultat en nombre de petits cubes
text(ax,20,5.5,'= 8 petits cubes','resultat','m')
text(ax,62,5.5,'= 27 petits cubes','resultat','m')
save(fig,'04-014')
