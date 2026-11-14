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

fig,ax=canvas(60)
line(ax,[(6,10),(40,10)],'fixe',lw=1.4);line(ax,[(23,10),(23,50)],'sujet',lw=2.4)
rt(ax,(23,10),(0,1),(1,0),3.5)
text(ax,23,56,'sans sol : L = l = 0','fixe','s');text(ax,26,32,'poteau : h = 2','sujet','s',ha='left');text(ax,12,6,'sol','fixe','s')
box(ax,48,34,36,16,'limite',label=r'$\tan\alpha = 2/0$'+'\npas de sens')
box(ax,48,10,36,16,'resultat',label=r'$\sin\alpha = 2/2 = 1$'+'\nα = 90°')
save(fig,'27-080')
