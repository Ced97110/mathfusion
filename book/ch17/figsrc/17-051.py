import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
def row(y, full, role, lab, st, strole, labels):
    f = numberline(ax, 8, 70, y, 0, 4, arrow_right=False, labels=labels)
    arrow(ax, (f(2) + 1.8, y), (80, y), role, lw=2.2)
    ax.add_patch(Circle((f(2), y), 1.8, ec=COL[role], fc=COL[role] if full else FILL['encre'], lw=1.3, zorder=3))
    text(ax, 6, y + 9, lab, role, 'l', ha='left')
    text(ax, 56, y + 9, st, strole, 's', ha='left')
    return f
row(48, False, 'fixe', r'$x > 2$', '2 refusé : point vide', 'limite', False)
f = row(22, True, 'sujet', r'$x \geq 2$', '2 accepté : point plein', 'resultat', True)
text(ax, 44, 4, 'seul le point change', 'varie', 's')
save(fig, '17-051')
