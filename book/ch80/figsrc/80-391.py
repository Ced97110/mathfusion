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
r=4.4
N={1:(44,10),2:(22,32),3:(66,32),6:(44,54)}
for a,b in ((1,2),(1,3),(2,6),(3,6)): link(ax,N[a],N[b],r,'fixe')
for d,(x,y) in N.items(): disc(ax,x,y,r,'varie' if d==6 else 'sujet',label=str(d))
text(ax,39,10,'+1','resultat','m',ha='right',weight='bold')
text(ax,16,32,'−1','limite','m',ha='right',weight='bold')
text(ax,71.5,32,'−1','limite','m',ha='left',weight='bold')
text(ax,39,54,r'$\mu(1,6)=1$','resultat','s',ha='right',weight='bold')
text(ax,66,10,r'somme : $1-1-1=-1$','varie','s')
text(ax,70,54,'puis l’opposé','varie','s',ha='left')
save(fig, '80-391')
