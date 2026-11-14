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

fig,ax=canvas(76)
by=20
P1=(6,by); C1=(22,by); Q1=(22,by+16)
P2=(30,by); C2=(78,by); Q2=(78,by+48)
poly(ax,[P1,C1,Q1],'sujet'); poly(ax,[P2,C2,Q2],'autre')
rmark(ax,C1,(-1,0),(0,1)); rmark(ax,C2,(-1,0),(0,1),s=3)
arc(ax,P1,0,45,6,'varie'); arc(ax,P2,0,45,9,'varie')
text(ax,*polar(P1,12,22.5),'45°','varie','s'); text(ax,*polar(P2,17,22.5),'45°','varie','s')
text(ax,*mid_off(P1,C1,-3),'1','sujet'); text(ax,*mid_off(C1,Q1,-3),'1','sujet'); text(ax,*mid_off(P1,Q1,3.8),'1,4142','sujet','s')
text(ax,*mid_off(P2,C2,-3),'3','autre'); text(ax,*mid_off(C2,Q2,-3.2),'3','autre'); text(ax,*mid_off(P2,Q2,4.5),'4,2426','autre','s')
text(ax,22,7,r'$1\div1{,}4142\approx0{,}7071$','sujet','s'); text(ax,60,7,r'$3\div4{,}2426\approx0{,}7071$','autre','s')
text(ax,44,72,'même rapport, deux tailles','encre','m')
save(fig,'26-060')
