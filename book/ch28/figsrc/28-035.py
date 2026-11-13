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

fig, ax = canvas(58)
box(ax, 31, 40, 26, 10, 'sujet', label='50°', size='l')
box(ax, 2, 4, 28, 10, 'resultat', label='−310°', size='l'); box(ax, 58, 4, 28, 10, 'resultat', label='410°', size='l')
arrow(ax, (38, 40), (22, 15.5), 'varie'); arrow(ax, (50, 40), (66, 15.5), 'varie')
text(ax, 64, 31, '+ 1 × 360°', 'varie', 's', ha='left'); text(ax, 64, 25, '1 tour, sens +', 'varie', 's', ha='left')
text(ax, 25, 31, '+ (−1) × 360°', 'varie', 's', ha='right'); text(ax, 25, 25, '1 tour, sens −', 'varie', 's', ha='right')
text(ax, 44, 55, 'point de départ', 'sujet', 's')
save(fig, '28-035')
