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
fig, ax = canvas(72)
cells={(0,0):1,(1,0):2,(2,0):4,(0,1):3,(1,1):6,(2,1):12}
X=lambda a:22+20*a; Y=lambda b:12+26*b
for (a,b),d in cells.items():
    box(ax,X(a),Y(b),14,14,'varie' if d==6 else 'sujet',label=str(d))
for b in (0,1):
    for a in (0,1): arrow(ax,(X(a)+14,Y(b)+7),(X(a+1),Y(b)+7),'fixe',lw=0.8)
for a in range(3): arrow(ax,(X(a)+7,Y(0)+14),(X(a)+7,Y(1)),'fixe',lw=0.8)
for a in range(3): text(ax,X(a)+7,58,f'a = {a}','sujet','s')
for b in (0,1): text(ax,10,Y(b)+7,f'b = {b}','sujet','s')
text(ax,50,3.5,r'$6 = 2^1\times3^1$','varie','m')
save(fig, '80-394')
