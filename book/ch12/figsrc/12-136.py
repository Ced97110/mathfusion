import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
text(ax, 44, 67, r'$\dfrac{5}{x-3}$', 'sujet', 'xl')
for cx, s in [(16, r'$x$'), (44, r'$x-3$'), (72, 'fraction')]: text(ax, cx, 52, s, 'varie' if cx == 16 else 'fixe' if cx == 44 else 'sujet', 'm')
rows = [('4', '1', '5', 'resultat'), ('5', '2', '2,5', 'resultat'), ('3', '0', 'interdit', 'limite')]
for i, (a, b, c, r) in enumerate(rows):
    y = 40 - i * 13
    box(ax, 2, y - 5, 84, 10, r)
    text(ax, 16, y, a, 'varie', 'm'); text(ax, 44, y, b, 'encre', 'm'); text(ax, 72, y, c, r, 'm', weight='bold' if r == 'limite' else 'normal')
save(fig, '12-136')
