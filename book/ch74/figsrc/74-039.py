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
P=Pm(18,14,8); axes(ax,P,-1.5,4.3,-0.8,4.3)
T=[(0,0),(2,0),(0,1)]; R=[(0,0),(0,2),(-1,0)]; b=(3,1)
poly(ax,[P(*p) for p in T],'sujet')
poly(ax,[P(p[0]+b[0],p[1]+b[1]) for p in R],'varie')
poly(ax,[P(*p) for p in R],'resultat')
arrow(ax,P(0,0),P(3,1),'varie',lw=1.1); pass
arrow(ax,P(3,3),P(0,2),'fixe',lw=0.9,curve=0.25); text(ax,P(1.5,3.2)[0],P(1.5,3.2)[1]+3,r'$-b$','fixe','m')
dot(ax,P(0,0),'fixe',1.0); dot(ax,P(3,1),'varie',1.2)
text(ax,P(3,1)[0]+3,P(3,1)[1]-4.5,r'$b=f(0)$','varie','s',ha='left'); text(ax,P(0,0)[0]-1,P(0,0)[1]-4,'0','fixe','s')
text(ax,P(-1,1)[0]-1,P(-1,1)[1]+5,'g(T)','resultat','s')
text(ax,P(4,2.2)[0]-3,P(4,2.2)[1]+4,'f(T)','varie','s'); text(ax,P(1,0)[0]+5,P(1,0)[1]-4.5,'T','sujet','s')
text(ax,66,52,r'$g(x)=f(x)-b$','resultat','m'); text(ax,66,45,r'$g(0)=0$','resultat','m')
save(fig,'74-039')
