import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
fig,ax=canvas(56)
def ring(x,y,r,role,lw=1.1): ax.add_patch(Circle((x,y),r,ec=COL[role],fc='none',lw=lw,zorder=3))
ring(20,31,16,'sujet')
line(ax,[(20,31),(36,31)],'varie',lw=1.4)
disc(ax,20,31,1.5,'fixe'); disc(ax,36,31,1.5,'fixe')
text(ax,20,26.5,'O','encre'); text(ax,40,31,'P','encre'); text(ax,28,34.5,'2 cm','varie','s')
text(ax,20,7,'centre O, passe par P','sujet','s'); text(ax,20,51,'deux points différents','sujet','s')
line(ax,[(47,6),(47,52)],'fixe',dash=True,lw=0.6)
disc(ax,67,31,2.2,'limite')
text(ax,67,41,'O = P','limite','l'); text(ax,67,20,'écartement 0 cm','limite','s'); text(ax,67,7,'aucun cercle','limite','s')
text(ax,67,51,'même point','limite','s')
save(fig,'61-003')
