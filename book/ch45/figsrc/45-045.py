import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(85)
text(ax,44,79,'base 2 : une image par entier','resultat','m',weight='bold')
for i,v in enumerate(['1/4','1/2','1','2','4','8']):
    box(ax,3+i*14,56,13,10,'resultat',label=v,size='s')
line(ax,[(4,42),(84,42)],'fixe',dash=True)
text(ax,44,34,r'base 1 : l\'image est toujours $1$','limite','m',weight='bold') if False else text(ax,44,34,'base 1 : une seule image','limite','m',weight='bold')
box(ax,32,12,24,14,'limite',label=r'$1$',size='l')
text(ax,70,19,'3, 5, …','limite','s')
arrow(ax,(63,19),(58,19),'limite')
save(fig,'45-045')
