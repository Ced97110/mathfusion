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
c=(44,12); R=24
arrow(ax,c,(c[0]+R,c[1]),'sujet',lw=1.3); arrow(ax,c,(c[0],c[1]+R),'varie',lw=1.3); arrow(ax,c,(c[0]-R,c[1]),'resultat',lw=1.3)
dot(ax,c,'fixe',1.1)
arc(ax,c,9,2,88,'varie',lw=0.9); arc(ax,c,9.0,92,178,'resultat',lw=0.9) if False else arc(ax,c,12,92,178,'resultat',lw=0.9)
arc(ax,c,19,2,178,'fixe',lw=1.0)
text(ax,c[0]+R+1,c[1]-4.5,r'$x$','sujet','m'); text(ax,c[0]+3,c[1]+R+3,r'$Bx$','varie','m'); text(ax,c[0]-R-1,c[1]-4.5,r'$ABx$','resultat','m')
text(ax,c[0]+12,c[1]+9,'¼ tour','varie','s',ha='left'); text(ax,c[0]-12,c[1]+13,'¼ tour','resultat','s',ha='right')
text(ax,c[0]+1,c[1]+23,'½ tour','fixe','s')
text(ax,44,48,r'$A\,B$ : un demi-tour','encre','m'); text(ax,44,55,'b et c : sans effet sur le tour','fixe','s')
save(fig,'74-045')
