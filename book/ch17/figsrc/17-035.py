import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def dot(ax, x, y, role, full=True, r=1.7):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role] if full else FILL['encre'], lw=1.0, zorder=4))

fig, ax = canvas(48); y = 18
f = numberline(ax, 8, 66, y, 7, 13)
arrow(ax, (f(10), y), (f(13) + 5, y), 'sujet', lw=2.0)
dot(ax, f(10), y, 'sujet', r=2.1)
text(ax, f(10), y + 8, 'ou égal', 'sujet', 's'); line(ax, [(f(10), y + 5.5), (f(10), y + 3.4)], 'sujet')
dot(ax, f(9), y, 'limite'); text(ax, f(9) - 3, y + 6, 'non', 'limite', 's')
dot(ax, f(12), y, 'resultat'); text(ax, f(12), y + 6, 'oui', 'resultat', 's')
text(ax, f(12), y + 13, 'supérieur', 'sujet', 's')
text(ax, 44, 41, r'$n\geq 10$', 'sujet', 'l')
save(fig, '17-035')
