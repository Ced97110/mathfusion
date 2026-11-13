import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(90)
def link(p,q,r1,r2,role="fixe",lw=1.0):
    dx,dy=q[0]-p[0],q[1]-p[1]; d=math.hypot(dx,dy); ux,uy=dx/d,dy/d
    arrow(ax,(p[0]+ux*r1,p[1]+uy*r1),(q[0]-ux*r2,q[1]-uy*r2),role,lw)
ys=[62-i*9 for i in range(6)]; xl,xr=17,71
box(ax,6,10,22,60,'sujet',fill=False,lw=1.0); box(ax,60,10,22,60,'resultat',fill=False,lw=1.0)
text(ax,17,75,r'$D^*$','sujet','l'); text(ax,71,75,r'$D^*$','resultat','l')
text(ax,44,85,r'$\lambda_3 : x\mapsto 3x$','varie','l')
for v in range(1,7):
    lab = v in (1,4,5); rr = v in (3,5,1)
    disc(ax,xl,ys[v-1],3 if lab else 1.5,'sujet' if lab else 'fixe',label=str(v) if lab else None)
    disc(ax,xr,ys[v-1],3 if rr else 1.5,'resultat' if rr else 'fixe',label=str(v) if rr else None)
for v,w in ((1,3),(4,5),(5,1)):
    link((xl,ys[v-1]),(xr,ys[w-1]),3,3,'varie',1.2)
save(fig,'51-228')
