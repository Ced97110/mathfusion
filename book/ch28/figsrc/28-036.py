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

fig, ax = canvas(70); c = (44, 34); R = 24
ucirc(ax, c, R); axes_xy(ax, c, R)
P = pp(c, R, 130); N = (P[0], c[1])
line(ax, [c, P], 'fixe'); line(ax, [P, N], 'fixe', dash=True)
line(ax, [c, N], 'sujet', lw=2.4); dot(ax, P, 'sujet'); dot(ax, N, 'sujet', 0.8)
arcp(ax, c, 6, 6, 0, 130, 'varie')
text(ax, P[0] - 3, P[1] + 2.5, r'$P$', 'sujet'); text(ax, c[0] + 3, c[1] - 3, r'$O$', 'encre', 's'); text(ax, N[0], c[1] + 3, r'$N$', 'sujet', 's')
text(ax, 55, 45, TH + ' = 130°', 'varie', 's')
text(ax, 36, 25, r'$\cos\,\theta = x \approx -0{,}643$', 'sujet', 's')
save(fig, '28-036')
