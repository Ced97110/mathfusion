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
fig, ax = canvas(88)
ds=[1,2,3,5,6,10,15,30]; mus=[1,-1,-1,-1,1,1,1,-1]; base=40; k=0.8
line(ax,[(3,base),(85,base)],'fixe')
text(ax,44,84,r'$\mu(d)\times30/d$','encre','m')
for i,(d,m) in enumerate(zip(ds,mus)):
    x=8+10.3*i; t=m*30//d; h=abs(t)*k
    ax.add_patch(Rectangle((x-3,base if t>0 else base-h),6,h,ec=COL['resultat' if t>0 else 'limite'],fc=FILL['resultat' if t>0 else 'limite'],lw=0.6,zorder=2))
    text(ax,x,73,f'$d={d}$\n'+('+' if t>0 else '−')+str(abs(t)),vr(m),'s')
text(ax,44,12,r'$30-15-10-6+5+3+2-1=8$','resultat','m')
save(fig, '80-408')
