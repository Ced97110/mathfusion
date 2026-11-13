import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
P=math.pi
def curve(ax,f,a,b,X,Y,role,dash=False,lw=1.3,n=240):
    ts=np.linspace(a,b,n); line(ax,[(X(t),Y(float(f(t)))) for t in ts],role,lw,dash)
def dot(ax,x,y,role,r=1.1): ax.add_patch(Circle((x,y),r,ec=COL[role],fc=COL[role],zorder=6))
def leg(ax,x,y,role,s,dash=False):
    line(ax,[(x,y),(x+6,y)],role,1.6,dash); text(ax,x+7.5,y,s,role,"s",ha="left")
fig,ax=canvas(76)
box(ax,2,64,40,8,'fixe',label='diapason : 440 /s',size='s'); box(ax,46,64,40,8,'autre',label='corde : 442 /s',size='s')
text(ax,44,58,'écart : 2 par seconde','resultat','s')
X=lambda t:8+t*68
Y=lambda v:32+v*14
line(ax,[(8,32),(80,32)],'fixe')
env=lambda t:math.sin(2*P*t)
curve(ax,lambda t:env(t)*math.sin(2*P*20*t),0,1,X,Y,'sujet',lw=0.9,n=1200)
curve(ax,env,0,1,X,Y,'varie',dash=True,lw=1.2); curve(ax,lambda t:-env(t),0,1,X,Y,'varie',dash=True,lw=1.2)
for t,s in [(0.25,'1'),(0.75,'2')]: text(ax,X(t),Y(1)+3.5,s,'varie','m',weight='bold')
text(ax,8,26.5,'0 s','fixe','s'); text(ax,76,26.5,'1 s','fixe','s')
leg(ax,6,10,'sujet','son entendu'); leg(ax,44,10,'varie','le volume enfle',True)
save(fig,'34-172')
