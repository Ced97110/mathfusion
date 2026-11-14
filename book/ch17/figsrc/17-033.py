import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def dot(ax, x, y, role, full=True, r=1.7):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role] if full else FILL['encre'], lw=1.0, zorder=4))

fig, ax = canvas(48); y = 18
f = numberline(ax, 8, 70, y, 1, 7)
arrow(ax, (f(5), y), (5, y), 'sujet', lw=2.0)
for v in (2, 4): dot(ax, f(v), y, 'resultat'); text(ax, f(v), y + 6, 'oui', 'resultat', 's')
dot(ax, f(5), y, 'sujet', r=2.1); text(ax, f(5), y + 6, r'$b$', 'sujet', 's')
dot(ax, f(6), y, 'limite'); text(ax, f(6), y + 6, 'non', 'limite', 's')
text(ax, f(3), y + 13, r'à gauche de $b$, ou sur $b$', 'sujet', 's')
text(ax, 44, 41, r'$a\leq b$ avec $b=5$', 'sujet', 'l')
save(fig, '17-033')
