import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
rows = [[1], [2, 3, 5], [4, 6, 10, 15], [12, 20, 30], [60]]
ys = [10 + 13 * i for i in range(5)]
P = {}
for y, row in zip(ys, rows):
    for j, n in enumerate(row):
        P[n] = (44 + 16 * (j - (len(row) - 1) / 2), y)
fig, ax = canvas(70)
box(ax, 14, 3, 60, 61, 'fixe', fill=False, dash=True)
for p in P:
    for q in P:
        if q % p == 0 and q // p in (2, 3, 5):
            (x1, y1), (x2, y2) = P[p], P[q]
            d = math.hypot(x2 - x1, y2 - y1)
            ux, uy = (x2 - x1) / d, (y2 - y1) / d
            line(ax, [(x1 + ux * 3.6, y1 + uy * 3.6), (x2 - ux * 3.6, y2 - uy * 3.6)], 'fixe')
for n, (x, y) in P.items():
    disc(ax, x, y, 3.6, 'resultat' if n in (12, 60) else 'sujet', label=str(n), size='s')
text(ax, 8, ys[3], 'rang 3', 'resultat', 's')
text(ax, 8, ys[4], 'rang 4', 'resultat', 's')
save(fig, '79-205')
