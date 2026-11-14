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

fig, ax = canvas(84); c = (44, 32); R = 24
ucirc(ax, c, R); axes_xy(ax, c, R)
P = pp(c, R, 130); N = (P[0], c[1])
line(ax, [pp(c, 28, 130), pp(c, 28, 310)], 'sujet', lw=1.4, dash=True)
line(ax, [c, N], 'fixe', lw=2.2); line(ax, [N, P], 'fixe', lw=2.2); dot(ax, P, 'sujet', 1.3)
text(ax, P[0] - 3, P[1] + 2.5, r'$P$', 'sujet'); text(ax, c[0] + 3, c[1] - 3, r'$O$', 'encre', 's')
text(ax, 35.6, c[1] - 4, r'$x$', 'fixe', 's'); text(ax, P[0] - 3, 43, r'$y$', 'fixe', 's')
text(ax, 44, 77, r'$\tan\,\theta = y \div x$', 'sujet', 'l')
text(ax, 44, 69, r'$0{,}766 \div (-0{,}643) \approx -1{,}19$', 'resultat', 's')
save(fig, '28-039')
