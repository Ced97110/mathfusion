import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
x, y = 2, 3
e1, e2 = x + y, x * y
assert x ** 3 + y ** 3 == 35 == e1 ** 3 - 3 * e1 * e2 and e1 ** 3 == 125 and 3 * e1 * e2 == 90
box(ax, 8, 66, 72, 9, 'varie', label=r'$x=2,\ y=3$ : $e_1=5,\ e_2=6$', size='s')
arrow(ax, (24, 66), (22, 59.5), 'varie')
arrow(ax, (64, 66), (66, 59.5), 'varie')
box(ax, 3, 50, 38, 9, 'sujet', label=r'$x^3+y^3$', size='m')
box(ax, 47, 50, 38, 9, 'autre', label=r'$e_1^3-3e_1e_2$', size='m')
text(ax, 44, 54.5, '=', 'resultat', 'l', weight='bold')
arrow(ax, (22, 50), (22, 43.5), 'varie')
arrow(ax, (66, 50), (66, 43.5), 'varie')
box(ax, 3, 34, 38, 9, 'sujet', label=r'$8+27$', size='m')
box(ax, 47, 34, 38, 9, 'autre', label=r'$125-90$', size='m')
text(ax, 44, 38.5, '=', 'resultat', 'l', weight='bold')
arrow(ax, (22, 34), (36, 27.5), 'varie')
arrow(ax, (66, 34), (52, 27.5), 'varie')
box(ax, 24, 18, 40, 9, 'resultat', label='35 = 35', size='l')
text(ax, 44, 11, 'contrôle avec 2 et 3, pas une preuve', 'fixe', 's')
save(fig, '55-124')
