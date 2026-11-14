import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def dot(ax, x, y, role, full=True, r=1.7):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role] if full else FILL['encre'], lw=1.0, zorder=4))

fig, ax = canvas(48); y = 18
f = numberline(ax, 8, 66, y, 13, 18)
arrow(ax, (f(15), y), (f(18) + 5, y), 'sujet', lw=2.0)
dot(ax, f(15), y, 'sujet', full=False, r=2.1)
text(ax, f(15), y + 8, '15 refusé', 'limite', 's'); line(ax, [(f(15), y + 5.5), (f(15), y + 3.3)], 'limite')
dot(ax, f(16), y, 'resultat'); text(ax, f(16.9), y + 6, '16 convient', 'resultat', 's')
text(ax, f(17.2), y + 13, 'à droite de 15', 'sujet', 's')
text(ax, 44, 41, r'$p>15$', 'sujet', 'l')
save(fig, '17-034')
