import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
P=math.pi
def curve(ax,f,a,b,X,Y,role,dash=False,lw=1.3,n=240):
    ts=np.linspace(a,b,n); line(ax,[(X(t),Y(float(f(t)))) for t in ts],role,lw,dash)
def dot(ax,x,y,role,r=1.1): ax.add_patch(Circle((x,y),r,ec=COL[role],fc=COL[role],zorder=6))
def leg(ax,x,y,role,s,dash=False):
    line(ax,[(x,y),(x+6,y)],role,1.6,dash); text(ax,x+7.5,y,s,role,"s",ha="left")

fig,ax=canvas(70)
X=lambda t:10+t/(2*P)*66
Y=lambda v:30+v*18
line(ax,[(10,30),(78,30)],'fixe'); line(ax,[(10,10),(10,52)],'fixe')
line(ax,[(10,Y(1)),(76,Y(1))],'fixe',dash=True); line(ax,[(10,Y(.5)),(76,Y(.5))],'resultat',dash=True,lw=1.3)
curve(ax,math.cos,0,2*P,X,Y,'autre'); curve(ax,lambda t:math.cos(t)**2,0,2*P,X,Y,'sujet',lw=2.0)
text(ax,5,Y(1),'1','fixe','s'); text(ax,4,Y(.5),'0,5','resultat','s'); text(ax,5,Y(-1),'−1','fixe','s')
text(ax,X(2*P),26.5,r'$2\pi$','fixe','s')
text(ax,44,Y(.5)+12.5,'puissance maximale : 1','fixe','s') if False else None
leg(ax,10,58,'resultat','puissance moyenne : 0,5',True); leg(ax,10,64,'autre','courant'); leg(ax,36,64,'sujet','puissance (carré)')
save(fig,'34-168')
