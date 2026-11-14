import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
D=[1,2,3,4,6,12]
P={1:(0,0),2:(-1,1),3:(1,1),4:(-2,2),6:(0,2),12:(-1,3)}
E=[(1,2),(1,3),(2,4),(2,6),(3,6),(4,12),(6,12)]
MU={1:1,2:-1,3:-1,4:0,6:1,12:0}
def sg(v): return '+1' if v>0 else ('−1' if v<0 else '0')
def vr(v): return 'sujet'
def mut(v): return r'$\mu=+1$' if v>0 else (r'$\mu=-1$' if v<0 else r'$\mu=0$')
def link(ax,p,q,r,role='fixe',ar=False,lw=0.9):
    dx,dy=q[0]-p[0],q[1]-p[1]; n=math.hypot(dx,dy); ux,uy=dx/n,dy/n
    a=(p[0]+ux*r,p[1]+uy*r); b=(q[0]-ux*r,q[1]-uy*r)
    if ar: arrow(ax,a,b,role,lw=lw)
    else: line(ax,[a,b],role,lw=lw)
def pos(d,ox,oy,sx,sy): return (ox+P[d][0]*sx, oy+P[d][1]*sy)
fig, ax = canvas(74)
def dia(cx,ds,mus):
    r=5.2
    N=[(cx,12),(cx-12,34),(cx+12,34),(cx,56)]
    for a,b in ((0,1),(0,2),(1,3),(2,3)): link(ax,N[a],N[b],r)
    for (x,y),d,m in zip(N,ds,mus): disc(ax,x,y,r,vr(m),label=f'{d}\n{sg(m)}',size='s')
dia(21,[1,2,3,6],[1,-1,-1,1]); dia(67,[2,4,6,12],[1,-1,-1,1])
text(ax,44,36,'=','resultat','xl',weight='bold'); text(ax,44,22,'mêmes valeurs','resultat','s')
text(ax,21,67,r'valeurs de $\mu(1,d)$','sujet','s'); text(ax,67,67,r'valeurs de $\mu(2,d)$','sujet','s')
text(ax,21,3.5,r'$6\div1=6$','encre','s'); text(ax,67,3.5,r'$12\div2=6$','encre','s')
save(fig, '80-396')
