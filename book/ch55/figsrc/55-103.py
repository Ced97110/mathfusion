import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 55, r'$x^2-5x+6=(x-2)(x-3)$', 'encre', 'l')
rows = [(30, r'$b_1=-5$', r'$(-1)^1=-1$', r'$e_1=2+3$'),
        (10, r'$b_2=6$', r'$(-1)^2=1$', r'$e_2=2\times 3$')]
for y, b, s, e in rows:
    box(ax, 2, y, 22, 12, 'sujet', label=b, weight='bold')
    text(ax, 27, y + 6, '=', 'encre', 'l')
    box(ax, 31, y, 24, 12, 'fixe', label=s, size='s')
    text(ax, 58, y + 6, r'$\times$', 'encre', 'l')
    box(ax, 62, y, 24, 12, 'autre', label=e, size='s')
text(ax, 13, 46, 'coefficient', 'sujet', 's')
text(ax, 43, 46, 'signe', 'fixe', 's')
text(ax, 74, 46, 'racines', 'autre', 's')
save(fig, '55-103')
