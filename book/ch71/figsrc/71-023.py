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

win=(-1,3,-1,4); pl=Pl(22,20,12); fig,ax=canvas(80)
frame(ax,pl,win); axes(ax,pl,win)
ylab=pl(0,-1)[1]-3.5
text(ax,12,ylab,'niveau','fixe','s')
for c in (0,2,4):
    lvl(ax,pl,2,1,c,win,'sujet',1.3)
    text(ax,pl((c+1)/2,-1)[0]+3.5,ylab,f'{c}','sujet','s')
for y in (0,2):
    A,B=pl(0,y),pl(1,y); arrow(ax,A,B,'varie',1.6)
    disc(ax,*A,1.1,'varie')
    text(ax,(A[0]+B[0])/2,A[1]-3.4,r'$+1$ kg','varie','s')
    text(ax,B[0]+4.2,B[1]+0.2,'+2','varie','s')
text(ax,44,76,'même pas, même écart','sujet','s')
save(fig,'71-023')
