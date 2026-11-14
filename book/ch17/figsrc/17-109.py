import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def odot(ax, x, y, role, closed=True, r=1.5):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role] if closed else FILL['encre'], lw=1.0, zorder=4))
def tl(f, ax, y, vals, role='fixe'):
    for v in vals:
        text(ax, f(v), y - 3.6, ('%g' % v).replace('-', '\u2212').replace('.', ','), role, 's')
def seg(ax, f, a, b, y, role, lw=2.4):
    line(ax, [(f(a), y), (f(b), y)], role, lw=lw)

fig, ax = canvas(68)
ya, yb = 52, 14
f = numberline(ax, 8, 70, ya, -6, 8, labels=False); g = numberline(ax, 8, 70, yb, -6, 8, labels=False)
pts = [(-5, 'autre'), (3, 'sujet'), (7, 'varie')]
for v, r in pts:
    odot(ax, f(v), ya, r); text(ax, f(v), ya - 5, ('%d' % v).replace('-', '\u2212'), r, 's')
    odot(ax, g(0) + 0 * v, yb, r, False, r=1.9 + 0.7 * (2 - pts.index((v, r))))
    arrow(ax, (f(v), ya - 8), (g(0), yb + 5), 'varie')
text(ax, 68, 34, r'$\times 0$', 'varie', 'l')
text(ax, g(0), yb - 5, '$0$', 'fixe', 's')
text(ax, 44, 4, 'lequel était à gauche ?', 'limite', 's')
text(ax, 44, 63, 'trois points différents', 'fixe', 's')
save(fig, '17-109')
