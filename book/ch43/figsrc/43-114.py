import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
xs = lambda v: 10 + 9 * v
text(ax, 4, 60, 'ℕ', 'sujet', 'l', ha='left')
for n in range(4):
    disc(ax, 10 + 18 * n, 50, 3.6, 'sujet', label=str(n))
text(ax, 82, 50, '…', 'sujet', 'l')
for v in range(8):
    role = 'resultat' if v % 2 == 0 else 'fixe'
    disc(ax, xs(v), 22, 3.6, role, label=str(v))
text(ax, 85, 22, '…', 'fixe', 'l')
for n in range(4):
    arrow(ax, (10 + 18 * n, 46.2), (xs(2 * n), 25.8), 'varie')
text(ax, 38, 38, r'$n\mapsto 2n$', 'varie', 'm', ha='left')
text(ax, 4, 11, 'pairs : atteints', 'resultat', 's', ha='left')
text(ax, 84, 11, 'impairs : non', 'fixe', 's', ha='right')
save(fig, '43-114')
