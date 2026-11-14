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
fig, ax = canvas(88)
ox,oy,sx,sy,r=30,14,11,19,4.0
for a,b in E: link(ax,pos(a,ox,oy,sx,sy),pos(b,ox,oy,sx,sy),r)
for d in D:
    x,y=pos(d,ox,oy,sx,sy); v=MU[d]
    disc(ax,x,y,r,'varie' if d==12 else vr(v),label=str(d))
    text(ax,x+r+4.5,y,sg(v),vr(v),'m',weight='bold')
text(ax,68,76,'somme sous 12 :','varie','s'); text(ax,68,68,r'$1-1-1+0+1=0$','varie','s')
save(fig, '80-392')
