import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
import math
fig,ax=canvas(76)
u=6.5; ox,oy=8,24
P=lambda x,y:(ox+x*u,oy+y*u)
poly(ax,[P(0,0),P(8,0),P(8,6)],'sujet')
poly(ax,[P(0,0),P(8,0),P(8,6.1)],'limite',fill=False,lw=0.6)
text(ax,20,66,'8 et 6','sujet','s'); text(ax,20,60,'8 et 6,1','limite','s')
text(ax,73,70,'écart : 1 mm','limite','s'); arrow(ax,(70,67.5),(61,63),'limite')
text(ax,28,13,'6/8 = 0,75','sujet','m'); text(ax,66,13,'6,1/8 = 0,7625','limite','m')
text(ax,47,13,r'$\neq$','encre','l'); text(ax,44,5,'le dessin ne distingue pas les deux','fixe','s')
save(fig,'25-034')
