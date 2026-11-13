import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(60)
text(ax,44,55,'somme des quatre carrés','sujet','s')
box(ax,4,34,80,14,'sujet',label=r'$\alpha_0^2+\alpha_1^2+\alpha_2^2+\alpha_3^2$')
brace(ax,10,78,34,'varie')
text(ax,44,27,'$N$','varie','xl'); text(ax,66,27,'un seul nombre réel','varie','s')
arrow(ax,(44,23.5),(44,17),'varie')
box(ax,14,4,60,13,'resultat',label=r'ici : $N=1+4+0+4=9$')
save(fig,'51-189')
