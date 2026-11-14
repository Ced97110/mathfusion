import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def dot(ax, x, y, role, r=1.1, hollow=False):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc="white" if hollow else COL[role], lw=0.9, zorder=6))

fig, ax = canvas(70)
for y, a, b, name in [(52, 2, 5, 'haut'), (20, -5, -2, 'bas')]:
    f = numberline(ax, 6, 70, y, -6, 6, labels=False)
    text(ax, f(0), y - 4.5, '0', 'fixe', 's')
    dot(ax, f(a), y, 'sujet', 1.3); dot(ax, f(b), y, 'autre', 1.3)
    arrow(ax, (f(a), y + 2.5), (f(b), y + 2.5), 'resultat', curve=-0.45)
    text(ax, f(a), y - 4.5, rf'$a={a}$'.replace('-', '−'), 'sujet', 's')
    text(ax, f(b), y - 4.5, rf'$b={b}$'.replace('-', '−'), 'autre', 's')
    text(ax, (f(a) + f(b)) / 2, y + 9, 'écart de 3', 'fixe', 's')
text(ax, 44, 66, 'même écart : la flèche va vers la droite', 'resultat', 's')
save(fig, '12-086')
