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
fig, ax = canvas(60)
text(ax,27,44,r'$\mu($','sujet','l',ha='right')
box(ax,28,39.5,8,9,'fixe',label='1')
text(ax,39,44,',','encre','l')
box(ax,42,39.5,12,9,'sujet',label='12')
text(ax,57,44,r'$)$','sujet','l')
text(ax,32,32,'toujours 1','fixe','s'); text(ax,49,32,'le nombre','sujet','s')
arrow(ax,(46,28),(46,20),'varie',lw=1.2); text(ax,62,24,'on retire le 1','varie','s',ha='left')
text(ax,41,11,r'$\mu($','sujet','l',ha='right')
box(ax,42,6.5,12,9,'sujet',label='12')
text(ax,57,11,r'$)$','sujet','l')
save(fig, '80-399')
