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

import math
winL=(-0.5,3,-0.5,4.5); L=Pl(12,12,8); fig,ax=canvas(64)
frame(ax,L,winL); axes(ax,L,winL)
lvl(ax,L,2,1,4,winL,'sujet',1.5)
R=Pl(66,32,12)
line(ax,[R(-1.6,0),R(1.6,0)],'fixe',0.5); line(ax,[R(0,-1.6),R(0,1.6)],'fixe',0.5)
a=math.sqrt(0.5); b=math.sqrt(2); s2=math.sqrt(2)
pts=[R((a*math.cos(t)+b*math.sin(t))/s2,(a*math.cos(t)-b*math.sin(t))/s2) for t in [i*2*math.pi/90 for i in range(91)]]
line(ax,pts,'sujet',1.5)
X,Y=R(1,-1); disc(ax,X,Y,1.3,'resultat'); text(ax,X-8,Y-3.5,r'$(1,-1)$','resultat','s')
text(ax,22,58,r'$2x+y=4$','sujet','m')
text(ax,66,58,r'$5x^2+6xy+5y^2=4$','sujet','m')
text(ax,22,5,'niveau : une droite','sujet','s')
text(ax,66,5,'niveau : une courbe','sujet','s')
save(fig,'71-027')
