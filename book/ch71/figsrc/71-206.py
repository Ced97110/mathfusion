import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
text(ax, 44, 70, 'restes non nuls', 'fixe', 's'); text(ax, 44, 4, 'carrés obtenus', 'resultat', 's')
X = lambda k: 14 + k * 20
for k, n in enumerate((1, 2, 3, 4)): box(ax, X(k) - 6, 52, 12, 12, 'sujet', label=str(n), size='l')
for k, n in enumerate((1, 2, 3, 4)):
    ok = n in (1, 4)
    box(ax, X(k) - 6, 12, 12, 12, 'resultat' if ok else 'limite', label=str(n), size='l', dash=not ok)
for a, b in ((0, 0), (1, 3), (2, 3), (3, 0)): arrow(ax, (X(a), 51), (X(b) + (a - b) * 0.0, 25.5), 'varie', lw=0.9)
text(ax, 44, 38, r'$1\to1,\ 2\to4,\ 3\to4,\ 4\to1$', 'varie', 's') if False else None
text(ax, 30, 31, r'$1^2=1$', 'varie', 's') if False else None
text(ax, 44, 44, 'au carré', 'varie', 's')
text(ax, X(1), 28, '', 'fixe', 's') if False else None
text(ax, 44, 30, 'jamais obtenus : 2 et 3', 'limite', 's') if False else None
text(ax, X(1) + 10, 8, '', 'fixe', 's') if False else None
save(fig, '71-206')
