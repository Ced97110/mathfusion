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
fig, ax = canvas(62)
rows=[(48,'4 =',[2,2],1),(32,'12 =',[2,2,3],1),(16,'18 =',[2,3,3],2)]
for y,lab,ps,st in rows:
    text(ax,18,y,lab,'encre','m',ha='right')
    for i,p in enumerate(ps):
        rep = (i>=st and ps[i]==ps[i-1]) or (i<len(ps)-1 and ps[i]==ps[i+1])
        disc(ax,26+11*i,y,4.2,'varie' if rep else 'sujet',label=str(p))
    k=[i for i in range(len(ps)-1) if ps[i]==ps[i+1]][0]
    box(ax,26+11*k-5.6,y-5.6,11*1+11.2,11.2,'limite',fill=False,dash=True)
    text(ax,72,y,r'$\mu=0$','fixe','m',weight='bold')
save(fig, '80-398')
