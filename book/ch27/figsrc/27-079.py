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
A=(40,10)
line(ax,[A,(82,10)],'fixe',lw=1.2);text(ax,64,5,'sol : diagonale 5','fixe','s')
line(ax,[A,(40,66)],'fixe',lw=0.7,dash=True);text(ax,40,68.5,'90°','fixe','s')
for ang,r,lab,pos in [(21.8,42,'h = 2 : 21,80°','r'),(84.29,46,'h = 50 : 84,29°','R'),(89.43,54,'h = 500 : 89,43°','L')]:
    t=math.radians(ang);p=(A[0]+r*math.cos(t),A[1]+r*math.sin(t))
    line(ax,[A,p],'varie',lw=1.4)
    if pos=='r': text(ax,66,32,lab,'varie','s')
    elif pos=='R': text(ax,p[0]+3,p[1],lab,'varie','s',ha='left')
    else: text(ax,p[0]-3,p[1],lab,'varie','s',ha='right')
save(fig,'27-079')
