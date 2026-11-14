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

fig,ax=canvas(108)
ys=[94,69,44,19]
tit=['Dessiner en perspective','Repérer l’angle droit','Redessiner à plat','Compléter et calculer']
for i,y in enumerate(ys):
    disc(ax,7,y,3.4,'varie',label=str(i+1),size='s')
    if i<3: arrow(ax,(7,y-3.8),(7,ys[i+1]+3.8),'fixe')
    text(ax,48,y,tit[i],'encre','s',ha='left')
o=lambda y:(28,y-11);u=3.8
for i in (0,1):
    pave(ax,4,3,2,o(ys[i]),u)
v=V(o(ys[1]),u)
A,C,G=v(0,0,0),v(4,3,0),v(4,3,2)
poly(ax,[A,C,G],'sujet')
rt(ax,C,(0,1),unit(C,A),2.0,'resultat')
for i in (2,3):
    y=ys[i]
    poly(ax,[(14,y-5),(39,y-5),(39,y+5)],'sujet')
    rt(ax,(39,y-5),(-1,0),(0,1),2.2,'resultat')
text(ax,26.5,ys[3]-8.5,'5','sujet','s');text(ax,42,ys[3],'2','sujet','s')
text(ax,26.5,ys[3]-14.5,'2 ÷ 5 = 0,4','resultat','s')
save(fig,'27-071')
