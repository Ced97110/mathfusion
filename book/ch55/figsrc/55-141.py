import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
# Z/3Z : x^3 - x = x (x - 1)(x - 2) ; roots 0, 1, 2 = all the elements
assert all((v ** 3 - v) % 3 == 0 for v in range(3))
text(ax, 44, 66, r'sur $\mathbb{Z}/3\mathbb{Z}$ : $x^3-x=x\,(x-1)(x-2)$', 'sujet', 's')
labs = [r'$x$', r'$x-1$', r'$x-2$']
for k, lab in enumerate(labs):
    cx = 16 + k * 28
    box(ax, cx - 11, 46, 22, 9, 'sujet', label=lab, size='m')
    arrow(ax, (cx, 46), (cx, 37.5), 'varie')
    disc(ax, cx, 33, 4, 'resultat', label=str(k), size='m')
brace(ax, 5, 83, 27, 'resultat', label='ses 3 racines : 0, 1, 2', size='s')
box(ax, 8, 4, 72, 9, 'fixe', label=r'ce sont tous les éléments de $\mathbb{Z}/3\mathbb{Z}$', size='s')
save(fig, '55-141')
