import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
fig,ax=canvas(60)
y0=28
f=numberline(ax,14,70,y0,-1,2,1)
line(ax,[(f(0),6),(f(0),52)],'fixe',dash=True,lw=0.6)
ax.add_patch(Circle((f(0),y0),f(1)-f(0),ec=COL['sujet'],fc='none',lw=1.3,zorder=3))
disc(ax,f(0),y0,1.5,'fixe'); disc(ax,f(1),y0,1.5,'fixe')
text(ax,f(0)-8,33,'(0 ; 0)','encre','s'); text(ax,f(1)+7.5,33,'(1 ; 0)','encre','s')
text(ax,67,18,'droite : axe horizontal','varie','s')
text(ax,68,52,'cercle de rayon 1','sujet','s'); text(ax,68,47,'centre (0 ; 0)','sujet','s')
text(ax,44,3.5,'dessin → couples de nombres','resultat','m')
save(fig,'61-014')
