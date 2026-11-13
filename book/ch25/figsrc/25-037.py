import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
import math
fig,ax=canvas(78)
u=5.5; ox,oy=10,14
P=lambda x,y:(ox+x*u,oy+y*u)
arrow(ax,(ox,oy),(ox+72,oy),'fixe')
line(ax,[P(0,0),P(12,9)],'encre',lw=1.2)
line(ax,[P(0,0),P(9,9)],'autre',dash=True)
for v in (4,8,10,12):
    line(ax,[P(v,0),P(v,0.75*v)],'varie',lw=1.6); text(ax,ox+v*u,oy-3.2,str(v),'fixe','s')
text(ax,ox-3,oy-3.2,'A','encre','s')
text(ax,30,68,'autre angle, autre rapport','autre','s')
text(ax,48,5,'orange ÷ bleu = 0,75 partout','resultat','s')
save(fig,'25-037')
