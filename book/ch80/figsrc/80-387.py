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
fig, ax = canvas(74)
rows=[(1,r'$\mu(1,1)=1$'),(2,r'$\mu(1,2)=-(1)=-1$'),(3,r'$\mu(1,3)=-(1)=-1$'),(4,r'$\mu(1,4)=-(1-1)=0$'),(6,r'$\mu(1,6)=-(1-1-1)=1$'),(12,r'$\mu(1,12)=-(1-1-1+0+1)=0$')]
for i,(d,f) in enumerate(rows):
    y=8+11*i
    disc(ax,9,y,4.2,'sujet',label=str(d))
    text(ax,17,y,f,vr(MU[d]),'s',ha='left')
arrow(ax,(83,8),(83,63),'varie',lw=1.2)
text(ax,78.5,35.5,'on monte','varie','s',rot=90)
save(fig, '80-387')
