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

fig,ax=canvas(80)
Bv=(14,26); Cv=(78,26)
AB=64*math.sin(math.radians(60))/math.sin(math.radians(70))
A=(Bv[0]+AB*math.cos(math.radians(50)),Bv[1]+AB*math.sin(math.radians(50))); H=(A[0],26)
poly(ax,[Bv,H,A],'sujet'); poly(ax,[H,Cv,A],'autre')
line(ax,[A,H],'varie',lw=1.2); rmark(ax,H,(-1,0),(0,1)); rmark(ax,H,(1,0),(0,1))
aB=math.degrees(math.atan2(Bv[1]-A[1],Bv[0]-A[0])); aC=math.degrees(math.atan2(Cv[1]-A[1],Cv[0]-A[0]))
arc(ax,Bv,0,50,8,'sujet',lw=1.5); text(ax,*polar(Bv,15,25),'50°','sujet','s')
arc(ax,Cv,120,180,8,'autre',lw=1.5); text(ax,*polar(Cv,15,150),'60°','autre','s')
arc(ax,A,aB,-90,7,'sujet',lw=1.5); text(ax,*polar(A,12.5,(aB-90)/2),'40°','sujet','s',weight='bold')
arc(ax,A,-90,aC,7,'autre',lw=1.5); text(ax,*polar(A,12.5,(aC-90)/2),'30°','autre','s',weight='bold'); arc(ax,A,aB,aC,20,'resultat',lw=1.6)
text(ax,A[0],A[1]+4,'70° = 40° + 30°','resultat','s',weight='bold')
text(ax,(Bv[0]+H[0])/2,18,'50° + 40° = 90°','sujet','s'); text(ax,(H[0]+Cv[0])/2,18,'60° + 30° = 90°','autre','s')
box(ax,12,2,64,10,'resultat',label='50° + 60° + 70° = 180°',size='m',weight='bold')
save(fig,'26-062')
