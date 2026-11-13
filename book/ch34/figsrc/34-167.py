import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
P=math.pi
def curve(ax,f,a,b,X,Y,role,dash=False,lw=1.3,n=240):
    ts=np.linspace(a,b,n); line(ax,[(X(t),Y(float(f(t)))) for t in ts],role,lw,dash)
def dot(ax,x,y,role,r=1.1): ax.add_patch(Circle((x,y),r,ec=COL[role],fc=COL[role],zorder=6))
def leg(ax,x,y,role,s,dash=False):
    line(ax,[(x,y),(x+6,y)],role,1.6,dash); text(ax,x+7.5,y,s,role,"s",ha="left")

fig,ax=canvas(66)
X=lambda d:12+d/180*62
Y=lambda v:16+v*30
line(ax,[(12,16),(78,16)],'fixe'); line(ax,[(12,16),(12,50)],'fixe')
line(ax,[(12,Y(.5)),(76,Y(.5))],'resultat',dash=True,lw=1.3)
curve(ax,lambda d:math.cos(math.radians(d))**2,0,180,X,Y,'sujet',lw=1.6)
for d,v in [(0,'1'),(45,'0,5'),(90,'0'),(135,'0,5')]:
    val=float(v.replace(',','.')); line(ax,[(X(d),16),(X(d),Y(val))],'sujet',lw=0.9); dot(ax,X(d),Y(val),'sujet',1.4)
    text(ax,X(d),11.5,f'{d}°','fixe','s'); text(ax,X(d)+3.5,Y(val)+3.2,v,'sujet','s')
text(ax,46,Y(.5)+4.5,'moyenne 0,5','resultat','s')
text(ax,44,60,r'$(1+0{,}5+0+0{,}5)/4=0{,}5$','encre','s')
save(fig,'34-167')
