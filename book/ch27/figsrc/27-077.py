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

fig,ax=canvas(58)
o=(20,13);u=5.2;v=V(o,u)
pave(ax,4,3,2,o,u)
A,C,G=v(0,0,0),v(4,3,0),v(4,3,2)
poly(ax,[A,C,G],'sujet')
text(ax,22,52,'le dessin repère','fixe','s');text(ax,22,5,'angle dessiné ≠ 21,80°','limite','s')
arrow(ax,(42,26),(48,26),'varie')
poly(ax,[(52,20),(77,20),(77,30)],'sujet');rt(ax,(77,20),(-1,0),(0,1),2.2,'fixe')
text(ax,64.5,16.5,'5','sujet','s');text(ax,80.5,25,'2','sujet','s')
text(ax,66,52,'le calcul mesure','resultat','s');text(ax,66,38,'α ≈ 21,80°','resultat','s');text(ax,66,9,'longueurs + angles droits','encre','s')
save(fig,'27-077')
