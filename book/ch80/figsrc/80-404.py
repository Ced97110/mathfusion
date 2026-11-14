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
def row(y,groups,labs,title,ty):
    x=5
    for gi,(n,role) in enumerate(groups):
        x0=x
        for k in range(n): box(ax,x,y,5,5,role,r=0.5); x+=6
        if labs[gi] is not None or True:
            brace(ax,x0,x-1.0,y-2,role,label=labs[gi])
        x+=3
    text(ax,44,ty,title,'encre','m')
row(48,[(6,'sujet'),(6,'autre')],['6','6'],r'$6\mid12$ car $12=6\times2$',64)
row(24,[(5,'sujet'),(5,'autre'),(2,'limite')],['5','5',None],r'$5\nmid12$ : il reste 2',8)
save(fig, '80-404')
