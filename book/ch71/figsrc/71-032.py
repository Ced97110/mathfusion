import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def clipline(a,b,c,win):
    xa,xb,ya,yb=win; pts=[]
    for x in (xa,xb):
        if b!=0:
            y=(c-a*x)/b
            if ya-1e-9<=y<=yb+1e-9: pts.append((x,y))
    for y in (ya,yb):
        if a!=0:
            x=(c-b*y)/a
            if xa-1e-9<=x<=xb+1e-9: pts.append((x,y))
    pts=sorted(set((round(p[0],9),round(p[1],9)) for p in pts))
    return [pts[0],pts[-1]] if len(pts)>=2 else None
class Pl:
    def __init__(s,ox,oy,k): s.ox,s.oy,s.k=ox,oy,k
    def __call__(s,x,y): return (s.ox+x*s.k, s.oy+y*s.k)
def lvl(ax,pl,a,b,c,win,role='sujet',lw=1.2,dash=False):
    seg=clipline(a,b,c,win)
    if seg: line(ax,[pl(*p) for p in seg],role,lw,dash)
    return seg
def axes(ax,pl,win):
    xa,xb,ya,yb=win
    line(ax,[pl(xa,0),pl(xb,0)],'fixe',0.5); line(ax,[pl(0,ya),pl(0,yb)],'fixe',0.5)
def frame(ax,pl,win):
    xa,xb,ya,yb=win
    line(ax,[pl(xa,ya),pl(xb,ya),pl(xb,yb),pl(xa,yb),pl(xa,ya)],'fixe',0.4)

u=6.4; x0=5.5; fig,ax=canvas(76)
text(ax,44,70,r'prix : $f(x+y)=f(x)+f(y)$','resultat','m')
box(ax,x0,52,4*u,9,'sujet',label=r'$f(x)=4$',size='s')
box(ax,x0+4*u,52,7*u,9,'autre',label=r'$f(y)=7$',size='s')
box(ax,x0,40,11*u,9,'resultat',label=r'$f(x+y)=11$',size='s')
text(ax,44,32,r'carré : $1+1\neq4$','limite','m')
box(ax,x0,18,u,9,'sujet',label='1',size='s'); box(ax,x0+u,18,u,9,'sujet',label='1',size='s')
box(ax,x0,6,4*u,9,'limite',label=r'$f(x+y)=4$',size='s')
text(ax,x0+2*u+3,22.5,r'$x$ et $y$ : même flèche','sujet','s',ha='left')
save(fig,'71-032')
