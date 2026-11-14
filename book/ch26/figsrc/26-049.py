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
u=7.0
C=(36,12); P=(C[0]-4*u,12); Q=(C[0],12+3*u)
poly(ax,[P,C,Q],'fixe'); rmark(ax,C,(-1,0),(0,1))
arc(ax,P,0,36.87,7,'sujet'); arc(ax,Q,216.87,270,7,'autre')
text(ax,*mid_off(P,C,-3.2),'4'); text(ax,*mid_off(C,Q,-3.2),'3'); text(ax,*mid_off(P,Q,3.2),'5')
text(ax,P[0]+6,7,'36,87°','sujet','s'); text(ax,Q[0]+8.5,Q[1]-4,'53,13°','autre','s')
text(ax,69,50,'même nombre : 0,8','encre','m')
box(ax,52,28,34,9,'sujet',label=r'$\arccos(0{,}8)=36{,}87^\circ$',size='s')
box(ax,52,12,34,9,'autre',label=r'$\arcsin(0{,}8)=53{,}13^\circ$',size='s')
save(fig,'26-049')
