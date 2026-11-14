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

fig, ax = canvas(84)
box(ax, 8, 66, 30, 12, 'sujet', label=r'$\sin\,\theta$', size='l'); text(ax, 46, 72, '=', 'encre', 'l'); box(ax, 54, 66, 26, 12, 'resultat', label=r'$y$', size='l')
text(ax, 23, 62, 'nom', 'sujet', 's'); text(ax, 67, 62, 'ordonnée de P', 'resultat', 's')
c = (44, 32); R = 22
ucirc(ax, c, R); axes_xy(ax, c, R, 3)
for a, lab in ((30, '0,5'), (210, '−0,5')):
    P = pp(c, R, a); N = (P[0], c[1])
    line(ax, [c, N], 'fixe', dash=True); line(ax, [N, P], 'resultat', lw=2.4); dot(ax, P, 'sujet', 1.3)
    text(ax, N[0] + (4.5 if a == 30 else -4.5), (P[1] + c[1]) / 2, lab, 'resultat', 's', ha='left' if a == 30 else 'right')
text(ax, 57, 45, r'$P$', 'sujet', 's'); text(ax, 31, 17, r'$P$', 'sujet', 's'); text(ax, 47, 28.5, r'$O$', 'encre', 's')
save(fig, '28-047')
