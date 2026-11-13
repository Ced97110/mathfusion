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
f=numberline(ax,8,78,18,0,1,step=0.1,every=5,arrow_right=False)
X=f(0.7071)
disc(ax,X,18,1.6,'resultat')
box(ax,4,38,36,16,'sujet'); text(ax,22,49.5,r'$1/\sqrt{2}$','sujet','m'); text(ax,22,42.5,'1 ÷ 1,41421','sujet','s')
box(ax,48,38,36,16,'autre'); text(ax,66,49.5,r'$\sqrt{2}/2$','autre','m'); text(ax,66,42.5,'1,41421 ÷ 2','autre','s')
text(ax,44,46,'=','encre','l')
arrow(ax,(22,38),(X-2,20.5),'sujet',curve=0.3); arrow(ax,(66,38),(X+2,20.5),'autre',curve=-0.3)
text(ax,X,9.5,'0,7071','resultat','m')
save(fig,'26-061')
