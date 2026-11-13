import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
cols = [(14, 4, '(1 3 5 8)'), (36, 2, '(2 6)'), (56, 1, '(4)'), (74, 1, '(7)')]
for x, n, lab in cols:
    for j in range(n):
        disc(ax, x, 50 - 7 * j, 3.2, 'fixe' if j == 0 else 'varie')
    text(ax, x, 22, lab, 'sujet', 's')
text(ax, 44, 12, 'somme des longueurs = 8', 'fixe', 's')
text(ax, 44, 4.5, r'$N(\sigma)$ = 4 (sans les gris)', 'varie', 's')
save(fig, '46-205')
