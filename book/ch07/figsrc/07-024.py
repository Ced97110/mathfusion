import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def row(ax,x,y,w,h,roles):
    for i,r in enumerate(roles):
        x0=x+i*w
        poly(ax,[(x0,y),(x0+w,y),(x0+w,y+h),(x0,y+h)],r or "fixe",fill=r is not None)
fig,ax=canvas(62)
text(ax,44,57,'3/7 + 2/7 = 5/7','encre','l')
f=numberline(ax,8,74,22,0,7,1)
arrow(ax,(f(0),25),(f(3),25),'sujet',curve=-0.35)
arrow(ax,(f(3),25),(f(5),25),'autre',curve=-0.45)
text(ax,f(1.5),37,'+3','sujet','m'); text(ax,f(4),35,'+2','autre','m')
ax.add_patch(Circle((f(5),22),1.8,ec=COL['resultat'],fc=FILL['resultat'],lw=1,zorder=4))
text(ax,44,43,'quantités : 3 + 2 = 5','encre','s')
text(ax,44,5,'unité : le septième, ne change pas','fixe','s')
save(fig,'07-024')
