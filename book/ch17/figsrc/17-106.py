import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def odot(ax, x, y, role, closed=True, r=1.5):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role] if closed else FILL['encre'], lw=1.0, zorder=4))
def tl(f, ax, y, vals, role='fixe'):
    for v in vals:
        text(ax, f(v), y - 3.6, ('%g' % v).replace('-', '\u2212').replace('.', ','), role, 's')
def seg(ax, f, a, b, y, role, lw=2.4):
    line(ax, [(f(a), y), (f(b), y)], role, lw=lw)

fig, ax = canvas(72)
ya, yb = 52, 18
box(ax, 4, ya - 8, 30, 14, 'fixe', label='$3x-5=10$', size='s')
arrow(ax, (35, ya - 1), (45, ya - 1), 'fixe')
f = numberline(ax, 50, 70, ya - 1, 0, 8, labels=False, arrow_right=False)
odot(ax, f(5), ya - 1, 'resultat', r=1.9); text(ax, f(5), ya - 6, '$5$', 'resultat', 's')
text(ax, 60, ya + 11, 'un nombre', 'resultat', 's')
text(ax, 19, ya + 11, 'chapitre 16', 'fixe', 's')
box(ax, 4, yb - 8, 30, 14, 'sujet', label=r'$4x\geq 12$', size='s')
arrow(ax, (35, yb - 1), (45, yb - 1), 'sujet')
g = numberline(ax, 48, 70, yb - 1, 0, 8, labels=False, arrow_right=False)
arrow(ax, (g(3), yb - 1), (80, yb - 1), 'resultat', lw=2.4); odot(ax, g(3), yb - 1, 'resultat')
text(ax, 62, yb + 8, 'un bord et un côté', 'resultat', 's'); text(ax, g(3), yb - 6, '$3$', 'resultat', 's')
text(ax, 19, yb + 11, 'ce chapitre', 'sujet', 's')
save(fig, '17-106')
