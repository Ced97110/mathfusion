import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(56)
n = 7
V = [(6 + i * 76 / (n - 1), 16 if i % 2 == 0 else 46) for i in range(n)]
for i in range(5):
    a, b, c = V[i], V[i + 1], V[i + 2]
    poly(ax, [a, b, c], 'sujet')
    line(ax, [a, b, c, a], 'sujet', 0.9)
    text(ax, (a[0] + b[0] + c[0]) / 3, (a[1] + b[1] + c[1]) / 3, str(i + 1), 'sujet', 'm', weight='bold')
for i in range(1, 5):                      # côtés communs, déjà calculés
    line(ax, [V[i], V[i + 1]], 'varie', 1.8)
line(ax, [V[0], V[1]], 'encre', 2.6)       # base, mesurée au ruban
line(ax, [V[5], V[6]], 'resultat', 2.6)    # contrôle, mesuré une seconde fois
text(ax, 12.5, 38, 'base', 'encre', 's', ha='right', weight='bold')
text(ax, 77, 38, 'contrôle', 'resultat', 's', ha='left', weight='bold')
arrow(ax, (10, 8), (78, 8), 'varie')
text(ax, 44, 2.5, 'chaque triangle s’appuie sur un côté commun', 'varie', 's')
save(fig, '38-058')
