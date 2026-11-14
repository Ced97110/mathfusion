import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
fig,ax=canvas(82)
k=math.sqrt(math.pi)
for cy,r,l1,l2 in ((68,7,r'$r = 1$ cm : $c^2 = \pi$',None),(33,14,r'$r = 2$ cm : $c^2 = 4\pi$',r'$c = 2\sqrt{\pi}$ = $r\times\sqrt{\pi}$')):
    disc(ax,22,cy,r,'sujet'); c=r*k
    ax.add_patch(Rectangle((60-c/2,cy-c/2),c,c,ec=COL['resultat'],fc=FILL['resultat'],lw=1.0,zorder=2))
    text(ax,41,cy,'=','encre','l'); text(ax,60,cy+c/2+3,'$c$','resultat','m')
    if cy==68: text(ax,44,cy-13,l1,'encre','m')
    else: text(ax,44,12,l1,'encre','m'); text(ax,44,6.5,l2,'resultat','m')
save(fig,'61-011')
