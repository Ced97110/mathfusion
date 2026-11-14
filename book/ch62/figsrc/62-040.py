import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
text(ax, 44, 69, r'$F[x]/(f)$ avec $f=x^2-2$', 'encre', 'l')
rows = [(r'$x^2$', r'$2$'), (r'$x^3$', r'$2x$'), (r'$x^2+x$', r'$2+x$')]
text(ax, 20, 59, 'polynômes', 'fixe', 'm')
text(ax, 70, 59, 'restes', 'sujet', 'm')
for i, (a, b) in enumerate(rows):
    y = 40 - i * 15
    box(ax, 6, y, 28, 11, 'fixe', label=a)
    box(ax, 56, y, 28, 11, 'sujet', label=b)
    arrow(ax, (35, y + 5.5), (55, y + 5.5), 'varie')
    text(ax, 45, y + 9, 'reste', 'varie', 's')
text(ax, 44, 4, r'reste : degré $\leq 1$, forme $a+bx$', 'sujet', 's')
save(fig, '62-040')
