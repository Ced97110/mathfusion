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
fig, ax = canvas(76)
for cx,t,pr,prod in ((22,'premiers distincts',(2,3),r'$6=2\times3$'),(66,'premiers égaux',(2,2),r'$4=2\times2$')):
    text(ax,cx,69,t,'encre','s')
    disc(ax,cx-7,52,5,'sujet',label=str(pr[0]))
    disc(ax,cx+7,52,5,'autre' if pr[1]==3 else 'sujet',label=str(pr[1]))
    text(ax,cx,39,prod,'encre','m')
    text(ax,cx,28,r'$(-1)^2=1$','resultat' if pr[1]==3 else 'limite','m')
    text(ax,cx,21,'formule juste' if pr[1]==3 else 'formule fausse','resultat' if pr[1]==3 else 'limite','s')
text(ax,22,8,r'$\mu(1,6)=1$','resultat','m'); text(ax,66,8,r'$\mu(1,4)=0$','resultat','m',weight='bold')
save(fig, '80-397')
