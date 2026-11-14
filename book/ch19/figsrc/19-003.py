import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 57, r'$x$ : le nombre de cahiers', 'sujet', 'l')
for k, (y, n) in enumerate([(38, 1), (24, 4), (6, 10)]):
    for i in range(n): box(ax, 4 + i * 4.6, y, 4, 8, 'fixe', r=0.4)
    text(ax, 60, y + 4, r'$x$', 'sujet', 'l'); text(ax, 70, y + 4, f'= {n}', 'varie', 'l')
text(ax, 44, 16.5, 'même lettre, valeur changeante', 'fixe', 's')
save(fig, '19-003')
