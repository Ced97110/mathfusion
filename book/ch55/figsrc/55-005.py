import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
box(ax, 4, 73, 80, 15, 'sujet', label=r'$x^3-x$ : liste $0,-1,0,1$' + '\nelle n’est pas nulle', size='s')
text(ax, 13, 67, 'nombre', 'fixe', 's')
text(ax, 43, 67, r'$x^3-x$', 'fixe', 's')
text(ax, 76, 67, r'dans $\mathbb{Z}/3\mathbb{Z}$', 'fixe', 's')
rows = [(56, '0', r'$0-0=0$', '0'), (40, '1', r'$1-1=0$', '0'), (24, '2', r'$8-2=6$', r'$6\to0$')]
for y, n, calc, res in rows:
    box(ax, 4, y - 5.5, 16, 11, 'fixe', label=n)
    arrow(ax, (20, y), (28, y), 'varie')
    box(ax, 28, y - 5.5, 30, 11, 'sujet', label=calc, size='s')
    arrow(ax, (58, y), (66, y), 'varie')
    box(ax, 66, y - 5.5, 20, 11, 'resultat', label=res, size='s')
box(ax, 4, 2, 80, 13, 'resultat', label='tableau 0, 0, 0\nidentique à la fonction nulle', size='s')
save(fig, '55-005')
