import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(84)
o=(32,50); u=9
def P(x,y,z): return iso(x,y,z,o,u)
def pl(pts,role):
    ax.add_patch(Polygon(pts,closed=True,ec=COL[role],fc=FILL[role],alpha=0.6,lw=0.9,zorder=2))
pl([P(0,-1.5,0),P(3,-1.5,0),P(3,1.5,0),P(0,1.5,0)],'sujet')
pl([P(0,0,-1.5),P(3,0,-1.5),P(3,0,1.5),P(0,0,1.5)],'autre')
ax.plot(*zip(P(0,0,0),P(3,0,0)),color=COL['resultat'],lw=2.4,zorder=4,solid_capstyle='round')
text(ax,P(3,-1.5,0)[0]+2,P(3,-1.5,0)[1]-1,'plan U','sujet','m',ha='left')
text(ax,P(3,0,1.5)[0]+2,P(3,0,1.5)[1],'plan W','autre','m',ha='left')
text(ax,P(3,0,0)[0]+3,P(3,0,0)[1]+4,r'$U\cap W$','resultat','m',ha='left')
text(ax,44,16,'une droite, dans U et dans W','resultat','s')
text(ax,44,8,'inf : le plus grand sous-espace commun','encre','s')
save(fig,'80-054')
