import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
# three exponents
for cx, s in zip((16, 44, 72), ('a', 'b', 'c')):
    v = {'a': 2, 'b': 2, 'c': 1}[s]
    box(ax, cx - 10, 68, 20, 10, 'sujet', label=rf'${s}_i = {v}$')
# left branch
box(ax, 3, 44, 34, 10, 'varie', label=r'$\max(b_i, c_i) = 2$', size='s')
box(ax, 3, 20, 34, 10, 'resultat', label=r'$\min(a_i, 2) = 2$', size='s')
arrow(ax, (16, 68), (16, 54)); arrow(ax, (44, 68), (30, 54)); arrow(ax, (20, 44), (20, 30))
# right branch
box(ax, 42, 44, 22, 10, 'varie', label=r'$\min(a_i, b_i) = 2$', size='s')
box(ax, 66, 44, 20, 10, 'varie', label=r'$\min(a_i, c_i) = 1$', size='s')
box(ax, 50, 20, 34, 10, 'resultat', label=r'$\max(2, 1) = 2$', size='s')
arrow(ax, (16, 68), (50, 54)); arrow(ax, (44, 68), (52, 54)); arrow(ax, (72, 68), (76, 54))
arrow(ax, (53, 44), (60, 30)); arrow(ax, (76, 44), (74, 30))
text(ax, 20, 12, 'côté gauche', 'fixe', 's'); text(ax, 67, 12, 'côté droit', 'fixe', 's')
text(ax, 43.5, 25, r'$=$', 'resultat', 'l')
save(fig, '79-145')
