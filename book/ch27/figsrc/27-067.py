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

fig,ax=canvas(70)
text(ax,44,63,r'$d^2 = L^2 + l^2 + h^2$','sujet','l')
rows=[('4 · 3 · 2',r'$16 + 9 + 4 = 29$',r'$d \approx 5{,}39$'),('2 · 3 · 6',r'$4 + 9 + 36 = 49$',r'$d = 7$'),('1 · 2 · 2',r'$1 + 4 + 4 = 9$',r'$d = 3$')]
for i,(a,b,c) in enumerate(rows):
    y=44-i*15
    box(ax,4,y-5,22,10,'varie',label=a)
    arrow(ax,(27,y),(32,y),'fixe')
    box(ax,33,y-5,32,10,'resultat',label=b)
    text(ax,76,y,c,'sujet','m')
text(ax,44,5,'même forme à chaque ligne','fixe','s')
save(fig,'27-067')
