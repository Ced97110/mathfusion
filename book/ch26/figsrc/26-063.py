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

fig,ax=canvas(40)
L=38.0; sn=math.sin
AB=L*sn(math.radians(20))/sn(math.radians(130))
def tri(ox,oy):
    return (ox,oy),(ox+L,oy),(ox+AB*math.cos(math.radians(30)),oy+AB*sn(math.radians(30)))
b,c,a=tri(5,16)
H=(a[0],16)
poly(ax,[b,H,a],'sujet'); poly(ax,[H,c,a],'autre')
line(ax,[a,H],'resultat',lw=1.4); rmark(ax,H,(-1,0),(0,1)); rmark(ax,H,(1,0),(0,1))
text(ax,a[0]-6,a[1]+3.5,'130°','encre','s'); text(ax,b[0]+2,12.5,'30°','encre','s'); text(ax,c[0]-2,12.5,'20°','encre','s')
text(ax,24,5,'depuis 130° : tombe dedans','resultat','s')
b2,c2,a2=tri(48,16)
t=L*math.cos(math.radians(30)); F=(b2[0]+t*math.cos(math.radians(30)),b2[1]+t*sn(math.radians(30)))
poly(ax,[b2,c2,a2],'fixe')
line(ax,[a2,F],'fixe',dash=True); line(ax,[c2,F],'limite',lw=1.4)
ux,uy=-math.cos(math.radians(30)),-sn(math.radians(30)); vx,vy=c2[0]-F[0],c2[1]-F[1]; n=math.hypot(vx,vy)
rmark(ax,F,(ux,uy),(vx/n,vy/n))
text(ax,a2[0]-6,a2[1]+3.5,'130°','encre','s'); text(ax,b2[0]+2,12.5,'30°','encre','s'); text(ax,c2[0]-2,12.5,'20°','encre','s')
text(ax,67,5,'depuis 20° : tombe dehors','limite','s')
save(fig,'26-063')
