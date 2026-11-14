import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
X = lambda k: 12 + 13 * (k - 1)
y, r = 36, 4
for k in range(1, 7):
    disc(ax, X(k), y, r, 'sujet', label=str(k))
for k in range(1, 6):
    arrow(ax, (X(k) + r, y), (X(k + 1) - r, y), 'sujet')
arrow(ax, (X(6), y - r), (X(1), y - r), 'sujet', curve=-0.3)
for k in range(2, 7):
    arrow(ax, (X(1), y + r), (X(k), y + r), 'varie', curve=-0.3)
text(ax, 44, 60, '1 atteint toute racine', 'varie', 'm')
text(ax, 44, 17, 'cycle de longueur 6', 'sujet', 'm')
text(ax, 44, 8, r'transitif, donc $f$ irréductible', 'resultat', 'm')
save(fig, '67-210')
