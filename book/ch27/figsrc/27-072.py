import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def V(o,u):
    return lambda x,y,z: iso(x,y,z,o,u)
def pave(ax,L,l,h,o,u,role='fixe'):
    v=V(o,u)
    if h>0:
        poly(ax,[v(0,0,h),v(L,0,h),v(L,l,h),v(0,l,h)],role)
        poly(ax,[v(0,0,0),v(L,0,0),v(L,0,h),v(0,0,h)],role)
        poly(ax,[v(0,0,0),v(0,l,0),v(0,l,h),v(0,0,h)],role)
        for a,b in [((L,0,0),(L,l,0)),((0,l,0),(L,l,0)),((L,l,0),(L,l,h))]:
            line(ax,[v(*a),v(*b)],role,lw=0.6,dash=True)
    else:
        poly(ax,[v(0,0,0),v(L,0,0),v(L,l,0),v(0,l,0)],role)
def rt(ax,p,d1,d2,s=2.4,role='resultat'):
    line(ax,[(p[0]+s*d1[0],p[1]+s*d1[1]),(p[0]+s*(d1[0]+d2[0]),p[1]+s*(d1[1]+d2[1])),(p[0]+s*d2[0],p[1]+s*d2[1])],role,lw=0.7)
def arc(ax,c,r,a0,a1,role='varie',n=24):
    pts=[(c[0]+r*math.cos(math.radians(a0+(a1-a0)*i/n)),c[1]+r*math.sin(math.radians(a0+(a1-a0)*i/n))) for i in range(n+1)]
    line(ax,pts,role,lw=1.0)
def unit(a,b):
    d=math.hypot(b[0]-a[0],b[1]-a[1]); return ((b[0]-a[0])/d,(b[1]-a[1])/d)

fig,ax=canvas(66)
line(ax,[(44,4),(44,62)],'fixe',lw=0.5,dash=True)
text(ax,23,60,'1. verticale + horizontale','fixe','s');text(ax,65,60,'2. face rectangulaire','fixe','s')
line(ax,[(6,18),(38,18)],'fixe',lw=1.4);line(ax,[(26,18),(26,50)],'sujet',lw=1.4)
rt(ax,(26,18),(0,1),(-1,0),3.5)
text(ax,24,36,'verticale','sujet','s',ha='right');text(ax,14,14,'horizontale','fixe','s');text(ax,23,6,'elles se touchent','encre','s')
poly(ax,[(52,20),(78,20),(78,46),(52,46)],'sujet')
for (x,y),(a,b) in [((52,20),((1,0),(0,1))),((78,20),((-1,0),(0,1))),((78,46),((-1,0),(0,-1))),((52,46),((1,0),(0,-1)))]:
    rt(ax,(x,y),a,b,3.0)
text(ax,65,33,'angle droit','resultat','s');text(ax,65,16,'arête','sujet','s');text(ax,80,33,'arête','sujet','s',ha='left')
save(fig,'27-072')
