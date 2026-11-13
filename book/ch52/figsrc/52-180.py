import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 22, 61, 'premiers entre eux', 'resultat', 's')
text(ax, 66, 61, 'pas premiers entre eux', 'limite', 's')
for x, a, b, d, last, role in ((6, '(4) + (9)', 'PGCD = 1', '= ℤ tout entier', '', 'resultat'), (50, '(4) + (6)', 'PGCD = 2', r'= (2) $\neq$ ℤ', '', 'limite')):
    box(ax, x, 46, 32, 9, 'sujet' if x < 40 else 'autre', label=a)
    box(ax, x, 28, 32, 9, 'fixe', label=b)
    box(ax, x, 10, 32, 9, role, label=d)
    arrow(ax, (x + 16, 46), (x + 16, 37.5), 'varie')
    arrow(ax, (x + 16, 28), (x + 16, 19.5), 'varie')
save(fig, '52-180')
