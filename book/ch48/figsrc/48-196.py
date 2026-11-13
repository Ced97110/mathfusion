import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 44, 60, "sous-groupes de l'horloge 12", 'sujet', 'm')
text(ax, 44, 21, 'sous-groupes du quotient', 'autre', 'm')
xs = [20, 44, 68]
for x, a, b in zip(xs, [3, 6, 12], [1, 2, 4]):
    box(ax, x - 8, 45, 16, 8, 'sujet', label=str(a), weight='bold')
    box(ax, x - 8, 28, 16, 8, 'autre', label=str(b), weight='bold')
    arrow(ax, (x, 44.5), (x, 36.5), 'resultat', both=True)
for i in range(2):
    line(ax, [(xs[i] + 8, 49), (xs[i + 1] - 8, 49)], 'fixe')
    line(ax, [(xs[i] + 8, 32), (xs[i + 1] - 8, 32)], 'fixe')
text(ax, 44, 8, '3↔1, 6↔2, 12↔4 : un pour un', 'resultat', 's')
save(fig, '48-196')
