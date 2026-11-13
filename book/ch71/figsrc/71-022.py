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

win=(-4,4,-2.5,2.5); pl=Pl(44,30,8); fig,ax=canvas(62)
frame(ax,pl,win); axes(ax,pl,win)
import math
for c in (-4,-2,0,2,4): lvl(ax,pl,2,1,c,win,'sujet',1.2)
line(ax,[pl(-4,-2),pl(4,2)],'varie',1.3,dash=True)
for c in (-4,-2,0,2,4):
    X,Y=pl(2*c/5,c/5); disc(ax,X,Y,1.0,'varie')
    text(ax,X+3.0,Y+3.0,f'{c}'.replace('-','\u2212'),'sujet','s')
O=pl(0,0); n=math.sqrt(5); d1=(2/n,1/n); d2=(1/n,-2/n); a=2.2
line(ax,[(O[0]+a*d1[0],O[1]+a*d1[1]),(O[0]+a*(d1[0]+d2[0]),O[1]+a*(d1[1]+d2[1])),(O[0]+a*d2[0],O[1]+a*d2[1])],'varie',0.8)
arrow(ax,pl(0,0),pl(2,1),'varie',1.6)
text(ax,pl(2,1)[0]+1,pl(2,1)[1]-3.5,r'$(2,1)$','varie','s',ha='left')
text(ax,44,54,'étiquettes alignées, angle droit','varie','s')
save(fig,'71-022')
