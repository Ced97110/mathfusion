import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(60)
box(ax,8,40,72,14,'resultat',label='aucune liste finie\nde briques ne suffit',size='s')
numberline(ax,6,46,18,0,5)
text(ax,28,6,'entiers','fixe','s')
line(ax,[(60,10),(60,30)],'limite',dash=True)
text(ax,72,21,'∞','sujet','xl'); text(ax,72,10,'pas un entier','limite','s')
arrow(ax,(72,26),(72,40),'sujet')
save(fig,'61-045')
