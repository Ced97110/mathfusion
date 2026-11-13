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

win=(-4,4,-4,5); pl=Pl(34,40,7); fig,ax=canvas(86)
frame(ax,pl,win); axes(ax,pl,win)
text(ax,44,81,r'prix $f(x,y)=2x+y$','sujet','m')
ylab=pl(0,-4)[1]-3.5
text(ax,15,ylab,'niveau','fixe','s')
for c in (-4,-2,0,2,4):
    lvl(ax,pl,2,1,c,win,'limite' if c==0 else 'sujet',1.4 if c==0 else 1.2)
    text(ax,pl((c+4)/2,-4)[0],ylab,f'{c}'.replace('-','\u2212'),'limite' if c==0 else 'sujet','s')
for nm,(x,y) in (('P',(1,2)),('Q',(2,0))):
    disc(ax,*pl(x,y),1.3,'resultat'); text(ax,pl(x,y)[0]+4,pl(x,y)[1],nm,'resultat','m')
save(fig,'71-017')
