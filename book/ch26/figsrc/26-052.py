import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
import math
def arc(ax,p,a0,a1,r,role='sujet',lw=0.9):
    ax.add_patch(Arc(p,2*r,2*r,theta1=a0,theta2=a1,color=COL[role],lw=lw,zorder=3))
def rmark(ax,p,d1,d2,s=2.2,role='fixe'):
    line(ax,[(p[0]+d1[0]*s,p[1]+d1[1]*s),(p[0]+(d1[0]+d2[0])*s,p[1]+(d1[1]+d2[1])*s),(p[0]+d2[0]*s,p[1]+d2[1]*s)],role,lw=0.7)
def polar(p,r,a): return (p[0]+r*math.cos(math.radians(a)),p[1]+r*math.sin(math.radians(a)))
def mid_off(p,q,off):
    dx,dy=q[0]-p[0],q[1]-p[1]; n=math.hypot(dx,dy)
    return ((p[0]+q[0])/2-dy/n*off,(p[1]+q[1])/2+dx/n*off)

fig,ax=canvas(62)
u=4.4
Bv=(6,22); Cv=(6+8*u,22); A=(6+2.5*u,22+math.sqrt(18.75)*u)
poly(ax,[Bv,Cv,A],'fixe')
text(ax,*mid_off(Bv,Cv,-3),'8'); text(ax,*mid_off(Bv,A,3),'5'); text(ax,*mid_off(A,Cv,3),'7')
text(ax,24,12,"pas d'angle droit",'encre','s')
text(ax,66,57,'méthode en quatre temps','encre','m')
labs=["1 regarder l'angle",'2 nommer : impossible','3 choisir le rapport','4 écrire, résoudre']
for i,l in enumerate(labs):
    box(ax,48,44-i*12,38,9,'limite' if i==1 else 'fixe',label=l,size='s')
save(fig,'26-052')
