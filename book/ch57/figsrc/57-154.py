import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
X = lambda n: 8 + (n - 1) * 9.0
for n in range(1, 10):
    reached = n % 3 == 0
    disc(ax, X(n), 12, 3.2, 'resultat' if reached else 'fixe', label=str(n), size='s')
for k in (1, 2, 3):
    disc(ax, X(k) + 0.0, 50, 3.2, 'sujet', label=str(k), size='s')
    arrow(ax, (X(k), 46.6), (X(3 * k), 15.6), 'varie', lw=1.0)
text(ax, 80, 56, 'départ', 'encre', 'm', ha='right', weight='bold')
text(ax, 80, 4, 'arrivée', 'encre', 'm', ha='right', weight='bold')
text(ax, 20, 30, 'tripler', 'varie', 'm')
text(ax, X(6), 3.5, 'vert : atteints', 'resultat', 's')
text(ax, X(2) + 3, 3.5, 'gris : jamais atteints', 'fixe', 's')
save(fig, '57-154')
