import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Rectangle
fig,ax=canvas(86)
u=2.4
def grid(x,y,r,c,role,n=None):
    for i in range(r):
        for j in range(c):
            ax.add_patch(Rectangle((x+j*u,y+i*u),u,u,ec=COL[role],fc=FILL[role],lw=0.5,zorder=2))
text(ax,44,83,'rectangles pleins de 24 carreaux','encre','m')
for (r,c,y,lab) in ((1,24,76,'1 et 24'),(2,12,66,'2 et 12'),(3,8,54,'3 et 8'),(4,6,40,'4 et 6')):
    grid(4,y,r,c,'sujet'); text(ax,4+c*u+3,y+r*u/2,lab,'sujet','m',ha='left')
text(ax,44,33,'1, 2, 3, 4, 6, 8, 12, 24','resultat','l')
text(ax,44,26,'8 diviseurs, 2 par rectangle','resultat','m')
grid(4,4,5,4,'fixe'); grid(17.6,4,2,2,'limite')
text(ax,26,10,'5 rangées : reste 4','limite','m',ha='left')
save(fig,'05-023')
