import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(46)
text(ax, 44, 42, r'cases d’un tableau $n \times n$', 'sujet', 'm', weight='bold')
x = 6
for n in (2, 3, 4):
    c = 5
    for i in range(n):
        for j in range(n): box(ax, x + j * c, 14 + i * c, c, c, 'sujet', r=0.3, lw=0.5)
    text(ax, x + n * c / 2, 9, rf'$n={n}$', 'fixe', 's')
    text(ax, x + n * c / 2, 4, rf'${n}^2 = {n*n}$', 'sujet', 'm', weight='bold')
    x += n * c + 8
save(fig, '76-026')
