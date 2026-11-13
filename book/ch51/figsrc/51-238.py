import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(100)
def link(p,q,r1,r2,role="fixe",lw=1.0):
    dx,dy=q[0]-p[0],q[1]-p[1]; d=math.hypot(dx,dy); ux,uy=dx/d,dy/d
    arrow(ax,(p[0]+ux*r1,p[1]+uy*r1),(q[0]-ux*r2,q[1]-uy*r2),role,lw)

xl,xr,r=24,64,3.4
yl=lambda v:76-(v-1)*12; yr=lambda w:82-w*12
text(ax,xl,92,r'$x$','sujet','l'); text(ax,xr,92,r'$2x$','fixe','l')
for v in range(1,6):
    w=(2*v)%6
    link((xl,yl(v)),(xr,yr(w)),r,r,'varie' if w==0 else 'limite',1.4 if w else 1.6)
for v in range(1,6): disc(ax,xl,yl(v),r,'sujet',label=str(v))
for w in range(6):
    hit=w%2==0
    disc(ax,xr,yr(w),r,('varie' if w==0 else 'limite') if hit else 'limite',fill=hit,label=str(w))
text(ax,44,8,'places vides : 1, 3 et 5','limite','m')
save(fig,'51-238')
