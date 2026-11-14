import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
box(ax,4,46,80,9,'fixe',label='prémisse : n est un entier',size='s')
box(ax,4,18,26,16,'sujet',label='n pair')
box(ax,58,18,26,16,'autre',label=r'$n^2$ pair')
arrow(ax,(31,29),(57,29),'varie'); text(ax,44,32.5,'sens 1','varie','s')
arrow(ax,(57,23),(31,23),'varie'); text(ax,44,19.5,'sens 2','varie','s')
text(ax,44,7,'conclusion : équivalence','resultat','s')
save(fig,'52-108')
