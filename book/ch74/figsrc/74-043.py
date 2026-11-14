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

fig,ax=canvas(58)
T=[(1,0),(2,0),(1,1)]
PL=Pm(18,22,6.5); axes(ax,PL,-2.4,3,-0.8,3)
poly(ax,[PL(*p) for p in T],'fixe'); poly(ax,[PL(-p[1],p[0]) for p in T],'sujet')
arc(ax,PL(0,0),6,12,78,'sujet'); dot(ax,PL(0,0),'sujet',1.2)
text(ax,22,46,r'$A$ : partie linéaire','sujet','s'); text(ax,22,8,'l’origine ne bouge pas','sujet','s')
PR=Pm(50,22,6.5); axes(ax,PR,-0.8,5.2,-0.8,3)
poly(ax,[PR(*p) for p in T],'fixe'); poly(ax,[PR(p[0]+3,p[1]+1) for p in T],'varie')
arrow(ax,PR(1.2,0.3),PR(4.2,1.3),'varie',lw=1.1); dot(ax,PR(0,0),'fixe',1.0)
text(ax,69,46,r'$b$ : partie translation','varie','s'); text(ax,69,8,'tous glissent de b','varie','s')
text(ax,44,54,r'$f(x)=Ax+b$','encre','m')
save(fig,'74-043')
