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
P=Pm(20,14,10); axes(ax,P,-1.5,4.4,-1.2,3.6)
c=P(1,2); o=P(0,0); q=P(3,1); r=10*math.sqrt(5)
a0=math.degrees(math.atan2(-2,-1)); 
line(ax,[(c[0]+r*math.cos(math.radians(a0+t)),c[1]+r*math.sin(math.radians(a0+t))) for t in range(0,91,4)],'fixe',lw=0.7,dash=True)
line(ax,[c,o],'sujet',lw=1.0); line(ax,[c,q],'resultat',lw=1.0)
arc(ax,c,9,a0+4,a0+86,'varie',lw=1.1)
dot(ax,o,'sujet',1.3); dot(ax,q,'resultat',1.3); dot(ax,c,'fixe',1.6)
text(ax,c[0]+1,c[1]+4,r'$c=(1\ ;\ 2)$','fixe','s',ha='left')
text(ax,c[0]+2,c[1]-6,'90°','varie','s'); text(ax,o[0]-1,o[1]-4,'0','sujet','s')
text(ax,q[0]+2,q[1]-3.5,r'$f(0)=(3\ ;\ 1)$','resultat','s',ha='left')
text(ax,66,56,'c ne bouge pas :','fixe','s'); text(ax,66,52,r'$f(c)=c$','fixe','m')
save(fig,'74-048')
