import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
rows = [(r'$m=6$', r'$2^6+1=65$', '5', '13', r'$r=2$ : $2^2+1$'), (r'$m=3$', r'$2^3+1=9$', '3', '3', r'$r=1$ : $2^1+1$')]
for k, (m, val, f1, f2, tag) in enumerate(rows):
    y = 38 - k * 28
    box(ax, 2, y, 16, 10, 'fixe', label=m, size='s')
    arrow(ax, (18, y + 5), (24, y + 5), 'varie')
    box(ax, 24, y, 27, 10, 'limite', label=val, size='s')
    arrow(ax, (51, y + 5), (56, y + 5), 'varie')
    box(ax, 56, y, 10, 10, 'varie', label=f1, size='m')
    text(ax, 69, y + 5, r'$\times$', 'encre', 'm')
    box(ax, 72, y, 14, 10, 'fixe', label=f2, size='m')
    text(ax, 61, y - 4.5, tag, 'varie', 's')
text(ax, 44, 56, r'$m=q\times r$, $q$ impair', 'encre', 's')
save(fig, '66-067')
