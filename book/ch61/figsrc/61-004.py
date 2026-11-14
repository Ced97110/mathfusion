import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
fig,ax=canvas(52)
def ring(x,y,r,role,lw=1.1): ax.add_patch(Circle((x,y),r,ec=COL[role],fc='none',lw=lw,zorder=3))
for x in (29.5,58.5): line(ax,[(x,5),(x,48)],'fixe',dash=True,lw=0.6)
text(ax,15,45,'point donné','fixe','m'); disc(ax,15,28,2.2,'fixe'); text(ax,15,12,'fourni','fixe','s')
text(ax,44,45,'posé à l’œil','limite','m'); disc(ax,44,28,2.2,'limite'); text(ax,44,12,'place au hasard','limite','s')
text(ax,73.5,45,'point construit','resultat','m')
line(ax,[(61,24),(86,24)],'sujet',lw=1.2); ring(73.5,32,10,'sujet')
import math
dx=math.sqrt(10**2-8**2); disc(ax,73.5-dx,24,2.2,'resultat')
text(ax,73.5,12,'intersection','resultat','s')
save(fig,'61-004')
