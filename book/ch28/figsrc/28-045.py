import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def pp(c, R, d): return (c[0] + R * math.cos(math.radians(d)), c[1] + R * math.sin(math.radians(d)))
def axes_xy(ax, c, R, ext=4):
    arrow(ax, (c[0] - R - ext, c[1]), (c[0] + R + ext, c[1]), 'fixe', lw=0.7)
    arrow(ax, (c[0], c[1] - R - ext), (c[0], c[1] + R + ext), 'fixe', lw=0.7)
def ucirc(ax, c, R): ax.add_patch(Circle(c, R, ec=COL['fixe'], fc='none', lw=0.8, zorder=1))
def arcp(ax, c, r0, r1, a0, a1, role, lw=1.0, head=True):
    n = max(8, int(abs(a1 - a0) / 4)); pts = [pp(c, r0 + (r1 - r0) * i / n, a0 + (a1 - a0) * i / n) for i in range(n + 1)]
    line(ax, pts, role, lw=lw)
    if head: arrow(ax, pts[-2], pts[-1], role, lw=lw)
def dot(ax, p, role, r=1.1): ax.add_patch(Circle(p, r, ec=COL[role], fc=COL[role], zorder=4))
TH = r'$\theta$'

fig, ax = canvas(66); c = (44, 33); R = 24
ucirc(ax, c, R); axes_xy(ax, c, R)
for a in (30, 210):
    P = pp(c, R, a); N = (P[0], c[1])
    line(ax, [c, N], 'fixe', dash=True); line(ax, [N, P], 'sujet', lw=2.4); dot(ax, P, 'sujet', 1.4)
text(ax, 72, 42, r'$y = 0{,}5$', 'sujet', 's'); text(ax, 15, 21, r'$y = -0{,}5$', 'sujet', 's')
text(ax, 55, 48, r'$P$', 'sujet'); text(ax, 33, 17, r'$P$', 'sujet'); text(ax, 47, 29.5, r'$O$', 'encre', 's')
text(ax, 44, 63, 'au-dessus : +   en dessous : −', 'sujet', 's')
save(fig, '28-045')
