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

win=(-3,3,-2,5); pl=Pl(30,30,9); fig,ax=canvas(80)
frame(ax,pl,win); axes(ax,pl,win)
lvl(ax,pl,2,1,0,win,'limite',1.5); lvl(ax,pl,2,1,4,win,'sujet',1.5)
X,Y=pl(-1.1,4.2); text(ax,X,Y,'niveau 0','limite','s')
X,Y=pl(0.35,4.6); text(ax,X+4,Y,'niveau 4','sujet','s')
P=pl(1,2); Q=pl(2,0); W=pl(-1,2); O=pl(0,0)
arrow(ax,Q,P,'varie',1.7); arrow(ax,O,W,'varie',1.7)
for pt,nm in ((P,'P'),(Q,'Q')):
    disc(ax,*pt,1.3,'resultat'); text(ax,pt[0]+3.6,pt[1]+0.5,nm,'resultat','m')
text(ax,pl(0.45,1)[0],pl(0.45,1)[1],r'$P-Q$','varie','s')
text(ax,pl(2.55,1.2)[0],pl(2.55,1.2)[1],r'$P-Q$','varie','s')
text(ax,44,7,r'$f(P-Q)=2\times(-1)+2=0$','resultat','s')
save(fig,'71-025')
