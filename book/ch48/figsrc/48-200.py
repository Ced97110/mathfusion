import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 44, 65, "sous-groupes de l'horloge 12", 'sujet', 'm')
text(ax, 44, 23, 'sous-groupes du quotient', 'autre', 'm')
xs = [18, 44, 70]
for x, a, b in zip(xs, [3, 6, 12], [1, 2, 4]):
    box(ax, x - 8, 48, 16, 8, 'sujet', label=str(a), weight='bold')
    box(ax, x - 8, 31, 16, 8, 'autre', label=str(b), weight='bold')
    arrow(ax, (x, 47.5), (x, 39.5), 'resultat')
for i in range(2):
    arrow(ax, (xs[i] + 8, 52), (xs[i + 1] - 8, 52), 'fixe', lw=0.7)
    arrow(ax, (xs[i] + 8, 35), (xs[i + 1] - 8, 35), 'fixe', lw=0.7)
text(ax, 44, 11, 'plus grand ici, plus grand là', 'resultat', 's')
text(ax, 44, 4, "l'ordre est gardé, non renversé", 'resultat', 's')
save(fig, '48-200')
