import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(80)
def link(p,q,r1,r2,role="fixe",lw=1.0):
    dx,dy=q[0]-p[0],q[1]-p[1]; d=math.hypot(dx,dy); ux,uy=dx/d,dy/d
    arrow(ax,(p[0]+ux*r1,p[1]+uy*r1),(q[0]-ux*r2,q[1]-uy*r2),role,lw)
box(ax,3,34,39,36,'autre',fill=False,lw=1.0); box(ax,46,34,39,36,'sujet',fill=False,lw=1.0)
text(ax,22.5,64,'Bézout','autre','l'); text(ax,22.5,52,r'$5\times3-2\times7=1$','autre','m'); text(ax,22.5,40,'vient des entiers','autre','s')
text(ax,65.5,64,'les flèches','sujet','l'); text(ax,65.5,40,'utilise l’anneau seul','sujet','s')
disc(ax,55,52,3.5,'sujet',label='5'); disc(ax,76,52,3.5,'resultat',label='1'); link((55,52),(76,52),3.5,3.5,'sujet',1.4)
box(ax,18,6,52,10,'resultat',label='3 a pour inverse 5')
arrow(ax,(22.5,33),(34,17),'autre',lw=1.2); arrow(ax,(65.5,33),(54,17),'sujet',lw=1.2)
save(fig,'51-234')
