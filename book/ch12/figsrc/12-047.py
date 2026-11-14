import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
box(ax,4,54,80,9,'fixe',label='deux fois la somme de 4 et 3',size='m')
arrow(ax,(44,53),(44,46),'varie')
text(ax,16,36,r'$2$','encre','xl'); box(ax,24,29,30,14,'sujet',label=r'$(4+3)$',size='l'); text(ax,70,36,'un seul nombre','sujet','s')
arrow(ax,(39,28),(39,21),'varie')
text(ax,16,11,r'$2\times$','encre','l'); box(ax,26,4,26,14,'sujet',label=r'$7$',size='l'); text(ax,68,11,r'$=14$','resultat','l')
save(fig,'12-047')
