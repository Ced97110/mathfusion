import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(82)
for r in range(4):
    from math import comb
    for k in range(r + 1):
        x = 44 + (k - r / 2) * 14
        y = 70 - r * 12
        last = r == 3
        text(ax, x, y, str(comb(r, k)), 'resultat' if last else 'fixe', 'l', weight='bold' if last else 'normal')
        if last:
            n = comb(r, k)
            for j in range(n):
                box(ax, x + (j - (n - 1) / 2) * 3.8 - 1.6, 25, 3.2, 3.2, 'sujet', r=0.2, lw=0.5)
text(ax, 44, 79, 'triangle de Pascal', 'fixe', 's')
text(ax, 44, 17, 'sacs de 0, 1, 2, 3 objets', 'sujet', 's')
save(fig, '42-016')
