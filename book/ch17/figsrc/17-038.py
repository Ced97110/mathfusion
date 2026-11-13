import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def dot(ax, x, y, role, full=True, r=1.7):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role] if full else FILL['encre'], lw=1.0, zorder=4))

fig, ax = canvas(48); y = 16
f = numberline(ax, 8, 66, y, 0, 6)
for a, b in ((0, 3), (3, 6)): line(ax, [(f(a), y), (f(b) if b == 3 else f(b) + 5, y)], 'resultat', lw=2.2)
dot(ax, f(3), y, 'limite', full=False, r=2.1)
text(ax, f(3), y + 8, 'non', 'limite', 's')
for v in (2, 5): dot(ax, f(v), y, 'resultat'); text(ax, f(v), y + 6, 'oui', 'resultat', 's')
text(ax, 44, 41, r'$x\neq 3$ : tout sauf $3$', 'sujet', 'l')
save(fig, '17-038')
