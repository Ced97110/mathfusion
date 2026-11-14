import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
fig,ax=canvas(62)
V=(10,8); L=56
pt=lambda r,a:(V[0]+r*math.cos(math.radians(a)),V[1]+r*math.sin(math.radians(a)))
line(ax,[V,pt(L,0)],'sujet',lw=1.3); line(ax,[V,pt(L,60)],'sujet',lw=1.3)
P=pt(22,0); Q=pt(22,60); R=pt(38.1,30)
ax.add_patch(Arc(V,44,44,theta1=-6,theta2=66,ec=COL['fixe'],lw=0.9,zorder=3))
ax.add_patch(Arc(P,44,44,theta1=40,theta2=80,ec=COL['varie'],lw=0.9,zorder=3))
ax.add_patch(Arc(Q,44,44,theta1=-12,theta2=12,ec=COL['varie'],lw=0.9,zorder=3))
line(ax,[V,R],'resultat',lw=1.3,dash=True)
for p in (P,Q,R): disc(ax,*p,1.3,'resultat')
text(ax,P[0]+2,P[1]-3.5,'P','encre'); text(ax,Q[0]-3.5,Q[1]+1.5,'Q','encre'); text(ax,R[0]+3.5,R[1]+1,'R','encre')
text(ax,*pt(32,13),'30°','resultat','s'); text(ax,*pt(32,47),'30°','resultat','s')
text(ax,68,53,'60° → 30° + 30°','encre','m'); text(ax,68,13,'R : 2 arcs qui se coupent','varie','s')
save(fig,'61-255')
