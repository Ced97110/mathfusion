import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
xs = [3, 33, 63]
for x, h in zip(xs, ['fraction', 'décimal', 'pourcentage']):
    text(ax, x + 11, 57, h, 'fixe', 's')
rows = [(38, [r'$\frac{3}{5}$', '0,6', '60 %'], 'resultat', 'se termine'), (14, [r'$\frac{1}{3}$', '0,333…', '33,333… %'], 'limite', 'ne se termine pas')]
for y, labs, role, note in rows:
    for i, (x, l) in enumerate(zip(xs, labs)):
        box(ax, x, y, 22, 12, 'sujet' if i == 0 else role, label=l, size='m')
        if i < 2: arrow(ax, (x + 23, y + 6), (xs[i + 1] - 1, y + 6), 'varie')
    text(ax, 44, y - 4.5, note, role, 's')
save(fig, '09-074')
