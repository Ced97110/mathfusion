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

fig,ax=canvas(68)
M=[(2,2),(6,2),(6,3.5),(3.5,3.5),(3.5,7),(2,7)]
def poster(o,k,role,ang=0,mir=False):
    poly(ax,tf([(0,0),(14*k,0),(14*k,9*k),(0,9*k)],o,ang,mir),role)
    poly(ax,tf([(x*k,y*k) for x,y in M],o,ang,mir),'fixe')
poster((6,44),1,'sujet'); poster((30,44),2,'autre')
text(ax,13,40.5,'50 cm','sujet','s'); text(ax,44,40.5,'100 cm','autre','s')
text(ax,24,49,'≠','limite','l'); text(ax,73,53,'distances','limite','s'); text(ax,73,49,'différentes','limite','s')
poster((6,10),1,'sujet'); poster((44,10),1,'varie',90); poster((84,10),1,'varie',0,True)
text(ax,13,29,'original','sujet','s'); text(ax,38,29,'tourné','varie','s'); text(ax,77,29,'retourné','varie','s')
text(ax,44,34.5,'50 cm : mêmes distances','resultat','s')
save(fig,'74-034')
