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

fig,ax=canvas(92)
k=2.2; x0=10; By=48
P0=(x0,By); T=(x0,By+18*k); P2=(x0+18*math.tan(math.radians(44))*k,By)
poly(ax,[P0,T,P2],'fixe',lw=0.1)
line(ax,[P0,T],'fixe',lw=1.8); line(ax,[P0,P2],'fixe',lw=0.9); line(ax,[T,P2],'resultat',lw=1.8)
rmark(ax,P0,(1,0),(0,1),s=2.6,role='encre')
arc(ax,T,-90,-46,8,'encre',lw=0.9)
text(ax,x0-1.5,By+9*k,'18 cm','fixe','s',ha='right')
p=mid_off(T,P2,3.2); text(ax,p[0]+1.5,p[1]+1.5,r'$l$','resultat','m')
text(ax,x0+6.5,T[1]-12,'44°','encre','s')
rows=[('18 cm',18,'fixe',''),(r'$l$ = 25,0 cm',25.0,'resultat',''),('échoue',12.9,'limite','')]
for i,(lab,v,role,_) in enumerate(rows):
    y=29-i*10
    box(ax,x0,y,k*v,6,role,r=0.6,label=lab,size='s')
text(ax,x0,17.3,r'$18\times\cos44^\circ=12{,}9$ cm','limite','s',ha='left')
line(ax,[(x0+18*k,3),(x0+18*k,35.5)],'fixe',dash=True)
text(ax,44,40.5,r'$l$ doit dépasser 18 cm','encre','m')
save(fig,'26-056')
