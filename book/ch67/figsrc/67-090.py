import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
# squaring in the field with 4 elements : 0 -> 0, 1 -> 1, alpha -> alpha + 1, alpha + 1 -> alpha
text(ax, 44, 70, r'Frobenius : $x \mapsto x^2$', 'sujet', 'm')
text(ax, 44, 60, '0 et 1 restent en place', 'fixe', 's')
L = ['0', '1', r'$\alpha$', r'$\alpha+1$']
ys = [44, 31, 18, 5]
for k in range(4):
    box(ax, 3, ys[k], 20, 9, 'sujet', label=L[k])
    box(ax, 65, ys[k], 20, 9, 'resultat', label=L[k])
for k in (0, 1):
    arrow(ax, (24, ys[k] + 4.5), (64, ys[k] + 4.5), 'fixe')
arrow(ax, (24, ys[2] + 4.5), (64, ys[3] + 4.5), 'varie')
arrow(ax, (24, ys[3] + 4.5), (64, ys[2] + 4.5), 'varie')
save(fig, '67-090')
