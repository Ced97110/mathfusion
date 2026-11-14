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

fig,ax=canvas(76)
box(ax,4,59,20,10,'fixe',label=r'$\sqrt{50}$');arrow(ax,(25,64),(31,64),'fixe');box(ax,32,59,22,10,'resultat',label='50')
text(ax,72,64,'valeur exacte','resultat','s')
box(ax,4,41,20,10,'varie',label=r'$7{,}07$');arrow(ax,(25,46),(31,46),'fixe');box(ax,32,41,26,10,'limite',label=r'$\approx 49{,}98$')
text(ax,74,46,'arrondi d’abord','varie','s')
f=numberline(ax,8,76,16,49.96,50.0,0.01,arrow_right=False,every=2)
disc(ax,f(49.98),16,1.4,'limite');disc(ax,f(50),16,1.4,'resultat')
brace(ax,f(49.98),f(50),22,'limite','écart 0,02',down=False)
arrow(ax,(45,40.5),(f(49.98),19),'limite')
save(fig,'27-073')
