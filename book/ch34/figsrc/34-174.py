import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
P=math.pi
def curve(ax,f,a,b,X,Y,role,dash=False,lw=1.3,n=240):
    ts=np.linspace(a,b,n); line(ax,[(X(t),Y(float(f(t)))) for t in ts],role,lw,dash)
def dot(ax,x,y,role,r=1.1): ax.add_patch(Circle((x,y),r,ec=COL[role],fc=COL[role],zorder=6))
def leg(ax,x,y,role,s,dash=False):
    line(ax,[(x,y),(x+6,y)],role,1.6,dash); text(ax,x+7.5,y,s,role,"s",ha="left")
fig,ax=canvas(68)
s=12; O=(8,8); d=lambda a,r:(O[0]+r*math.cos(math.radians(a)),O[1]+r*math.sin(math.radians(a)))
P1=d(20,3*s); P2=d(80,4*s); F=d(20,4*math.cos(math.radians(60))*s)
line(ax,[O,(O[0]+52,O[1])],'fixe',lw=0.7)
poly(ax,[O,P1,P2],'sujet')
line(ax,[P2,F],'varie',lw=1.3,dash=True)
ux=(math.cos(math.radians(20)),math.sin(math.radians(20))); vx=(-ux[1],ux[0]); q=2.0
line(ax,[(F[0]+q*ux[0],F[1]+q*ux[1]),(F[0]+q*ux[0]+q*vx[0],F[1]+q*ux[1]+q*vx[1]),(F[0]+q*vx[0],F[1]+q*vx[1])],'varie',lw=0.8)
line(ax,[(O[0]+10*math.cos(math.radians(a)),O[1]+10*math.sin(math.radians(a))) for a in np.linspace(20,80,30)],'encre',lw=1.0)
text(ax,d(50,16)[0],d(50,16)[1],'60°','encre','s')
text(ax,(O[0]+P1[0])/2+1,O[1]+(P1[1]-O[1])/2-4,'3','sujet','m')
text(ax,(O[0]+P2[0])/2-4,(O[1]+P2[1])/2,'4','sujet','m')
text(ax,19.5,36,'h','varie','m')
text(ax,66,32,r'$h=4\sin 60°\approx3{,}464$','varie','s')
text(ax,66,22,r'aire $\approx 5{,}196$','resultat','m')
save(fig,'34-174')
