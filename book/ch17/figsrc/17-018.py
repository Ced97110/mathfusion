import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
def dot(x, y, role, full):
    ax.add_patch(Circle((x, y), 1.8, ec=COL[role], fc=COL[role] if full else FILL['encre'], lw=1.0, zorder=4))
text(ax, 44, 69, r'on remplace $x$ par 2', 'varie', 'm', weight='bold')
rows = [(48, r'$x > 2$', 'point vide', r'$2 > 2$ : faux', 'limite', False),
        (17, r'$x \geq 2$', 'point plein', r'$2 \geq 2$ : vrai', 'resultat', True)]
for y, form, nom, test, role, full in rows:
    f = numberline(ax, 8, 62, y, 0, 4, labels=False)
    line(ax, [(f(2), y), (67, y)], 'sujet', lw=2.2)
    dot(f(2), y, role, full)
    text(ax, f(2), y + 4.5, '2', 'encre', 's')
    text(ax, 2, y + 9, form, 'sujet', 'l', ha='left')
    text(ax, 86, y + 9, nom, role, 's', ha='right')
    arrow(ax, (f(2), y - 2.5), (f(2), y - 6.5), role, lw=1.0)
    box(ax, f(2) - 18, y - 15.5, 36, 8, role, label=test, size='m', lw=1.2)
save(fig, '17-018')
