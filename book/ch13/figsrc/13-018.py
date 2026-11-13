import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
rows = [('3', '$|3|$', '3'), (r'$-3$', r'$|-3|$', '3'), ('8', '$|8|$', '8')]
cx = (14, 44, 74)
for c, h in zip(cx, ('nombre', 'avec les barres', 'distance de 0')):
    text(ax, c, 56, h, 'fixe', 's')
for i, (a, b, c) in enumerate(rows):
    y = 38 - i * 15
    box(ax, cx[0] - 7, y - 5, 14, 10, 'fixe', label=a, size='l')
    box(ax, cx[1] - 8, y - 5, 16, 10, 'sujet', label=b, size='l')
    box(ax, cx[2] - 7, y - 5, 14, 10, 'resultat', label=c, size='l')
    arrow(ax, (cx[0] + 7.5, y), (cx[1] - 8.5, y), 'varie')
    arrow(ax, (cx[1] + 8.5, y), (cx[2] - 7.5, y), 'varie')
save(fig, '13-018')
