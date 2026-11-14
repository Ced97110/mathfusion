import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
X = lambda k: 28 + 11 * (k - 1)
r = 3.4
text(ax, 3, 86, r'racine $r_{k}$', 'encre', 'm', ha='left')
for k in range(1, 7):
    text(ax, X(k), 86, str(k), 'encre', 'm')
# ligne 1 : mod 2, un cycle de longueur 6
y = 70
for k in range(1, 7):
    disc(ax, X(k), y, r, 'sujet')
for k in range(1, 6):
    arrow(ax, (X(k) + r, y), (X(k + 1) - r, y), 'sujet')
arrow(ax, (X(6), y + r), (X(1), y + r), 'sujet', curve=0.25)
text(ax, 3, y + 3, 'mod 2', 'sujet', 'm', ha='left')
text(ax, 3, y - 3, 'cycle de 6', 'fixe', 's', ha='left')
# ligne 2 : mod 3, un point fixe et un cycle de longueur 5
y = 42
disc(ax, X(1), y, r, 'fixe')
for k in range(2, 7):
    disc(ax, X(k), y, r, 'varie')
for k in range(2, 6):
    arrow(ax, (X(k) + r, y), (X(k + 1) - r, y), 'varie')
arrow(ax, (X(6), y + r), (X(2), y + r), 'varie', curve=0.25)
text(ax, 3, y + 3, 'mod 3', 'varie', 'm', ha='left')
text(ax, 3, y - 3, 'cycles 1 et 5', 'fixe', 's', ha='left')
# ligne 3 : mod 5, un échange de deux racines
y = 14
for k in range(1, 7):
    disc(ax, X(k), y, r, 'resultat' if k < 3 else 'fixe')
arrow(ax, (X(1) + r, y), (X(2) - r, y), 'resultat', both=True)
text(ax, 3, y + 3, 'mod 5', 'resultat', 'm', ha='left')
text(ax, 3, y - 3, 'cycle de 2', 'fixe', 's', ha='left')
save(fig, '67-208')
