import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def Pm(ox, oy, s): return lambda x, y: (ox + x * s, oy + y * s)
def axes(ax, P, x0, x1, y0, y1):
    line(ax, [P(x0, 0), P(x1, 0)], 'fixe', lw=0.5); line(ax, [P(0, y0), P(0, y1)], 'fixe', lw=0.5)
def dot(ax, p, role, r=1.1): disc(ax, p[0], p[1], r, role)
def arc(ax, c, r, a0, a1, role, lw=1.0):
    n = 24; pts = [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
    line(ax, pts, role, lw=lw); arrow(ax, pts[-3], pts[-1], role, lw=lw)
def tf(pts, o, ang=0, mir=False):
    a = math.radians(ang); out = []
    for x, y in pts:
        if mir: x = -x
        out.append((o[0] + x * math.cos(a) - y * math.sin(a), o[1] + x * math.sin(a) + y * math.cos(a)))
    return out

fig,ax=canvas(62)
P=Pm(20,16,8); axes(ax,P,-1.5,4.5,-0.6,4.2)
T=[(1,0),(2,0),(1,1)]; T2=[(0,1),(0,2),(-1,1)]; T3=[(3,2),(3,3),(2,2)]
poly(ax,[P(*p) for p in T],'sujet'); poly(ax,[P(*p) for p in T2],'varie'); poly(ax,[P(*p) for p in T3],'resultat')
arc(ax,P(0,0),8.5,12,78,'varie'); text(ax,P(0,0)[0]+11,P(0,0)[1]+9,r'$A$','varie','m')
arrow(ax,P(0.2,1.1),P(2.8,2.1),'fixe',lw=1.0); text(ax,P(1.6,1.2)[0]+3,P(1.6,1.2)[1]-4,r'$b$','fixe','m')
text(ax,P(1.5,-0.1)[0]+2,P(1.5,-0.1)[1]-4,'départ','sujet','s'); text(ax,P(-0.4,2.1)[0]-1,P(-0.4,2.1)[1]+4,'après A','varie','s')
text(ax,P(2.9,3.2)[0]+1,P(2.9,3.2)[1]+4,'après A, puis b','resultat','s')
text(ax,66,8,r'$f(x)=Ax+b$,  $A\in O(2)$','encre','m'); text(ax,66,2.8,'A : ¼ tour ; b : (3 ; 1)','fixe','s')
save(fig,'74-038')
