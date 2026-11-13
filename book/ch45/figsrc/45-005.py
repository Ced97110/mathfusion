import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

ROLES = ['fixe', 'sujet', 'varie', 'resultat']  # one colour per result 0..3
C = 8.0  # cell size

def table(ax, x0, y0, frame):
    """4x4 addition table mod 4: row a (top to bottom), column b, cell colour = (a+b) mod 4."""
    for a in range(4):
        for b in range(4):
            v = (a + b) % 4
            x, y = x0 + b * C, y0 + (3 - a) * C
            hit = (a, b) in ((1, 2), (3, 2))
            box(ax, x, y, C, C, ROLES[v], r=0.3, lw=0.5)
            if hit: ax.add_patch(Rectangle((x + 0.6, y + 0.6), C - 1.2, C - 1.2, ec=COL['encre'], fc='none', lw=1.6, zorder=4))
    ax.add_patch(Rectangle((x0, y0), 4 * C, 4 * C, ec=COL[frame], fc='none', lw=1.6, zorder=4))
    return lambda a, b: (x0 + b * C + C / 2, y0 + (3 - a) * C + C / 2)

fig, ax = canvas(80)
text(ax, 22, 74, 'horloge', 'sujet', 'm', weight='bold')
text(ax, 66, 74, 'rotations', 'autre', 'm', weight='bold')
fl = table(ax, 6, 30, 'sujet')
fr = table(ax, 50, 30, 'autre')
text(ax, 44, 46, '=', 'resultat', 'xl', weight='bold')
text(ax, 22, 66, 'ligne + colonne', 'encre', 's')
text(ax, 66, 66, 'ligne + colonne', 'encre', 's')
for i, v in enumerate(range(4)):
    x = 8 + i * 20
    box(ax, x, 14, 6, 6, ROLES[v], r=0.3)
    text(ax, x + 9, 17, '= %d' % v, ROLES[v] if ROLES[v] != 'fixe' else 'encre', 's')
text(ax, 44, 6, '16 cases : mêmes valeurs', 'resultat', 'm')
text(ax, 44, 24.5, 'contour noir : 1+2 et 3+2', 'encre', 's')
save(fig, '45-005')
