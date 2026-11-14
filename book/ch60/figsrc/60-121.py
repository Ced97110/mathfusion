import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
xl, xr = 22, 66
text(ax, xl, 59, 'Horloge de 8 h', 'sujet', 'l', weight='bold')
text(ax, xr, 59, 'Horloge de 12 h', 'autre', 'l', weight='bold')
text(ax, xl, 51, r'$|G| = 8 = 2^3$', 'resultat', 'm')
text(ax, xr, 51, r'$|G| = 12$', 'limite', 'm')
text(ax, xr, 45, r'pas une puissance de 2', 'limite', 's')
text(ax, xl, 39, 'ordres des éléments', 'fixe', 's')
text(ax, xr, 39, 'ordres des éléments', 'fixe', 's')
# left: 4 boxes
bw, gap = 8, 1.5
x0 = xl - (4 * bw + 3 * gap) / 2
for i, v in enumerate([1, 2, 4, 8]):
    box(ax, x0 + i * (bw + gap), 25, bw, 9, 'resultat', label=str(v), size='m')
# right: 2 boxes
bw2 = 12
x1 = xr - (2 * bw2 + gap) / 2
for i, (v, who) in enumerate([(12, 'heure 1'), (3, 'heure 4')]):
    box(ax, x1 + i * (bw2 + gap), 25, bw2, 9, 'limite', label=str(v), size='m')
    text(ax, x1 + i * (bw2 + gap) + bw2 / 2, 20.5, who, 'fixe', 's')
text(ax, xl, 14, r'toutes des puissances de 2', 'resultat', 's')
text(ax, xr, 14, r'12 et 3 : pas des $2^k$', 'limite', 's')
text(ax, xl, 6, 'un 2-groupe', 'resultat', 'm', weight='bold')
text(ax, xr, 6, 'pas un 2-groupe', 'limite', 'm', weight='bold')
save(fig, '60-121')
