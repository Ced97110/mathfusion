import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def dot(ax, x, y, role, full=True, r=1.7):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role] if full else FILL['encre'], lw=1.0, zorder=4))

fig, ax = canvas(98)
rows = ((92, r'$x+7>4$', 'retirer 7 des deux côtés', r'$x>-3$', r'$-3$', -3, False, 'bord : point vide'),
        (45, r'$4x\geq 12$', 'diviser par 4', r'$x\geq 3$', r'$3$', 3, True, 'bord : point plein'))
for yt, ineq, op, res, anum, a, full, bord in rows:
    text(ax, 2, yt, ineq, 'sujet', 'm', ha='left')
    text(ax, 86, yt, op, 'varie', 's', ha='right')
    arrow(ax, (6, yt - 3), (6, yt - 6), 'varie', lw=1.0)
    text(ax, 2, yt - 9, res, 'resultat', 'l', ha='left', weight='bold')
    y = yt - 24
    f = numberline(ax, 8, 70, y, -6, 6, labels=False)
    arrow(ax, (f(a), y), (f(6) + 5, y), 'sujet', lw=2.0); dot(ax, f(a), y, 'sujet', full=full, r=2.1)
    text(ax, f(a), y + 4.5, anum, 'encre', 's')
    text(ax, (f(a) + f(6)) / 2 + 8, y + 5, 'côté : droite', 'sujet', 's')
    text(ax, f(a), y - 6, bord, 'sujet', 's')
save(fig, '17-045')
