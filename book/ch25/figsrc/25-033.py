import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
import math
fig,ax=canvas(66)
u=5.2; ox,oy=6,12
P=lambda x,y:(ox+x*u,oy+y*u)
for k in (3,2):
    poly(ax,[P(0,0),P(4*k,0),P(4*k,3*k)],'varie',fill=False)
poly(ax,[P(0,0),P(4,0),P(4,3)],'sujet')
for k,(a,b) in {1:(4,3),2:(8,6),3:(12,9)}.items():
    r='sujet' if k==1 else 'varie'
    text(ax,ox+4*k*u/2 if k==1 else ox+4*k*u-2*u,oy-3.2,str(a),r,'s')
    text(ax,ox+4*k*u+3,oy+3*k*u/2,str(b),r,'s')
text(ax,17,31,r'$k = 1$','sujet','s'); text(ax,56,46,r'$k = 2$','varie','s'); text(ax,78,60.5,r'$k = 3$','varie','s')
text(ax,44,4,'les deux côtés sont multipliés par k','fixe','s')
save(fig,'25-033')
