import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
cs, x0, y0 = 13, 8, 14
for i in range(4):
    for j in range(3):
        box(ax, x0 + i * cs, y0 + j * cs, cs, cs, 'resultat' if (i < 3 and j < 2) else 'fixe', r=0.2)
brace(ax, x0, x0 + 3 * cs, y0, 'resultat', label=r'largeur $\frac{3}{4}$')
xr = x0 + 4 * cs + 3
line(ax, [(xr, y0), (xr, y0 + 2 * cs)], 'resultat')
line(ax, [(xr - 1, y0), (xr + 1, y0)], 'resultat'); line(ax, [(xr - 1, y0 + 2 * cs), (xr + 1, y0 + 2 * cs)], 'resultat')
text(ax, xr + 3, y0 + cs, r'hauteur $\frac{2}{3}$', 'resultat', 's', ha='left')
text(ax, x0 + 2 * cs, y0 + 3 * cs + 5, 'carré unité : 12 cases', 'sujet', 'm')
text(ax, 75, y0 + 3 * cs - 4, '6 cases', 'resultat', 'l', weight='bold')
text(ax, 75, y0 + 3 * cs - 10, 'sur 12', 'resultat', 'm')
save(fig, '06-049')
