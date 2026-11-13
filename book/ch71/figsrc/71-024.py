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

win=(0,5,0,4); pl=Pl(14,40,10); fig,ax=canvas(84)
frame(ax,pl,win); axes(ax,pl,win)
P=pl(1,2); R=pl(4,3)
arrow(ax,P,R,'varie',1.6)
disc(ax,*P,1.4,'sujet'); disc(ax,*R,1.4,'resultat')
text(ax,P[0]-1,P[1]+4.2,r'$P=(1,2)$','sujet','s')
text(ax,R[0]+1,R[1]+4.2,r'$P+w=(4,3)$','resultat','s')
text(ax,(P[0]+R[0])/2+1,(P[1]+R[1])/2-4.2,r'$w=(3,1)$','varie','s')
u=7; x0=6
box(ax,x0,22,4*u,9,'sujet',label=r'$f(P)=4$',size='s')
box(ax,x0+4*u,22,7*u,9,'varie',label=r'$f(w)=7$',size='s')
box(ax,x0,8,11*u,9,'resultat',label=r'$f(P+w)=11$',size='s')
save(fig,'71-024')
