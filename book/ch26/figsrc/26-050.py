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

fig,ax=canvas(56)
u=21.0
P=(8,26); C=(P[0]+math.sqrt(3)*u,26); Q=(C[0],26+u)
poly(ax,[P,C,Q],'fixe'); rmark(ax,C,(-1,0),(0,1))
arc(ax,P,0,30,9,'sujet'); text(ax,*polar(P,15,15),'30°','sujet','s')
text(ax,*mid_off(P,C,-3.5),r'$\sqrt{3}$'); text(ax,*mid_off(C,Q,-3),'1'); text(ax,*mid_off(P,Q,3.5),'2')
text(ax,44,17,r'$\sin 30^\circ=1/2=0{,}5$','resultat','m')
box(ax,6,3,76,9,'sujet',label=r'$\arcsin(0{,}5)=30^\circ$')
save(fig,'26-050')
