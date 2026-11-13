import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(76)
o=(24,38); u=8
P=lambda x,y,z: iso(x,y,z,o,u)
def pl(pts,role,a=0.55): ax.add_patch(Polygon(pts,closed=True,ec=COL[role],fc=FILL[role],alpha=a,lw=0.9,zorder=1.5))
pl([P(-1.5,-1.5,0),P(1.5,-1.5,0),P(1.5,1.5,0),P(-1.5,1.5,0)],'sujet')
pl([P(0,0,0),P(0,1.5,0),P(0,1.5,2),P(0,0,2)],'limite',0.45)
arrow(ax,P(0,0,0),P(0,0,2.3),'resultat',lw=1.8)
arrow(ax,P(0,0,0),P(1.2,-0.4,2.0),'resultat',lw=1.8)
text(ax,P(-1.5,-1.5,0)[0]-1,P(-1.5,-1.5,0)[1]-3,'U : plan, dim 2','sujet','s',ha='left')
text(ax,6,66,'complément de U ?','encre','s',ha='left')
for i,(t,r) in enumerate((('axe vertical : oui','resultat'),('droite oblique : oui','resultat'),('plan vertical : non','limite'))):
    line(ax,[(52,56-i*10),(58,56-i*10)],r,lw=2.0); text(ax,60,56-i*10,t,r,'s',ha='left')
text(ax,69,24,'le plan vertical coupe','limite','s'); text(ax,69,19,'U selon une droite','limite','s')
save(fig,'80-070')
