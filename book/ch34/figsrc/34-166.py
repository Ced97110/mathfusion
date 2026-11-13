import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
P=math.pi
def curve(ax,f,a,b,X,Y,role,dash=False,lw=1.3,n=240):
    ts=np.linspace(a,b,n); line(ax,[(X(t),Y(float(f(t)))) for t in ts],role,lw,dash)
def dot(ax,x,y,role,r=1.1): ax.add_patch(Circle((x,y),r,ec=COL[role],fc=COL[role],zorder=6))
def leg(ax,x,y,role,s,dash=False):
    line(ax,[(x,y),(x+6,y)],role,1.6,dash); text(ax,x+7.5,y,s,role,"s",ha="left")

fig,ax=canvas(74)
X=lambda t:10+t/(2*P)*66
Y=lambda v:34+v*18
line(ax,[(10,34),(78,34)],'fixe'); line(ax,[(10,15),(10,53)],'fixe')
curve(ax,math.cos,0,2*P,X,Y,'autre'); curve(ax,lambda t:math.cos(t)**2,0,2*P,X,Y,'sujet',lw=2.0)
for t in (0,P): line(ax,[(X(t),Y(-1)),(X(t),Y(1))],'fixe',dash=True)
dot(ax,X(0),Y(1),'sujet',1.4); dot(ax,X(P),Y(1),'sujet',1.4); dot(ax,X(P),Y(-1),'autre',1.4)
text(ax,X(P)+2.5,Y(1)+3,'1','sujet','s',ha='left'); text(ax,X(P)+2.5,Y(-1)-2.5,'−1','autre','s',ha='left')
text(ax,X(0)+2.5,Y(1)+3,'1','sujet','s',ha='left')
text(ax,X(0),30.5,'0','fixe','s'); text(ax,X(P),30.5,r'$\pi$','fixe','s'); text(ax,X(2*P),30.5,r'$2\pi$','fixe','s')
leg(ax,10,69,'autre',r'$\cos x$'); leg(ax,40,69,'sujet',r'$\cos^2 x$')
save(fig,'34-166')
