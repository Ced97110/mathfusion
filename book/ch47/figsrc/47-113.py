import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
R = ['sujet', 'varie', 'resultat']
text(ax, 44, 77, 'les entiers', 'fixe', 's')
for i in range(6):
    disc(ax, 10 + 13 * i, 68, 4.5, R[i % 3], label=str(i))
arrow(ax, (44, 61), (44, 50), 'fixe')
text(ax, 48, 55.5, 'modulo 3 : m = 3 classes', 'encre', 's', ha='left')
for k in range(3):
    box(ax, 4 + 28 * k, 34, 24, 12, R[k], label=r'$\bar{%d}$' % k, size='l')
box(ax, 20, 4, 48, 11, 'resultat', label=r'$\bar{1}+\bar{2}=\bar{0}$', size='m')
arrow(ax, (44, 33.5), (40, 15.5), 'varie')
arrow(ax, (72, 33.5), (60, 15.5), 'varie')
save(fig, '47-113')
