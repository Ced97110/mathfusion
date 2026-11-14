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
u=34.0
P=(8,12); Cv=(8+u,12); Q=(8+u,12+u); T=(8,12+u)
poly(ax,[P,T,Q],'fixe',fill=False); poly(ax,[P,Cv,Q],'sujet')
line(ax,[P,Q],'varie',lw=1.3); rmark(ax,Cv,(-1,0),(0,1))
arc(ax,P,0,45,9,'varie'); arc(ax,Q,225,270,9,'varie')
text(ax,*polar(P,17,22.5),'45°','varie','s'); text(ax,*polar(Q,17,247.5),'45°','varie','s')
text(ax,*mid_off(P,Cv,-3),'1'); text(ax,*mid_off(Cv,Q,-3),'1'); text(ax,*mid_off(P,Q,3.5),r'$\sqrt{2}$','resultat')
box(ax,50,38,36,10,'fixe',label='deux côtés égaux à 1',size='s')
box(ax,50,24,36,10,'varie',label='angles égaux : 45° chacun',size='s')
box(ax,50,10,36,10,'resultat',label=r'$c^2=1+1=2,\ c=\sqrt{2}$',size='s')
arrow(ax,(68,38),(68,34.5),'fixe'); arrow(ax,(68,24),(68,20.5),'fixe')
save(fig,'26-058')
