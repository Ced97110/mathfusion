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
fig, ax = canvas(78)
box(ax,4,4,80,70,'fixe',fill=False,dash=True)
text(ax,44,68,'tout ensemble ordonné fini','fixe','s')
box(ax,10,10,48,50,'sujet')
cx=34; N={1:(cx,18),2:(cx-11,31),3:(cx+11,31),6:(cx,44)}
for a,b in ((1,2),(1,3),(2,6),(3,6)): link(ax,N[a],N[b],3.6,'sujet')
for d,(x,y) in N.items(): disc(ax,x,y,3.6,'sujet',label=str(d),size='s')
text(ax,34,54,'diviseurs d’un entier','sujet','s')
box(ax,62,44,20,11,'autre',fill=False,label='autre ordre',size='s',dash=True)
box(ax,62,29,20,11,'autre',fill=False,label='autre ordre',size='s',dash=True)
box(ax,62,12,20,11,'varie',label='1832',size='m')
arrow(ax,(62,17.5),(58.8,17.5),'varie')
save(fig, '80-400')
