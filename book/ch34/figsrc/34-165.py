import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
P=math.pi
def curve(ax,f,a,b,X,Y,role,dash=False,lw=1.3,n=240):
    ts=np.linspace(a,b,n); line(ax,[(X(t),Y(float(f(t)))) for t in ts],role,lw,dash)
def dot(ax,x,y,role,r=1.1): ax.add_patch(Circle((x,y),r,ec=COL[role],fc=COL[role],zorder=6))
def leg(ax,x,y,role,s,dash=False):
    line(ax,[(x,y),(x+6,y)],role,1.6,dash); text(ax,x+7.5,y,s,role,"s",ha="left")

fig,ax=canvas(66)
X=lambda t:10+t/(2*P)*66
Y=lambda v:26+v*24
line(ax,[(10,26),(78,26)],'fixe'); line(ax,[(10,26),(10,52)],'fixe')
line(ax,[(10,Y(.5)),(76,Y(.5))],'resultat',dash=True,lw=1.2)
curve(ax,lambda t:math.cos(t)**2,0,2*P,X,Y,'sujet',lw=2.0)
text(ax,6,Y(1),'1','fixe','s'); text(ax,5,Y(.5),'1/2','resultat','s')
text(ax,X(P),22.5,r'$\pi$','fixe','s'); text(ax,X(2*P),22.5,r'$2\pi$','fixe','s')
brace(ax,X(0),X(P),19,'varie',r'période $\pi$'); brace(ax,X(P),X(2*P),19,'varie',r'période $\pi$')
text(ax,44,60,'moyenne : 1/2','resultat','s'); arrow(ax,(44,57),(44,Y(.5)+1.2),'resultat')
save(fig,'34-165')
