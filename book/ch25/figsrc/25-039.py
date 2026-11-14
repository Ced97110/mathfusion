import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
import math
fig,ax=canvas(62)
ox,oy=40,8
d=lambda a,L:(ox+L*math.cos(math.radians(a)),oy+L*math.sin(math.radians(a)))
line(ax,[(ox-28,oy),(ox+44,oy)],'fixe')
line(ax,[(ox,oy),d(40,34)],'sujet',lw=1.3); line(ax,[(ox,oy),d(50,34)],'sujet',lw=1.3)
line(ax,[(ox,oy),d(135,34)],'limite',lw=1.3)
ax.add_patch(Arc((ox,oy),36,36,theta1=0,theta2=40,color=COL['sujet'],lw=0.8))
ax.add_patch(Arc((ox,oy),24,24,theta1=0,theta2=50,color=COL['sujet'],lw=0.8))
ax.add_patch(Arc((ox,oy),16,16,theta1=0,theta2=135,color=COL['limite'],lw=0.8))
text(ax,74,28,'40°','sujet','s'); text(ax,63,39,'50°','sujet','s')
text(ax,13,36,'135°','limite','s'); text(ax,14,28,'pente −1','limite','s')
text(ax,66,56,'angles aigus : règle vraie','resultat','s'); text(ax,20,56,'135° : règle fausse','limite','s')
save(fig,'25-039')
