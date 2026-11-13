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
fig, ax = canvas(92)
r=5.5
names={1:(44,12),2:(22,34),3:(44,34),5:(66,34),6:(22,56),10:(44,56),15:(66,56),30:(44,78)}
mu={1:1,2:-1,3:-1,5:-1,6:1,10:1,15:1,30:-1}
ed=[(1,2),(1,3),(1,5),(2,6),(2,10),(3,6),(3,15),(5,10),(5,15),(6,30),(10,30),(15,30)]
for a,b in ed: link(ax,names[a],names[b],r)
for d,(x,y) in names.items():
    disc(ax,x,y,r,'varie' if d==30 else 'sujet',label=f'{d}\n{sg(mu[d])}',size='s')
for yy,s in ((12,'0 premier'),(34,'1 premier'),(56,'2 premiers'),(78,'3 premiers')): text(ax,86,yy,s,'fixe','s',ha='right')
text(ax,44,89,r'$30=2\times3\times5$','encre','m')
save(fig, '80-401')
