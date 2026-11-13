import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Circle
fig,ax=canvas(60)
for x,s in [(6,'dim.'),(34,'lundi'),(62,'mardi')]: box(ax,x,40,16,7,'fixe',label=s,size='s')
arrow(ax,(22,43.5),(34,43.5),'varie'); arrow(ax,(50,43.5),(62,43.5),'varie')
box(ax,33,39,18,9,'limite',fill=False)
text(ax,42,54,'lundi : pas un début','limite','s')
f=numberline(ax,22,70,16,0,4)
for k in range(4): arrow(ax,(f(k),17.5),(f(k+1),17.5),'varie',curve=-0.5)
disc(ax,22,16,1.8,'sujet')
text(ax,22,7,'début','sujet','s')
ax.add_patch(Circle((10,16),3,ec=COL['limite'],fc='none',lw=0.8,ls='--',zorder=2))
text(ax,10,16,'?','limite','m')
arrow(ax,(13,17.5),(21,17.5),'limite',curve=-0.5)
d=1.2/2**0.5
line(ax,[(17-d,20.5-d),(17+d,20.5+d)],'limite',lw=1.1)
line(ax,[(17-d,20.5+d),(17+d,20.5-d)],'limite',lw=1.1)
text(ax,16,30,"rien n'arrive sur 0",'limite','s')
save(fig,'01-034')
