import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Rectangle
fig,ax=canvas(60)
def grid(x0,y0,c,r,n,role):
    for k in range(c*r):
        i,j=k%c,r-1-k//c
        on=k<n
        ax.add_patch(Rectangle((x0+i*3.4,y0+j*3.4),3,3,fc=COL[role] if on else FILL['fixe'],ec=COL[role] if on else COL['fixe'],lw=0.4,zorder=2))
grid(6,22,6,5,18,'sujet'); grid(44,22,10,8,24,'autre')
text(ax,16,43,'30 élèves','sujet','s'); text(ax,61,52,'80 élèves','autre','s')
text(ax,16,17,'18 absents','sujet','s'); text(ax,61,17,'24 absents','autre','s')
text(ax,16,7,'60 %','sujet','l',weight='bold'); text(ax,61,7,'30 %','autre','l',weight='bold')
save(fig,'09-105')
