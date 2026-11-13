import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
import math
def arc(ax,p,a0,a1,r,role='sujet',lw=0.9):
    ax.add_patch(Arc(p,2*r,2*r,theta1=a0,theta2=a1,color=COL[role],lw=lw,zorder=3))
def rmark(ax,p,d1,d2,s=2.2,role='fixe'):
    line(ax,[(p[0]+d1[0]*s,p[1]+d1[1]*s),(p[0]+(d1[0]+d2[0])*s,p[1]+(d1[1]+d2[1])*s),(p[0]+d2[0]*s,p[1]+d2[1]*s)],role,lw=0.7)
def polar(p,r,a): return (p[0]+r*math.cos(math.radians(a)),p[1]+r*math.sin(math.radians(a)))
def mid_off(p,q,off):
    dx,dy=q[0]-p[0],q[1]-p[1]; n=math.hypot(dx,dy)
    return ((p[0]+q[0])/2-dy/n*off,(p[1]+q[1])/2+dx/n*off)

fig,ax=canvas(52)
u=20.0; y0=12
a=(6,y0); b=(26,y0); c=(26,y0+u); d=(6,y0+u)
poly(ax,[d,a,c],'fixe'); poly(ax,[a,b,c],'sujet')
line(ax,[a,c],'varie',lw=1.3,dash=True); rmark(ax,b,(-1,0),(0,1))
text(ax,16,8.5,'1'); text(ax,*mid_off(b,c,-3.2),'1'); text(ax,*mid_off(a,c,-3.5),r'$\sqrt{2}$')
B1=(40,y0); C1=(80,y0); A1=(60,y0+math.sqrt(3)*u); H=(60,y0)
poly(ax,[B1,H,A1],'fixe'); poly(ax,[H,C1,A1],'sujet')
line(ax,[A1,H],'varie',lw=1.3,dash=True); rmark(ax,H,(1,0),(0,1))
text(ax,50,8.5,'1'); text(ax,70,8.5,'1'); text(ax,56.3,29,r'$\sqrt{3}$')
text(ax,*mid_off(C1,A1,-3.5),'2'); text(ax,*mid_off(B1,A1,3.5),'2')
text(ax,16,3,'carré coupé','encre','s'); text(ax,60,3,'triangle équilatéral coupé','encre','s')
save(fig,'26-057')
