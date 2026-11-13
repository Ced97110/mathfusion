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

win=(-2,3,-3,4); pl=Pl(26,30,9.5); fig,ax=canvas(76)
frame(ax,pl,win); axes(ax,pl,win)
for c in (2,4): lvl(ax,pl,2,1,c,win,'sujet',1.2)
lvl(ax,pl,2,1,0,win,'limite',1.6)
for c in (2,4):
    s=clipline(2,1,c,win)[1]; X,Y=pl(*s); text(ax,X-1,Y+4,f'niveau {c}','sujet','s',ha='right')
X,Y=pl(-1.4,2.8); text(ax,X+5,Y+7.5,'niveau 0','limite','s')
O=pl(0,0); disc(ax,*O,1.4,'resultat'); text(ax,O[0]-5.2,O[1]+3,'O','resultat','m')
X,Y=pl(1,-2); disc(ax,X,Y,1.4,'resultat'); text(ax,X-3.2,Y-1.5,r'$(1,-2)$ : 0','resultat','s',ha='right')
text(ax,O[0]-12,O[1]-5,r'$f(0,0)=0$','resultat','s')
save(fig,'71-020')
