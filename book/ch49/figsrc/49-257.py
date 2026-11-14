import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
order = [1, 3, 2, 5, 4]
X = [20 + 12 * i for i in range(5)]
for n, x in zip(order, X): text(ax, x, 80, str(n), 'encre', 'l')
# rows: label, set of fixed points, swapped pairs (as positions), count
rows = [('(1)', [], '5'), ('(1 3)', [(0, 1)], '3'), ('(1 3)(2 5)', [(0, 1), (2, 3)], '1'), ('(2 5)', [(2, 3)], '3')]
for r, (lab, pairs, c) in enumerate(rows):
    y = 68 - 11 * r
    moved = {i for p in pairs for i in p}
    text(ax, 2, y, lab, 'encre', 's', ha='left')
    for i, x in enumerate(X):
        disc(ax, x, y, 2.2, 'varie' if i in moved else 'resultat')
    for i, j in pairs:
        arrow(ax, (X[i] + 2.6, y + 1.2), (X[j] - 2.6, y + 1.2), 'varie', lw=0.8, curve=-0.0, both=True)
    text(ax, 84, y, c + (' fixe' if c == '1' else ' fixes'), 'resultat', 's', ha='right')
# orbits
yo = 18
groups = [(0, 1), (2, 3), (4, 4)]
for a, b in groups:
    box(ax, X[a] - 4.5, yo - 4.5, X[b] - X[a] + 9, 9, 'autre', fill=False, dash=True)
    for i in range(a, b + 1): disc(ax, X[i], yo, 2.2, 'autre')
text(ax, 44, 6, r'$(5+3+1+3)\div4=3$ orbites', 'autre', 'm')
save(fig, '49-257')
