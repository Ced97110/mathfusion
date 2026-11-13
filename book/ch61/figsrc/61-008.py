import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
fig,ax=canvas(60)
V=(8,8); L=52
pt=lambda r,a:(V[0]+r*math.cos(math.radians(a)),V[1]+r*math.sin(math.radians(a)))
line(ax,[V,pt(L,0)],'sujet',lw=1.3); line(ax,[V,pt(L,60)],'sujet',lw=1.3)
for a in (20,40): line(ax,[V,pt(L,a)],'varie',dash=True,lw=1.0)
ax.add_patch(Arc(V,88,88,theta1=0,theta2=60,ec=COL['sujet'],lw=0.9,zorder=3))
text(ax,*pt(49,30),'60°','sujet','m',weight='bold')
for a in (10,30,50): text(ax,*pt(32,a),'?','varie','l',weight='bold')
text(ax,70,53,'But : 3 angles égaux','varie','m'); text(ax,70,48,'de 20° chacun ?','varie','m')
text(ax,70,14,'condition :','limite','s'); text(ax,70,10,'règle + compas seuls','limite','s')
save(fig,'61-008')
