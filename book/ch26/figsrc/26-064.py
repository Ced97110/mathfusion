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
u=22.0
Bv=(8,12); Cv=(8+2*u,12); A=(8+u,12+math.sqrt(3)*u); H=(A[0],12)
poly(ax,[Bv,H,A],'fixe'); poly(ax,[H,Cv,A],'sujet')
line(ax,[A,H],'varie',lw=1.3,dash=True); rmark(ax,H,(1,0),(0,1))
arc(ax,Bv,0,60,7,'fixe'); text(ax,*polar(Bv,13,30),'60°','fixe','s')
arc(ax,Cv,120,180,7,'sujet'); text(ax,*polar(Cv,13,150),'60°','sujet','s')
arc(ax,A,-120,-90,9,'fixe'); text(ax,*polar(A,19,-105),'30°','fixe','s')
arc(ax,A,-90,-60,9,'sujet'); text(ax,*polar(A,19,-75),'30°','sujet','s')
text(ax,Bv[0]+u/2,8.5,'1','fixe'); text(ax,H[0]+u/2,8.5,'1','sujet')
text(ax,*mid_off(Cv,A,-3.5),'2'); text(ax,H[0]+2.8,22,r'$h$','varie','m')
box(ax,56,38,30,12,'varie'); text(ax,71,46,'symétrie :','varie','s'); text(ax,71,41.5,'base : 1 et 1','varie','s')
box(ax,56,22,30,10,'resultat',label=r'$h^2=2^2-1^2=3$',size='s')
box(ax,56,6,30,10,'resultat',label=r'$h=\sqrt{3}$')
arrow(ax,(71,38),(71,32.5),'fixe'); arrow(ax,(71,22),(71,16.5),'fixe')
save(fig,'26-064')
