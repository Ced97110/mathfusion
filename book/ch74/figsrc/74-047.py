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

fig,ax=canvas(56)
P=Pm(6,8,6); axes(ax,P,-0.4,8,-0.4,7)
a=P(2,5); b=P(5,6); c=P(1,2); d=P(4,3)
arrow(ax,a,b,'varie',lw=1.2); arrow(ax,c,d,'varie',lw=1.2)
dot(ax,a,'sujet',1.3); dot(ax,b,'resultat',1.3); dot(ax,c,'sujet',1.3); dot(ax,d,'resultat',1.3)
text(ax,a[0]-2,a[1]+3.5,'(2 ; 5)','sujet','s',ha='right'); text(ax,b[0]+1,b[1]+3.5,'(5 ; 6)','resultat','s',ha='left')
text(ax,(a[0]+b[0])/2,(a[1]+b[1])/2+6,r'$b=(3\ ;\ 1)$','varie','s')
text(ax,(c[0]+d[0])/2+3,(c[1]+d[1])/2-4.5,'même vecteur','varie','s')
dot(ax,(72,34),'sujet',1.3); disc(ax,72,34,3.6,'resultat',fill=False)
text(ax,72,44,r'$b=0$','varie','m'); text(ax,72,25,'rien ne bouge :','resultat','s'); text(ax,72,21.5,'identité','resultat','s')
save(fig,'74-047')
