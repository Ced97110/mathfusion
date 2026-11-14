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
for a, lab, off in ((30, r'$x \approx 0{,}866$', 0), (130, r'$x \approx -0{,}643$', 0)):
    P = pp(c, R, a); N = (P[0], c[1])
    line(ax, [P, N], 'fixe', dash=True); line(ax, [c, N], 'sujet', lw=2.4); dot(ax, P, 'sujet', 1.4)
    text(ax, (c[0] + N[0]) / 2 + (6 if a == 30 else -6), c[1] - 5.5, lab, 'sujet', 's')
text(ax, 62, 49, r'$P$', 'sujet'); text(ax, 24, 56, r'$P$', 'sujet')
text(ax, 70, 38, 'droite', 'sujet', 's'); text(ax, 17, 38, 'gauche', 'sujet', 's'); text(ax, 47, 29, r'$O$', 'encre', 's')
save(fig, '28-044')
