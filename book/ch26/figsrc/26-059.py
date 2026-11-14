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

fig,ax=canvas(72)
u=26.0
P=(8,14); Cv=(8+u,14); Q=(8+u,14+u)
poly(ax,[P,Cv,Q],'fixe'); rmark(ax,Cv,(-1,0),(0,1))
line(ax,[Cv,Q],'sujet',lw=1.8); line(ax,[P,Q],'autre',lw=1.8)
arc(ax,P,0,45,8,'varie'); text(ax,*polar(P,13,22.5),'45°','varie','s')
text(ax,*mid_off(Cv,Q,-3),'1','sujet'); text(ax,*mid_off(P,Cv,-3),'1'); text(ax,*mid_off(P,Q,3.5),r'$\sqrt{2}$','autre')
text(ax,65,63,'1. opposé ÷ hypoténuse','fixe','s')
text(ax,65,53,r'$\sin45^\circ=\frac{1}{\sqrt{2}}$','encre','l')
text(ax,65,41,r'2. haut et bas $\times\sqrt{2}$','fixe','s')
text(ax,65,30,r'$=\frac{1\times\sqrt{2}}{\sqrt{2}\times\sqrt{2}}$','encre','l')
text(ax,65,18,'3. même nombre','fixe','s')
text(ax,65,9,r'$=\frac{\sqrt{2}}{2}\approx0{,}7071$','resultat','l')
save(fig,'26-059')
