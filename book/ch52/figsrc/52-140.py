import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 44, 65, r'chaque classe $\bar{n}$ et son carré', 'encre', 's')
X = lambda n: 12 + n * 12.8
sq = [(n * n) % 6 for n in range(6)]
for n in range(6):
    fixed = sq[n] == n
    disc(ax, X(n), 50, 4.5, 'resultat' if fixed else 'fixe', label=r'$\bar{%d}$' % n, size='s')
    disc(ax, X(n), 18, 4.5, 'resultat' if n in (0, 1, 3, 4) else 'fixe', label=r'$\bar{%d}$' % n, size='s')
for n in range(6):
    fixed = sq[n] == n
    if fixed:
        arrow(ax, (X(n), 45), (X(n), 23), 'resultat')
    else:
        arrow(ax, (X(n) + (0.8 if sq[n] > n else -0.8), 45), (X(sq[n]) + (-0.8 if sq[n] > n else 0.8), 23), 'limite')
text(ax, 4, 58, 'classe', 'fixe', 's', ha='left'); text(ax, 4, 10, 'son carré', 'fixe', 's', ha='left')
text(ax, 44, 4, 'vert : carré égal à la classe (0, 1, 3, 4)', 'resultat', 's')
save(fig, '52-140')
