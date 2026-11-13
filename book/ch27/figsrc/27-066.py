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

fig,ax=canvas(64)
o=(30,8);u=8;v=V(o,u)
pave(ax,4,3,2,o,u)
A=v(0,0,0);C=v(4,3,0);G=v(4,3,2)
line(ax,[A,C],'fixe',lw=1.1,dash=True);line(ax,[A,G],'sujet',lw=1.4)
text(ax,A[0],A[1]-3,'A','encre','s');text(ax,C[0]+2.8,C[1]-2,'C','encre','s');text(ax,G[0],G[1]+3,'G','encre','s')
mg=((A[0]+G[0])/2,(A[1]+G[1])/2);mc=((A[0]+C[0])/2,(A[1]+C[1])/2)
line(ax,[mg,(60,38)],'sujet',lw=0.7);line(ax,[mc,(60,16)],'fixe',lw=0.7)
text(ax,61,41,'grande diagonale','sujet','s',ha='left');text(ax,61,36,'AG ≈ 5,39 m','sujet','s',ha='left')
text(ax,61,19,'diagonale du sol','fixe','s',ha='left');text(ax,61,14,'AC = 5 m','fixe','s',ha='left')
save(fig,'27-066')
