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
u=1.5
d=math.sqrt(224); P=(6,8); Cv=(6+d*u,8); Q=(Cv[0],8+26*u)
line(ax,[Cv,Q],'fixe'); line(ax,[P,Q],'fixe'); line(ax,[P,Cv],'sujet',lw=1.8)
rmark(ax,Cv,(-1,0),(0,1))
arc(ax,P,0,60.07,7,'autre'); text(ax,*polar(P,12,30),r'$\theta$','autre','m')
text(ax,*mid_off(P,Cv,-3.2),r'$d$','sujet','m'); text(ax,*mid_off(Cv,Q,-5),'26 m'); text(ax,*mid_off(P,Q,4.5),'30 m')
box(ax,42,36,20,14,'fixe'); text(ax,52,45,'Pythagore','fixe','s'); text(ax,52,40,r'$\sqrt{224}$','fixe','m')
box(ax,66,36,20,14,'autre'); text(ax,76,45,'Cosinus','autre','s'); text(ax,76,40,r'$30\cos\theta$','autre','m')
box(ax,46,10,38,13,'resultat',label=r'$d\approx14{,}966\ldots$')
arrow(ax,(52,36),(58,23.5),'fixe'); arrow(ax,(76,36),(70,23.5),'fixe')
save(fig,'26-054')
