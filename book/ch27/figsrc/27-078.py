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

fig,ax=canvas(52)
o=(18,10);u=5;v=V(o,u)
pave(ax,4,3,2,o,u)
line(ax,[v(0,0,0),v(4,3,2)],'sujet',lw=1.3)
o2=(62,10);v2=V(o2,u)
pave(ax,4,3,0,o2,u)
line(ax,[v2(0,0,0),v2(4,3,0)],'sujet',lw=1.3)
arrow(ax,(38,24),(46,24),'varie');text(ax,42,30,'h → 0','varie','s')
text(ax,20,46,'h = 2','fixe','m');text(ax,64,46,'h = 0','fixe','m')
text(ax,20,4,r'$d=\sqrt{16+9+4}$','sujet','s');text(ax,64,4,r'$d=\sqrt{16+9+0}=5$','resultat','s')
save(fig,'27-078')
