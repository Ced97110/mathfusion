import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
eq = lambda v: -3 * v[0] + v[1] + v[2]
a, b = (1, 2, 1), (0, 1, -1)
assert eq(a) == 0 and eq(b) == 0
text(ax, 44, 65, r'on remplace $x,y,z$ dans $-3x+y+z$', 'fixe', 's')
box(ax, 2, 48, 26, 9, 'sujet', label=r'$a=(1,2,1)$')
arrow(ax, (30, 52.5), (36, 52.5), 'varie')
box(ax, 38, 48, 48, 9, 'varie', label=r'$-3\times1+2+1=0$')
box(ax, 2, 33, 26, 9, 'autre', label=r'$b=(0,1,-1)$')
arrow(ax, (30, 37.5), (36, 37.5), 'varie')
box(ax, 38, 33, 48, 9, 'varie', label=r'$-3\times0+1+(-1)=0$')
text(ax, 44, 24, r'$x_1a+x_2b$ se calcule avec les mêmes', 'resultat', 's')
text(ax, 44, 20, 'opérations : multiplier, additionner', 'resultat', 's')
box(ax, 14, 4, 60, 10, 'resultat', label=r'$x_1a+x_2b$ donne aussi $0$')
save(fig, '58-130')
