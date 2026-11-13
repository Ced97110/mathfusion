import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
text(ax,44,62,r'$G$ : couples de 0 ou 1','sujet','m')
P={'00':(18,42),'01':(44,42),'10':(18,18),'11':(44,18)}
for k,(x,y) in P.items(): disc(ax,x,y,5,'sujet',label=k)
arrow(ax,(23.5,43.5),(38.5,43.5),'varie'); arrow(ax,(38.5,40.5),(23.5,40.5),'varie')
arrow(ax,(23.5,19.5),(38.5,19.5),'varie'); arrow(ax,(38.5,16.5),(23.5,16.5),'varie')
text(ax,70,36,'ajouter 01','varie','m'); text(ax,70,30,'= 2 cycles','resultat','s'); text(ax,70,25,'de longueur 2','resultat','s')
text(ax,44,5,'les éléments sont permutés','fixe','s')
save(fig,'46-280')
