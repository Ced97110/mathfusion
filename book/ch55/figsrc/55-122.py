import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
assert 2 ** 7 + 2 * 2 ** 2 == 136 == 27 * 5 + 1
assert 2 ** 3 + 2 * 2 ** 2 == 16 == 3 * 5 + 1
assert 136 - 16 == 120 == 2 ** 2 * (2 ** 5 - 2) == 4 * 30 and 30 % 5 == 0
text(ax, 44, 80, r'en $x=2$, sur $\mathbb{Z}/5\mathbb{Z}$', 'fixe', 'm')
# the two programs
box(ax, 3, 62, 39, 9, 'sujet', label=r'$f(2)=128+8=136$', size='s')
box(ax, 46, 62, 39, 9, 'autre', label=r'$f_0(2)=8+8=16$', size='s')
arrow(ax, (22.5, 62), (22.5, 56), 'varie')
arrow(ax, (65.5, 62), (65.5, 56), 'varie')
box(ax, 3, 47, 39, 9, 'sujet', label=r'$136=27\times5+1$', size='s')
box(ax, 46, 47, 39, 9, 'autre', label=r'$16=3\times5+1$', size='s')
arrow(ax, (22.5, 47), (40, 40.5), 'varie')
arrow(ax, (65.5, 47), (48, 40.5), 'varie')
box(ax, 24, 31, 40, 9, 'resultat', label='même reste : 1', size='m')
# why: the difference is a multiple of 5
box(ax, 4, 11, 80, 9, 'fixe', label=r'$136-16=120=2^2\,(2^5-2)=4\times30$', size='s')
text(ax, 44, 4, r'$30=2^5-2$ est un multiple de 5', 'varie', 's')
arrow(ax, (44, 31), (44, 21.5), 'varie')
save(fig, '55-122')
