import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
P=math.pi
def curve(ax,f,a,b,X,Y,role,dash=False,lw=1.3,n=240):
    ts=np.linspace(a,b,n); line(ax,[(X(t),Y(float(f(t)))) for t in ts],role,lw,dash)
def dot(ax,x,y,role,r=1.1): ax.add_patch(Circle((x,y),r,ec=COL[role],fc=COL[role],zorder=6))
def leg(ax,x,y,role,s,dash=False):
    line(ax,[(x,y),(x+6,y)],role,1.6,dash); text(ax,x+7.5,y,s,role,"s",ha="left")
fig,ax=canvas(84)
X=lambda t:10+t/(2*P)*66
Y=lambda v:36+v*5.2
line(ax,[(10,36),(78,36)],'fixe'); line(ax,[(10,Y(-5)),(10,Y(5))],'fixe')
curve(ax,lambda t:3*math.sin(t),0,2*P,X,Y,'autre'); curve(ax,lambda t:4*math.cos(t),0,2*P,X,Y,'fixe')
curve(ax,lambda t:3*math.sin(t)+4*math.cos(t),0,2*P,X,Y,'sujet',lw=2.2)
dot(ax,X(0),Y(4),'sujet',1.4); text(ax,6.5,Y(4),'4','sujet','s')
text(ax,6,Y(5)+0.5,'5','sujet','s') ; text(ax,5.5,Y(-5),'−5','sujet','s')
leg(ax,2,80,'autre',r'$3\sin x$'); leg(ax,30,80,'fixe',r'$4\cos x$'); leg(ax,56,80,'sujet',r'$5\sin(x+\alpha)$')
text(ax,44,72,r'somme des deux : hauteur 5','sujet','s')
save(fig,'34-170')
