import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
u = 3.2
text(ax, 14, 68, 'côté', 'sujet', 's'); text(ax, 70, 68, 'aire', 'resultat', 's')
for n, y in ((3, 40), (5, 8)):
    ax.plot([6, 6 + n*u], [y + 8, y + 8], color=COL['sujet'], lw=2.2, solid_capstyle='butt', zorder=3)
    text(ax, 6 + n*u/2, y + 12, str(n), 'sujet', 'm')
    poly(ax, [(58, y), (58+n*u, y), (58+n*u, y+n*u), (58, y+n*u)], 'resultat')
    text(ax, 58 + n*u/2, y + n*u/2, str(n*n), 'resultat', 'm')
    arrow(ax, (26, y + 11), (54, y + 11), 'varie')
    arrow(ax, (54, y + 5), (26, y + 5), 'autre')
    text(ax, 40, y + 15, 'au carré', 'varie', 's')
    text(ax, 40, y + 1, 'racine', 'autre', 's')
save(fig, '22-010')
