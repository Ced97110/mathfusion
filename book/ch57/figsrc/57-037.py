import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 12, 60, r'$x$ et $y$', 'sujet', 's')
text(ax, 39, 60, r'$\eta(x+y)$', 'varie', 's')
text(ax, 72, 60, r'$\eta(x)+\eta(y)$', 'varie', 's')
rows = [('4 et 5', '3 × 9 = 27', '12 + 15 = 27'),
        ('2 et 7', '3 × 9 = 27', '6 + 21 = 27'),
        ('10 et −3', '3 × 7 = 21', '30 + (−9) = 21')]
for i, (a, b, c) in enumerate(rows):
    y = 40 - i * 17
    box(ax, 2, y, 20, 10, 'sujet', label=a, size='s')
    box(ax, 26, y, 26, 10, 'varie', label=b, size='s')
    text(ax, 55, y + 5, '=', 'resultat', 'l')
    box(ax, 58, y, 28, 10, 'varie', label=c, size='s')
save(fig, '57-037')
