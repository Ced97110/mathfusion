import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def odot(ax, x, y, role, closed=True, r=1.5):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role] if closed else FILL['encre'], lw=1.0, zorder=4))
def tl(f, ax, y, vals, role='fixe'):
    for v in vals:
        text(ax, f(v), y - 3.6, ('%g' % v).replace('-', '\u2212').replace('.', ','), role, 's')
def seg(ax, f, a, b, y, role, lw=2.4):
    line(ax, [(f(a), y), (f(b), y)], role, lw=lw)

fig, ax = canvas(64)
ya, yb = 48, 14
f = numberline(ax, 12, 66, ya, 0, 8, labels=False); g = numberline(ax, 12, 66, yb, 0, 8, labels=False)
odot(ax, f(3), ya, 'sujet'); odot(ax, f(7), ya, 'autre')
text(ax, f(3), ya - 5, '$3$', 'sujet', 's'); text(ax, f(7), ya - 5, '$7$', 'autre', 's')
text(ax, 44, 60, '$3<7$ : vrai', 'resultat', 'm')
arrow(ax, (f(3), ya - 8), (g(0) + 1, yb + 8), 'varie'); arrow(ax, (f(7), ya - 8), (g(0) + 3, yb + 8), 'varie')
text(ax, 58, 31, r'$\times 0$', 'varie', 'l')
odot(ax, g(0), yb, 'sujet', r=1.9); odot(ax, g(0) + 1.6, yb, 'autre', r=1.9)
text(ax, g(0), yb - 5, '$0$', 'fixe', 's'); text(ax, 54, yb + 6, '$0<0$ : faux', 'limite', 'm')
save(fig, '17-107')
