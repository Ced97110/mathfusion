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
fig, ax = canvas(70)
text(ax,44,65,r'chaîne : $\mu(0,j)$','encre','s')
vals=[1,-1,0,0]
for j in range(4):
    x=16+18*j
    disc(ax,x,52,4.2,'sujet',label=str(j)); text(ax,x,41,sg(vals[j]),vr(vals[j]),'m',weight='bold')
    if j<3: arrow(ax,(x+4.4,52),(x+18-4.4,52),'varie')
ds=[1,2,6,30]
for j,d in enumerate(ds):
    x=16+18*j
    disc(ax,x,22,4.4,'sujet',label=str(d))
    if j<3: arrow(ax,(x+4.6,22),(x+18-4.6,22),'varie')
text(ax,44,8,r'3 pas, pourtant $\mu(1,30)=-1$','limite','s')
save(fig, '80-395')
