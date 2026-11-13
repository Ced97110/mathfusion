import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
box(ax,6,44,34,12,'sujet',label=r'$6x-4$',size='l'); text(ax,44,50,'=','encre','xl'); box(ax,48,44,34,12,'sujet',label=r'$2x+8$',size='l')
text(ax,23,60.5,'$x$ à gauche','sujet','s'); text(ax,65,60.5,'$x$ à droite','sujet','s')
text(ax,44,32,r'retirer $2x$ des deux côtés','varie','m')
arrow(ax,(23,42),(23,25),'varie'); arrow(ax,(65,42),(65,25),'varie')
box(ax,6,11,34,12,'resultat',label=r'$4x-4$',size='l'); text(ax,44,17,'=','encre','xl'); box(ax,48,11,34,12,'resultat',label='$8$',size='l')
text(ax,23,5.5,'$x$ d’un seul côté','resultat','s')
save(fig,'16-085')
