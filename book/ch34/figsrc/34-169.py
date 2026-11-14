import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
P=math.pi
def curve(ax,f,a,b,X,Y,role,dash=False,lw=1.3,n=240):
    ts=np.linspace(a,b,n); line(ax,[(X(t),Y(float(f(t)))) for t in ts],role,lw,dash)
def dot(ax,x,y,role,r=1.1): ax.add_patch(Circle((x,y),r,ec=COL[role],fc=COL[role],zorder=6))
def leg(ax,x,y,role,s,dash=False):
    line(ax,[(x,y),(x+6,y)],role,1.6,dash); text(ax,x+7.5,y,s,role,"s",ha="left")
fig,ax=canvas(82)
box(ax,2,66,36,9,'sujet',label=r'$\cos 2\theta=\sin\theta$',size='s')
box(ax,50,66,36,9,'varie',label=r'$2s^2+s-1=0$',size='s')
arrow(ax,(38.5,70.5),(49.5,70.5),'encre')
text(ax,44,61,r'$\cos 2\theta=1-2\sin^2\theta$','encre','s')
text(ax,66,56.5,r'avec $s=\sin\theta$','varie','s')
cx,cy,R=28,26,18
line(ax,[(cx+R*math.cos(a),cy+R*math.sin(a)) for a in np.linspace(0,2*P,200)],'fixe')
line(ax,[(8,cy+R/2),(80,cy+R/2)],'varie',dash=True); line(ax,[(8,cy-R),(80,cy-R)],'varie',dash=True)
text(ax,66,cy+R/2+2.5,r'$s=1/2$','varie','s'); text(ax,66,cy-R+2.5,r'$s=-1$','varie','s')
for a,t,dx,dy in [(30,'30°',6,-3),(150,'150°',-6,-3),(270,'270°',0,-3.8)]:
    x=cx+R*math.cos(math.radians(a)); y=cy+R*math.sin(math.radians(a)); dot(ax,x,y,'resultat',1.5)
    text(ax,x+dx,y+dy,t,'resultat','s')
save(fig,'34-169')
