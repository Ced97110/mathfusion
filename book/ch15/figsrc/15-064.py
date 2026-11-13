import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
for y, t, l, n in [(48, r'$5x^3$', r'$x$', 3), (30, r'$21b^2$', r'$b$', 2), (12, r'$4x$', r'$x$', 1)]:
    box(ax, 3, y - 5.5, 24, 11, 'sujet', label=t, size='l')
    arrow(ax, (27.5, y), (31.5, y), 'fixe')
    for i in range(n): disc(ax, 36 + i * 10, y, 3.4, 'varie', label=l)
    arrow(ax, (36 + (n - 1) * 10 + 4.4, y), (65, y), 'fixe')
    box(ax, 66, y - 4.5, 19, 9, 'resultat', label=f'degré {n}')
save(fig, '15-064')
