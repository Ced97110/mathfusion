import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
items = [('sujet', r'$f(1) = a$'), ('varie', r'dans $\mathbb{Z}/7\mathbb{Z}$ : $7 \times 1 = 0$'),
         ('varie', r'donc $7a = 0$ dans $\mathbb{Z}/12\mathbb{Z}$'),
         ('autre', r'$7 \times 7 = 49$, qui vaut 1'), ('resultat', r'donc $a = 0$ : $f$ est triviale')]
y = 76
for k, (r, t) in enumerate(items):
    box(ax, 6, y, 76, 9.5, r, label=t, size='m')
    if k < len(items) - 1: arrow(ax, (44, y), (44, y - 5), 'fixe')
    y -= 15
text(ax, 44, 4, r'$7a \times 7 = 49a = a$', 'autre', 's') if False else None
save(fig, '48-165')
