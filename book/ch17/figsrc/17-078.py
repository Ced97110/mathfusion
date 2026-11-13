import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(84)
box(ax,6,62,22,11,'sujet',label=r'$-3y$',size='m'); box(ax,30,62,14,11,'varie',label=r'$\geq$',size='m'); box(ax,46,62,14,11,'fixe',label=r'$6$',size='m')
box(ax,6,30,22,11,'sujet',label=r'$y$',size='m'); box(ax,30,30,14,11,'varie',label=r'$\leq$',size='m'); box(ax,46,30,14,11,'resultat',label=r'$-2$',size='m')
arrow(ax,(33,60),(33,43),'varie'); text(ax,38,54,r'$\div(-3)$','varie','s',ha='left'); text(ax,38,48,'diviseur négatif : oui','varie','s',ha='left')
text(ax,33,22,'on retourne le symbole','varie','s')
text(ax,33,10,r'$y=-3$ : $9\geq 6$ vrai','resultat','s')
save(fig,'17-078')
