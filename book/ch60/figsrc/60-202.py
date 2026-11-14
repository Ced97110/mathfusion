import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
s = 3; deg = [1, 1, 2]
text(ax, 44, 71, 's = 3, degrés 1, 1, 2', 'encre', 'm')
text(ax, 44, 64, 'coefficient 2s − 2j + 1', 'varie', 's')
tot = 0
for j in range(1, s + 1):
    coef = 2 * s - 2 * j + 1
    n = deg[j - 1]
    prod = coef * n
    tot += prod
    y = 52 - (j - 1) * 12
    text(ax, 2, y, f'j = {j} : {coef} × {n}', 'sujet', 's', ha='left')
    for k in range(prod):
        box(ax, 34 + k * 6, y - 2.5, 5.2, 5.2, 'sujet', r=0.3, lw=0.6)
    text(ax, 34 + 5 * 6 + 4, y, f'= {prod}', 'sujet', 's', ha='left')
assert tot == 10
text(ax, 44, 12, 'N = 5 + 3 + 2 = 10', 'resultat', 'l', weight='bold')
save(fig, '60-202')
