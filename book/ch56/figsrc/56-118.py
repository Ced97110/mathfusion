import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
assert 3 * 0 ** 2 + 5 * 0 + 7 == 7
box(ax, 3, 56, 34, 10, 'sujet', label=r'$3x^2 + 5x + 7$', size='m')
arrow(ax, (37, 61), (54, 61), 'varie')
text(ax, 45.5, 66.5, r'$x \mapsto 0$', 'varie', 's')
box(ax, 54, 56, 30, 10, 'resultat', label='7', size='m')
text(ax, 69, 51, 'un entier de ℤ', 'resultat', 's')
text(ax, 22, 50, r'on retire $x(3x + 5)$', 'varie', 's')
box(ax, 4, 28, 80, 10, 'resultat', label='ℤ est intègre ⇒ (x) est premier', size='s')
box(ax, 4, 10, 80, 10, 'limite', label='2 sans inverse : (x) pas maximal', size='s')
save(fig, '56-118')
