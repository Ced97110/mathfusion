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

fig,ax=canvas(76)
box(ax,3,44,82,30,'autre')
text(ax,44,69,r'$F$ : le corps des nombres','autre','m')
for i,s in enumerate(('\u211a','\u211d','\u2102','\u2124/5')):
    box(ax,6+i*20.5,48,18,12,'autre',label=s,size='l')
box(ax,3,2,82,38,'sujet')
text(ax,44,35,r'$V$ : espace de dimension $n$','sujet','m')
O=(14,9)
arrow(ax,O,(38,9),'sujet',1.6); arrow(ax,O,(14,27),'sujet',1.6); arrow(ax,O,(36,26),'sujet',1.6)
text(ax,42,9,r'$e_1$','sujet','m'); text(ax,14,30,r'$e_2$','sujet','m'); text(ax,40,28,r'$e_n$','sujet','m')
text(ax,63,18,'une base :','sujet','s'); text(ax,63,12,r'$(e_1,\dots,e_n)$','sujet','m')
save(fig,'71-028')
