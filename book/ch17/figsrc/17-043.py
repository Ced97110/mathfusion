import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def dot(ax, x, y, role, full=True, r=1.7):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role] if full else FILL['encre'], lw=1.0, zorder=4))

fig, ax = canvas(74)
text(ax, 6, 66, 'à retourner', 'autre', 's', ha='left'); text(ax, 50, 66, 'se lit tout de suite', 'sujet', 's', ha='left')
box(ax, 2, 48, 38, 12, 'autre', label=r'$3<x$'); box(ax, 48, 48, 38, 12, 'sujet', label=r'$x>3$')
y = 18
f = numberline(ax, 8, 66, y, 1, 6)
arrow(ax, (f(3), y), (f(6) + 5, y), 'sujet', lw=2.0); dot(ax, f(3), y, 'sujet', full=False, r=2.1)
arrow(ax, (67, 47), (f(5), y + 4), 'varie'); arrow(ax, (21, 47), (f(3.4), y + 4), 'varie')
save(fig, '17-043')
