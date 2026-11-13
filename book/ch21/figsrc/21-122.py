import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
rows = [(r'$M\times\frac{3}{x}$', r'$3(x-1)$', r'$x$ se retire'),
        (r'$M\times\frac{4x}{x-1}$', r'$4x^2$', r'$x-1$ se retire'),
        (r'$M\times\frac{4x^2+x+5}{x^2-x}$', r'$4x^2+x+5$', 'tout le bas se retire')]
for i, (a, b, n) in enumerate(rows):
    y = 48 - i * 21
    box(ax, 2, y, 38, 14, 'sujet', label=a, size='s')
    arrow(ax, (41, y + 7), (58, y + 7), 'varie')
    text(ax, 49.5, y + 12, n, 'varie', 's')
    box(ax, 59, y, 27, 14, 'resultat', label=b, size='s')
save(fig, '21-122')
