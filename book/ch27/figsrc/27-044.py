import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
text(ax, 20, 50, 'droite du sol', 'fixe', 's'); text(ax, 45, 50, 'distance de G', 'fixe', 's'); text(ax, 78, 50, 'angle', 'fixe', 's')
rows = [('AC (projeté)', 2.0, '2 m', '21,80°', 'resultat'), ('AB', 3.606, '3,606 m', '42,03°', 'varie'), ('AD', 4.472, '4,472 m', '56,15°', 'varie')]
k = 10.0
for i, (n, d, ds, an, r) in enumerate(rows):
    y = 40 - i * 12.5
    text(ax, 2, y, n, r, 's', ha='left')
    box(ax, 26, y - 4, d * k, 8, r, label=ds, size='s')
    text(ax, 84, y, an, r, 's', ha='right')
text(ax, 44, 4.5, 'plus court : plus petit angle', 'resultat', 's')
save(fig, '27-044')
