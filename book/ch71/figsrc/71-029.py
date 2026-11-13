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

win=(0,4,0,2.6); pl=Pl(12,16,16); fig,ax=canvas(64)
frame(ax,pl,win); axes(ax,pl,win)
for i in range(3): arrow(ax,pl(i,0),pl(i+1,0),'sujet',1.8)
for j in range(2): arrow(ax,pl(3,j),pl(3,j+1),'autre',1.8)
X,Y=pl(3,2); disc(ax,X,Y,1.5,'resultat'); text(ax,X,Y+4,r'$(3,2)$','resultat','m')
text(ax,pl(1.5,0)[0],pl(1.5,0)[1]+4.2,r'$e_1=(1,0)$','sujet','s')
text(ax,pl(3,0.5)[0]-4,pl(3,0.5)[1],r'$e_2=(0,1)$','autre','s',ha='right')
brace(ax,pl(0,0)[0],pl(3,0)[0],pl(0,0)[1]-1.5,'sujet',r'$3\times e_1$','down')
text(ax,pl(3,1.5)[0]+4,pl(3,1.5)[1],r'$2\times e_2$','autre','s',ha='left')
save(fig,'71-029')
