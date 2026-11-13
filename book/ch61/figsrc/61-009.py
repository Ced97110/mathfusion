import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
fig,ax=canvas(56)
A=(31,10); B=(57,10); r=26; C=(44,10+r*math.sin(math.radians(60)))
poly(ax,[A,B,C],'fixe')
ax.add_patch(Arc(A,2*r,2*r,theta1=0,theta2=80,ec=COL['varie'],lw=0.9,zorder=3))
ax.add_patch(Arc(B,2*r,2*r,theta1=100,theta2=180,ec=COL['varie'],lw=0.9,zorder=3))
for p,q in ((A,B),(B,C),(C,A)): line(ax,[p,q],'sujet',lw=1.3)
for P,a0 in ((A,0),(B,120),(C,240)):
    ax.add_patch(Arc(P,12,12,theta1=a0,theta2=a0+60,ec=COL['resultat'],lw=1.8,zorder=4))
text(ax,44,5.5,'5 cm','sujet','s'); text(ax,31,25,'5 cm','sujet','s'); text(ax,57,25,'5 cm','sujet','s')
text(ax,38.5,14.5,'60°','resultat','s',weight='bold'); text(ax,49.5,14.5,'60°','resultat','s',weight='bold'); text(ax,44,28,'60°','resultat','s',weight='bold')
text(ax,44,50,'3 côtés égaux : 3 angles de 60°','encre','m')
save(fig,'61-009')
