import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Rectangle
fig, ax = canvas(84)
text(ax, 44, 79, r'$x^2+4y^2-z^2$', 'encre', 'm')
by, u = 36, 3.5  # ligne de base, mm par unité de coefficient
line(ax, [(8, by), (82, by)], 'fixe', lw=0.7)
terms = [(20, 1, r'$x^2$', 'sujet'), (44, 4, r'$4y^2$', 'sujet'), (68, -1, r'$-z^2$', 'autre')]
for cx, c, lab, role in terms:
    h = c * u
    ax.add_patch(Rectangle((cx - 7, by if h > 0 else by + h), 14, abs(h), ec=COL[role], fc=FILL[role], lw=0.8, zorder=2))
    text(ax, cx, 24, lab, role, 'm')
brace(ax, 13, 51, 58, 'sujet', label='2 positifs', down=False)
brace(ax, 61, 75, 58, 'autre', label='1 négatif', down=False)
box(ax, 14, 5, 60, 10, 'resultat', label='2 positifs, 1 négatif', size='s')
save(fig, '69-139')
