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
P=Pm(44,20,7.5); o=P(0,0); axes(ax,P,-4.2,3.2,-1.2,4.2)
e1=P(1,0); e2=P(0,1)
arrow(ax,o,P(0,1),'sujet',lw=1.3); arrow(ax,o,P(-1,0),'varie',lw=1.3)
line(ax,[P(-3,0),P(-3,2)],'fixe',lw=0.7,dash=True); line(ax,[P(0,2),P(-3,2)],'fixe',lw=0.7,dash=True)
arrow(ax,o,P(-3,2),'resultat',lw=1.2)
dot(ax,P(-3,2),'resultat',1.2); dot(ax,P(-3,0),'varie',0.9); dot(ax,P(0,2),'sujet',0.9)
text(ax,P(0,1)[0]+5,P(0,1)[1]-0.5,r'$u_1=(0\ ;\ 1)$','sujet','s',ha='left')
text(ax,P(-1,0)[0],P(-1,0)[1]-4,r'$u_2=(-1\ ;\ 0)$','varie','s')
text(ax,P(-3,0)[0]+1,P(-3,0)[1]-4,r'$3u_2$','varie','s'); text(ax,P(0,2)[0]+5,P(0,2)[1]+0.5,r'$2u_1$','sujet','s',ha='left')
text(ax,P(-3,2)[0]-1,P(-3,2)[1]+4,r'$g(x)=(-3\ ;\ 2)$','resultat','s')
text(ax,44,7,r'$x=(2\ ;\ 3)$ : $g(x)=2u_1+3u_2$','encre','s')
save(fig,'74-042')
