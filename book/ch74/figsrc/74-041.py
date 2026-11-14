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

fig,ax=canvas(52)
P=Pm(6,10,9); o=P(0,0); axes(ax,P,-0.4,3.8,-1.4,2.6)
x=P(3,1); y=P(1,2)
arrow(ax,o,x,'sujet',lw=1.2); arrow(ax,o,y,'autre',lw=1.2); arrow(ax,y,x,'varie',lw=1.2)
text(ax,x[0]+1.5,x[1]-3.5,r'$x$','sujet','m'); text(ax,y[0]-2.5,y[1]+2,r'$y$','autre','m'); text(ax,(x[0]+y[0])/2+6,(x[1]+y[1])/2+3.5,r'$x-y$','varie','m')
text(ax,65,44,r'$|x|^2=10$','sujet','m'); text(ax,65,36,r'$|y|^2=5$','autre','m'); text(ax,65,28,r'$|x-y|^2=5$','varie','m')
text(ax,65,18,r'$\frac{1}{2}(10+5-5)=5$','resultat','m')
text(ax,65,9,r'$3\times1+1\times2=5$','resultat','s')
save(fig,'74-041')
