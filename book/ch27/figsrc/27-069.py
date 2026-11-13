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

fig,ax=canvas(80)
u=5.5
text(ax,22,72,'étage 1 : le sol','fixe','s');text(ax,62,72,'étage 2 : triangle ACG','sujet','s')
poly(ax,[(6,40),(28,40),(28,56.5),(6,56.5)],'fixe')
line(ax,[(6,40),(28,56.5)],'sujet',lw=1.3)
text(ax,17,36.5,'4','fixe','s');text(ax,31,48,'3','fixe','s');text(ax,12.5,51,'AC','sujet','s')
poly(ax,[(48,40),(75.5,40),(75.5,51)],'sujet')
rt(ax,(75.5,40),(-1,0),(0,1),2.2,'fixe')
text(ax,62,36.5,'5','sujet','s');text(ax,79,45.5,'2','sujet','s');text(ax,58,49,'AG','sujet','s')
text(ax,24,26,r'$AC^2 = 16 + 9 = 25$','fixe','s');text(ax,62,26,r'$AG^2 = 25 + 4 = 29$','resultat','s')
arrow(ax,(40,26),(46.5,26),'varie')
text(ax,44,14,'25 est remplacé par 16 + 9','varie','s')
save(fig,'27-069')
