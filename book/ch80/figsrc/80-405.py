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
fig, ax = canvas(84)
N={1:(44,14),2:(22,36),3:(66,36),6:(44,58)}
ph={1:1,2:1,3:2,6:2}
for a,b in ((1,2),(1,3),(2,6),(3,6)): link(ax,N[a],N[b],4.2)
for d,(x,y) in N.items(): disc(ax,x,y,4.2,'varie' if d==6 else 'sujet',label=str(d))
for d,side in ((1,1),(2,-1),(3,1),(6,1)):
    x,y=N[d]; bx=x+4.2+2 if side>0 else x-4.2-2-13
    box(ax,bx,y-3.5,13,7,'resultat',label=r'$\varphi=%d$'%ph[d],size='s')
text(ax,44,76,r'$g(6)=1+1+2+2=6$','resultat','m')
save(fig, '80-405')
