import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
D=[1,2,3,4,6,12]
P={1:(0,0),2:(-1,1),3:(1,1),4:(-2,2),6:(0,2),12:(-1,3)}
E=[(1,2),(1,3),(2,4),(2,6),(3,6),(4,12),(6,12)]
MU={1:1,2:-1,3:-1,4:0,6:1,12:0}
def sg(v): return '+1' if v>0 else ('−1' if v<0 else '0')
def vr(v): return 'resultat' if v>0 else ('limite' if v<0 else 'fixe')
def mut(v): return r'$\mu=+1$' if v>0 else (r'$\mu=-1$' if v<0 else r'$\mu=0$')
def link(ax,p,q,r,role='fixe',ar=False,lw=0.9):
    dx,dy=q[0]-p[0],q[1]-p[1]; n=math.hypot(dx,dy); ux,uy=dx/n,dy/n
    a=(p[0]+ux*r,p[1]+uy*r); b=(q[0]-ux*r,q[1]-uy*r)
    if ar: arrow(ax,a,b,role,lw=lw)
    else: line(ax,[a,b],role,lw=lw)
def pos(d,ox,oy,sx,sy): return (ox+P[d][0]*sx, oy+P[d][1]*sy)
fig, ax = canvas(60)
facs=['1',r'$2$',r'$3$',r'$2\times2$',r'$2\times3$',r'$2\times2\times3$']
for i,d in enumerate(D):
    x=11+13.2*i; v=MU[d]
    disc(ax,x,44,5,vr(v),label=sg(v),weight='bold') if False else disc(ax,x,44,5,vr(v),label=sg(v))
    arrow(ax,(x,38.5),(x,28),'fixe',lw=0.7)
    text(ax,x,23,facs[i],'sujet','s')
text(ax,44,8,'un carré dans le produit : 0','limite','s')
save(fig, '80-393')
