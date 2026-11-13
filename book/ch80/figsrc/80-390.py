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
fig, ax = canvas(80)
ys={1:12,2:38,4:64}
for d in (1,2,4): disc(ax,24,ys[d],4.5,'sujet' if d!=4 else 'varie',label=str(d))
arrow(ax,(24,16.5),(24,33.5),'varie'); arrow(ax,(24,42.5),(24,59.5),'varie')
text(ax,33,12,r'$\mu(1,1)=1$','resultat','s',ha='left')
text(ax,33,38,r'$\mu(1,2)=-1$','limite','s',ha='left')
text(ax,33,64,r'$\mu(1,4)=0$','fixe','s',ha='left',weight='bold')
box(ax,56,20,30,22,'varie')
text(ax,71,35,'somme sous 4','varie','s'); text(ax,71,27,r'$1+(-1)=0$','varie','m')
save(fig, '80-390')
