import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
X = lambda v: 44 + 11 * v
y = 36
numberline(ax, X(-3), X(3), y, -3, 3, labels=False)
disc(ax, X(-2), y, 1.4, 'sujet'); disc(ax, X(2), y, 1.4, 'autre'); disc(ax, X(0), y, 1.2, 'fixe')
text(ax, X(0), y + 4.5, r'$O$', 'fixe', 'm')
text(ax, 44, 56, 'coordonnée : étiquette du point', 'encre', 's', weight='bold')
text(ax, X(-2), y + 8, '−2', 'sujet', 'l', weight='bold'); text(ax, X(2), y + 8, '2', 'autre', 'l', weight='bold')
text(ax, X(-2), y + 14, 'à gauche de O', 'sujet', 's'); text(ax, X(2), y + 14, 'à droite de O', 'autre', 's')
text(ax, 44, 20, 'distance à O : sans côté', 'encre', 's', weight='bold')
arrow(ax, (X(0), 12), (X(-2) + 0.5, 12), 'fixe'); arrow(ax, (X(0), 12), (X(2) - 0.5, 12), 'fixe')
text(ax, X(-1), 6.5, 'distance 2', 'fixe', 's'); text(ax, X(1), 6.5, 'distance 2', 'fixe', 's')
save(fig, '12-059')
