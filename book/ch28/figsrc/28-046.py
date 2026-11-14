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

fig, ax = canvas(80)
box(ax, 8, 62, 30, 12, 'sujet', label=r'$\cos\,\theta$', size='l'); text(ax, 46, 68, '=', 'encre', 'l'); box(ax, 54, 62, 26, 12, 'resultat', label=r'$x$', size='l')
text(ax, 23, 58, 'nom', 'sujet', 's'); text(ax, 67, 58, 'abscisse de P', 'resultat', 's')
c = (44, 28); R = 20
ucirc(ax, c, R); axes_xy(ax, c, R, 3)
for a, lab, dx in ((30, '0,866', 9), (130, '−0,643', -8)):
    P = pp(c, R, a); N = (P[0], c[1])
    line(ax, [P, N], 'fixe', dash=True); line(ax, [c, N], 'resultat', lw=2.4); dot(ax, P, 'sujet', 1.3)
    text(ax, c[0] + dx, c[1] - 4.5, lab, 'resultat', 's')
text(ax, 57, 45, r'$P$', 'sujet', 's'); text(ax, 30, 47, r'$P$', 'sujet', 's'); text(ax, 47, 24.5, r'$O$', 'encre', 's')
save(fig, '28-046')
