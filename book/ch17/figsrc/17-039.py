import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def dot(ax, x, y, role, full=True, r=1.7):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role] if full else FILL['encre'], lw=1.0, zorder=4))

fig, ax = canvas(74)
f = None
y = 50
f = numberline(ax, 8, 66, y, 0, 6)
arrow(ax, (f(3), y), (f(6) + 5, y), 'sujet', lw=2.0); dot(ax, f(3), y, 'sujet', full=False, r=2.1)
text(ax, 4, y + 13, r'$x>3$', 'sujet', 'l', ha='left'); text(ax, 84, y + 13, 'une direction', 'sujet', 's', ha='right')
y = 16
f = numberline(ax, 8, 66, y, 0, 6)
arrow(ax, (f(3), y), (f(6) + 5, y), 'autre', lw=2.0); arrow(ax, (f(3), y), (4, y), 'autre', lw=2.0)
dot(ax, f(3), y, 'autre', full=False, r=2.1)
for v in (2, 5): dot(ax, f(v), y, 'resultat')
text(ax, 4, y + 13, r'$x\neq 3$', 'autre', 'l', ha='left'); text(ax, 84, y + 13, 'deux directions', 'autre', 's', ha='right')
save(fig, '17-039')
