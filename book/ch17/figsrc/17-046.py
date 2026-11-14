import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def dot(ax, x, y, role, full=True, r=1.7):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role] if full else FILL['encre'], lw=1.0, zorder=4))

fig, ax = canvas(76)
text(ax, 54, 71, r'$a$ est-il solution ?', 'encre', 'm')
text(ax, 11, 62, 'côté ?', 'encre', 's')
text(ax, 38, 62, 'oui : point plein', 'sujet', 's'); text(ax, 70, 62, 'non : point vide', 'sujet', 's')
for r, (yb, side, rl) in enumerate(((32, 1, 'à droite'), (6, -1, 'à gauche'))):
    text(ax, 2, yb + 11, rl, 'encre', 's', ha='left')
    for c, full in enumerate((True, False)):
        xc = 38 + 32 * c
        box(ax, xc - 15, yb, 30, 22, 'fixe')
        ym = yb + 8; xe = xc + side * 12
        arrow(ax, (xc, ym), (xe, ym), 'sujet', lw=1.8); dot(ax, xc, ym, 'sujet', full=full)
        sym = ('>', r'\geq') if side == 1 else ('<', r'\leq')
        text(ax, xc, yb + 17, r'$x' + (sym[1] if full else sym[0]) + r' a$', 'sujet', 'm')
save(fig, '17-046')
