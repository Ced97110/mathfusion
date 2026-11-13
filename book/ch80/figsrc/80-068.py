import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
o=(28,24); u=13
P=lambda x,y,z: iso(x,y,z,o,u)
def pl(pts,role): ax.add_patch(Polygon(pts,closed=True,ec=COL[role],fc=FILL[role],alpha=0.55,lw=0.8,zorder=1.5))
pl([P(-0.2,-0.2,0),P(1.4,-0.2,0),P(1.4,1.4,0),P(-0.2,1.4,0)],'sujet')
pl([P(-0.2,0,-0.2),P(1.4,0,-0.2),P(1.4,0,1.4),P(-0.2,0,1.4)],'autre')
arrow(ax,P(0,0,0),P(1,0,0),'resultat',lw=1.8); arrow(ax,P(0,0,0),P(0,1,0),'sujet',lw=1.8); arrow(ax,P(0,0,0),P(0,0,1),'autre',lw=1.8)
text(ax,P(1,0,0)[0]+2,P(1,0,0)[1]-4,'(1, 0, 0)','resultat','s',ha='left')
text(ax,P(0,1,0)[0]-1,P(0,1,0)[1]+3,'(0, 1, 0)','sujet','s',ha='right')
text(ax,P(0,0,1)[0]-2,P(0,0,1)[1]+3,'(0, 0, 1)','autre','s',ha='right')
for i,(t,r) in enumerate((('base de U ∩ W','resultat'),('ajouté dans U','sujet'),('ajouté dans W','autre'))):
    disc(ax,62,52-i*11,2.0,r); text(ax,66,52-i*11,t,r,'s',ha='left')
text(ax,44,60,'on complète la base de U ∩ W','encre','s')
text(ax,44,6,'les trois : une base de U + W','resultat','s')
save(fig,'80-068')
