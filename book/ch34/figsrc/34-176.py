import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
P=math.pi
def curve(ax,f,a,b,X,Y,role,dash=False,lw=1.3,n=240):
    ts=np.linspace(a,b,n); line(ax,[(X(t),Y(float(f(t)))) for t in ts],role,lw,dash)
def dot(ax,x,y,role,r=1.1): ax.add_patch(Circle((x,y),r,ec=COL[role],fc=COL[role],zorder=6))
def leg(ax,x,y,role,s,dash=False):
    line(ax,[(x,y),(x+6,y)],role,1.6,dash); text(ax,x+7.5,y,s,role,"s",ha="left")
fig,ax=canvas(72)
O=(44,22); u=22
line(ax,[(8,22),(80,22)],'fixe'); line(ax,[(44,20),(44,48)],'fixe')
arc=lambda a0,a1,r:[(O[0]+r*math.cos(math.radians(a)),O[1]+r*math.sin(math.radians(a))) for a in np.linspace(a0,a1,60)]
for a0,a1 in [(0,87),(90,177)]:
    pts=arc(a0,a1,u+0.01); line(ax,pts[:-1],'varie',lw=1.3); arrow(ax,pts[-2],pts[-1],'varie',lw=1.3)
dot(ax,66,22,'sujet',1.5); dot(ax,44,44,'varie',1.5); dot(ax,22,22,'resultat',1.5)
text(ax,66,17.5,'1','sujet','m'); text(ax,48.5,46,r'$i$','varie','m'); text(ax,22,17.5,'−1','resultat','m')
text(ax,66,38,'fois $i$','varie','s'); text(ax,22,38,'fois $i$','varie','s')
text(ax,44,10,r'$i\times i=-1$','resultat','l')
text(ax,44,66,r'$i\sin\theta\times i\sin\varphi$','encre','s'); text(ax,44,60,r'$=-\sin\theta\sin\varphi$','resultat','s')
save(fig,'34-176')
