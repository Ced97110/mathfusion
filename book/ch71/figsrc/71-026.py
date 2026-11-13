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

win=(-3,5,-2,3.5); pl=Pl(28,26,9); fig,ax=canvas(70)
frame(ax,pl,win); axes(ax,pl,win)
text(ax,44,64,r'$f(x,y)=x+3y$','sujet','l')
for c in (0,3,6):
    lvl(ax,pl,1,3,c,win,'sujet',1.3)
    X,Y=pl(5,(c-5)/3); text(ax,X+3.5,Y,f'{c}','sujet','s')
arrow(ax,pl(0,0),pl(0,1),'varie',1.5); arrow(ax,pl(0,1),pl(0,2),'varie',1.5)
for y in (0.5,1.5): text(ax,pl(-0.62,y)[0],pl(-0.62,y)[1],'+3','varie','s')
text(ax,44,5,'chaque droite porte sa valeur','sujet','s')
save(fig,'71-026')
