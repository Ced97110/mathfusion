import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(90)
def link(p,q,r1,r2,role="fixe",lw=1.0):
    dx,dy=q[0]-p[0],q[1]-p[1]; d=math.hypot(dx,dy); ux,uy=dx/d,dy/d
    arrow(ax,(p[0]+ux*r1,p[1]+uy*r1),(q[0]-ux*r2,q[1]-uy*r2),role,lw)
xl,xr,r=24,64,3.4
y=lambda v:70-(v-1)*11
f=lambda v:(3*v)%7
text(ax,xl,81,r'$x$','sujet','l'); text(ax,xr,81,r'$3x$','resultat','l')
for v in range(1,7):
    if v!=5: link((xl,y(v)),(xr,y(f(v))),r,r,'sujet',0.9)
link((xl,y(5)),(xr,y(1)),r,r,'resultat',1.8)
for v in range(1,7):
    disc(ax,xl,y(v),r,'sujet',label=str(v))
    disc(ax,xr,y(v),r,'resultat' if v==1 else 'fixe',label=str(v))
save(fig,'51-224')
