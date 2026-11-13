import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(80)
# haut : restes positifs ou nuls
text(ax,2,74,'restes ≥ 0 : arrêt à 0','resultat','m',ha='left',weight='bold')
f=numberline(ax,6,76,52,0,54,step=18,arrow_right=False)
pts=[54,36,18,0]
for a,b in zip(pts,pts[1:]): arrow(ax,(f(a),55),(f(b)+1,55),'resultat',curve=0.5)
for v in pts: disc(ax,f(v),52,1.6,'resultat')
# bas : négatifs permis
text(ax,2,36,'négatifs permis : sans fin','limite','m',ha='left',weight='bold')
g=numberline(ax,14,80,14,-6,6,step=1,labels=False,arrow_right=False)
arrow(ax,(14,14),(3,14),'limite')
vals=[5,3,1,-1,-3,-5]
for a,b in zip(vals,vals[1:]): arrow(ax,(g(a),17),(g(b)+1,17),'limite',curve=0.5)
for v in vals:
    disc(ax,g(v),14,1.6,'limite')
    text(ax,g(v),9.5,str(v).replace('-','−'),'limite','s')
text(ax,g(0),21.5,'0','encre','s')
ax.plot([g(0),g(0)],[10.5,20],color=COL['encre'],lw=0.8,zorder=1.5)
save(fig,'05-086')
