import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
P=math.pi
def curve(ax,f,a,b,X,Y,role,dash=False,lw=1.3,n=240):
    ts=np.linspace(a,b,n); line(ax,[(X(t),Y(float(f(t)))) for t in ts],role,lw,dash)
def dot(ax,x,y,role,r=1.1): ax.add_patch(Circle((x,y),r,ec=COL[role],fc=COL[role],zorder=6))
def leg(ax,x,y,role,s,dash=False):
    line(ax,[(x,y),(x+6,y)],role,1.6,dash); text(ax,x+7.5,y,s,role,"s",ha="left")
fig,ax=canvas(58)
k=60/1.2247; x0=14
box(ax,x0,42,60,9,'sujet',label=r'$2\sin 45°\cos 30°$',size='s')
text(ax,8,46.5,'=','encre','l')
brace(ax,x0,x0+60,41,'sujet','1,2247')
box(ax,x0,22,0.9659*k,9,'varie',label=r'$\sin 75°$',size='s')
box(ax,x0+0.9659*k,22,0.2588*k,9,'autre',label=r'$\sin 15°$',size='s')
text(ax,8,26.5,'=','encre','l')
brace(ax,x0,x0+60,21,'resultat',r'1,2247 = 0,9659 + 0,2588')
save(fig,'34-171')
