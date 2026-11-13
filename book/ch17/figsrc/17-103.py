import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def odot(ax, x, y, role, closed=True, r=1.5):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role] if closed else FILL['encre'], lw=1.0, zorder=4))
def tl(f, ax, y, vals, role='fixe'):
    for v in vals:
        text(ax, f(v), y - 3.6, ('%g' % v).replace('-', '\u2212').replace('.', ','), role, 's')
def seg(ax, f, a, b, y, role, lw=2.4):
    line(ax, [(f(a), y), (f(b), y)], role, lw=lw)

fig, ax = canvas(60)
ya, yb = 44, 16
f = numberline(ax, 12, 60, ya, 0, 8, labels=False); g = numberline(ax, 12, 60, yb, 0, 8, labels=False)
tl(f, ax, ya, [0, 3, 8]); tl(g, ax, yb, [0, 3, 8])
odot(ax, f(5), ya, 'sujet', r=1.4); text(ax, f(5), ya + 5, '$S$', 'sujet', 'm'); text(ax, f(5), ya - 4, '$5$', 'sujet', 's')
text(ax, 44, 57, '$3x-5=10$ : un point', 'sujet', 's')
arrow(ax, (f(3), yb), (g(8) + 11, yb), 'autre', lw=2.4); odot(ax, g(3), yb, 'autre')
text(ax, g(3) - 4, yb + 5, '$T$', 'autre', 'm')
text(ax, 44, 4, '$4x\\geq 12$ : une demi-droite', 'autre', 's')
line(ax, [(f(3), ya - 7), (f(3), yb + 3)], 'fixe', lw=0.5, dash=True); line(ax, [(f(5), ya - 7), (f(5), yb + 3)], 'fixe', lw=0.5, dash=True)
save(fig, '17-103')
