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

fig,ax=canvas(68)
u=2.2; h=18*u; yb=22
ap=(44,yb+h); hw=18*math.tan(math.radians(44))*u
poly(ax,[ap,(44,yb),(44-hw,yb)],'fixe'); poly(ax,[ap,(44,yb),(44+hw,yb)],'sujet')
line(ax,[ap,(44,yb)],'fixe',dash=True); rmark(ax,(44,yb),(1,0),(0,1))
arc(ax,ap,-90,-46,9,'sujet'); arc(ax,ap,-134,-90,9,'fixe')
text(ax,*polar(ap,16,-68),'44°','sujet','s'); text(ax,*polar(ap,16,-112),'44°','fixe','s')
text(ax,53,36,'18 cm','sujet','s')
text(ax,*mid_off(ap,(44+hw,yb),3.5),r'$l$','sujet','m')
text(ax,44,15,r"$\cos44^\circ=\frac{18}{l}$",'encre','m')
text(ax,44,5,r"$l=\frac{18}{\cos44^\circ}\approx25{,}02$ cm",'resultat','m')
save(fig,'26-055')
