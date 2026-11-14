import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
P=math.pi
def curve(ax,f,a,b,X,Y,role,dash=False,lw=1.3,n=240):
    ts=np.linspace(a,b,n); line(ax,[(X(t),Y(float(f(t)))) for t in ts],role,lw,dash)
def dot(ax,x,y,role,r=1.1): ax.add_patch(Circle((x,y),r,ec=COL[role],fc=COL[role],zorder=6))
def leg(ax,x,y,role,s,dash=False):
    line(ax,[(x,y),(x+6,y)],role,1.6,dash); text(ax,x+7.5,y,s,role,"s",ha="left")
fig,ax=canvas(70)
s=3.6; g=math.acos(198/390); A=(8,16); B=(A[0]+15*s,A[1]); C=(A[0]+13*s*math.cos(g),A[1]+13*s*math.sin(g))
poly(ax,[A,B,C],'fixe')
line(ax,[B,C],'sujet',lw=2.0)
text(ax,(A[0]+B[0])/2,11,'15','fixe','m')
text(ax,(A[0]+C[0])/2-4,(A[1]+C[1])/2+1,'13','fixe','m')
text(ax,(B[0]+C[0])/2+4.5,(B[1]+C[1])/2+1,'14','sujet','m')
r=9; line(ax,[(A[0]+r*math.cos(a),A[1]+r*math.sin(a)) for a in np.linspace(0,g,30)],'varie',lw=1.2)
text(ax,A[0]+14,A[1]+3.2,r'$A+B$','varie','s')
text(ax,44,64,r'$14^2=13^2+15^2-2\cdot13\cdot15\cos$','encre','s')
text(ax,70,36,r'$\cos=0{,}5077$','resultat','s')
save(fig,'34-173')
