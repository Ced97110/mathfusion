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

fig,ax=canvas(66)
u=1.55
d=math.sqrt(224); P=(6,10); Cv=(6+d*u,10); Q=(Cv[0],10+26*u)
line(ax,[P,Cv],'fixe'); line(ax,[Cv,Q],'fixe'); line(ax,[P,Q],'sujet',lw=1.8)
rmark(ax,Cv,(-1,0),(0,1))
arc(ax,P,0,60.07,8,'sujet'); text(ax,*polar(P,13,30),r'$\theta$','sujet','m')
text(ax,*mid_off(Cv,Q,-5),'26 m'); text(ax,*mid_off(P,Q,5),'30 m','sujet')
box(ax,46,48,40,9,'fixe',label=r'$\sin\theta=26/30$')
box(ax,46,30,40,9,'fixe',label=r'$\theta=\arcsin(0{,}8666\ldots)$',size='s')
box(ax,46,12,40,9,'resultat',label=r'$\theta\approx60^\circ$ (arrondi)',size='s')
arrow(ax,(66,48),(66,39.5),'fixe'); arrow(ax,(66,30),(66,21.5),'fixe')
save(fig,'26-053')
