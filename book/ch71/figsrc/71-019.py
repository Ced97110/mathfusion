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

win=(-2,3,-1,5); pl=Pl(30,20,11); fig,ax=canvas(86)
frame(ax,pl,win); axes(ax,pl,win)
text(ax,44,82,r'$y=-2x+c$','sujet','l')
starts={0:-1.0,2:0.0,4:0.5}
for c in (0,2,4):
    lvl(ax,pl,2,1,c,win,'sujet',1.3)
    x0=starts[c]; y0=c-2*x0
    p0,p1,p2=pl(x0,y0),pl(x0+1,y0),pl(x0+1,y0-2)
    line(ax,[p0,p1],'varie',1.2); line(ax,[p1,p2],'varie',1.2)
    X,Y=pl((c+1)/2,-1); text(ax,X,Y-3.4,f'c = {c}','sujet','s')
text(ax,pl(0.5,2.9)[0]+3.8,pl(0.5,2.9)[1]+0.3,'1','varie','s')
text(ax,pl(1.5,2)[0]+4,pl(1.5,2)[1],'\u22122','varie','s')
save(fig,'71-019')
