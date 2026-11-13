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

fig,ax=canvas(42)
A=(6,16);t=math.radians(21.8)
line(ax,[A,(32,16)],'fixe',lw=1.2);line(ax,[A,(6+26*math.cos(t),16+26*math.sin(t))],'sujet',lw=1.4)
arc(ax,A,12,0,21.8);text(ax,22,18.4,'α','varie','s')
text(ax,18,8,'α ≈ 21,80°','sujet','s')
poly(ax,[(54,16),(79,16),(79,26)],'autre');rt(ax,(79,16),(-1,0),(0,1),2.2,'fixe')
text(ax,66.5,12,'5','autre','s');text(ax,82,21,'2','autre','s');text(ax,67,6,'rapport 0,4','autre','s')
arrow(ax,(52,32),(34,32),'resultat');text(ax,43,36.5,'arctan','resultat','s');text(ax,43,27.5,'chapitre 33','resultat','s')
arrow(ax,(36,16),(50,16),'fixe');text(ax,43,11.5,'tan','fixe','s')
save(fig,'27-076')
