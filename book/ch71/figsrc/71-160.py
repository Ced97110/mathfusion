import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig,ax=canvas(72)
text(ax,44,69,r'$5X^2+\frac{16}{5}Y^2=4$','sujet','m')
c=(34,38); a=0.894*20; b=1.118*20
ax.add_patch(Rectangle((c[0]-a,c[1]-b),2*a,2*b,fill=False,ec=COL['fixe'],lw=0.8,ls='--',zorder=1))
arrow(ax,(6,c[1]),(62,c[1]),'fixe',lw=0.8); arrow(ax,(c[0],12),(c[0],64),'fixe',lw=0.8)
line(ax,[(c[0]+a*math.cos(t*math.pi/90),c[1]+b*math.sin(t*math.pi/90)) for t in range(181)],'resultat',lw=1.6)
text(ax,65,c[1]-3,r'$X$','fixe','m'); text(ax,c[0]+3,64,r'$Y$','fixe','m')
text(ax,c[0],8,r'$X^2\leq0{,}8$','varie','m'); text(ax,54,52,r'$Y^2\leq1{,}25$','varie','m',ha='left')
text(ax,54,24,'courbe fermée','resultat','m',ha='left')
save(fig,'71-160')
