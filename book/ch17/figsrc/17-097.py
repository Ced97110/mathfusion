import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def odot(ax, x, y, role, closed=True, r=1.5):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role] if closed else FILL['encre'], lw=1.0, zorder=4))
def tl(f, ax, y, vals, role='fixe'):
    for v in vals:
        text(ax, f(v), y - 3.6, ('%g' % v).replace('-', '\u2212').replace('.', ','), role, 's')
def seg(ax, f, a, b, y, role, lw=2.4):
    line(ax, [(f(a), y), (f(b), y)], role, lw=lw)

fig, ax = canvas(72)
ya, yb = 56, 14
f = numberline(ax, 8, 64, ya, -4, 7, labels=False)
g = numberline(ax, 8, 64, yb, -4, 7, labels=False)
seg(ax, f, -3, 6, ya, 'sujet'); seg(ax, g, -2, 1, yb, 'sujet')
odot(ax, f(-3), ya, 'sujet'); odot(ax, f(6), ya, 'sujet', False)
odot(ax, g(1), yb, 'sujet'); odot(ax, g(-2), yb, 'sujet', False)
text(ax, 8, ya + 7, r'$-3\leq -3x<6$', 'sujet', 'm', ha='left')
text(ax, 8, yb + 8, r'$1\geq x>-2$', 'sujet', 'm', ha='left')
text(ax, f(-3), ya - 5, '$-3$', 'sujet', 's'); text(ax, f(-3), ya - 8.5, 'inclus', 'fixe', 's')
text(ax, f(6), ya - 5, '$6$', 'sujet', 's'); text(ax, f(6), ya - 8.5, 'exclu', 'fixe', 's')
text(ax, g(1), yb - 5, '$1$', 'sujet', 's'); text(ax, g(1), yb - 8.5, 'inclus', 'fixe', 's')
text(ax, g(-2), yb - 5, '$-2$', 'sujet', 's'); text(ax, g(-2), yb - 8.5, 'exclu', 'fixe', 's')
arrow(ax, (f(-3), ya - 12), (g(1), yb + 13), 'varie'); arrow(ax, (f(6), ya - 12), (g(-2), yb + 13), 'varie')
text(ax, 64, 36, r'$\div(-3)$', 'varie', 'm', ha='left')
save(fig, '17-097')
