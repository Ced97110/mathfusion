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
ds=D; ts=[12,-6,-4,0,2,0]; base=42; s=2.8
line(ax,[(3,base),(85,base)],'fixe')
for i,(d,t) in enumerate(zip(ds,ts)):
    x=10+13.6*i; m=(t>0)-(t<0); v=MU[d]
    for k in range(abs(t)):
        y=base+s*k if m>0 else base-s*(k+1)
        box(ax,x-s/2,y,s,s,'resultat' if m>0 else 'limite',r=0.3,lw=0.5)
    text(ax,x,88,r'$d=%d$'%d,'encre','s'); text(ax,x,82.5,mut(v),vr(v),'s')
text(ax,44,8,r'$12-6-4+0+2+0=4$','resultat','m')
save(fig, '80-407')
