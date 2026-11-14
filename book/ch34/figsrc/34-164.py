import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
P=math.pi
def curve(ax,f,a,b,X,Y,role,dash=False,lw=1.3,n=240):
    ts=np.linspace(a,b,n); line(ax,[(X(t),Y(float(f(t)))) for t in ts],role,lw,dash)
def dot(ax,x,y,role,r=1.1): ax.add_patch(Circle((x,y),r,ec=COL[role],fc=COL[role],zorder=6))
def leg(ax,x,y,role,s,dash=False):
    line(ax,[(x,y),(x+6,y)],role,1.6,dash); text(ax,x+7.5,y,s,role,"s",ha="left")

fig,ax=canvas(64)
X=lambda t:12+t/(P/2)*58
Y=lambda v:16+v*34
line(ax,[(12,16),(78,16)],'fixe'); line(ax,[(12,16),(12,54)],'fixe')
curve(ax,lambda t:math.cos(t)**2,0,P/2,X,Y,'sujet',lw=2.0)
curve(ax,lambda t:(1+math.cos(2*t))/2,0,P/2,X,Y,'varie',dash=True,lw=1.2)
for t,v,a in [(0,'1','0°'),(P/4,'0,5','45°'),(P/2,'0','90°')]:
    val=float(v.replace(',','.')); dot(ax,X(t),Y(val),'resultat',1.5)
    text(ax,X(t),11.5,a,'fixe','s'); text(ax,X(t)+(3.5 if t else 3.5),Y(val)+3.5,v,'resultat','s')
leg(ax,30,60,'sujet',r'$\cos^2 x$'); leg(ax,52,60,'varie',r'$(1+\cos 2x)/2$',True)
save(fig,'34-164')
