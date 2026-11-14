import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 61, r'on cherche $x$ tel que $0\cdot x=1$', 'sujet', 'm')
for i, (v, lab) in enumerate([('5', r'$0\cdot5$'), ('100', r'$0\cdot100$'), ('1/2', r'$0\cdot\frac{1}{2}$')]):
    y = 38 - i * 15
    box(ax, 6, y, 30, 11, 'sujet', label=lab, size='m')
    arrow(ax, (37, y + 5.5), (47, y + 5.5), 'varie')
    box(ax, 48, y, 10, 11, 'fixe', label='0', size='l')
    box(ax, 66, y, 16, 11, 'limite', label=r'$\neq1$', size='l')
text(ax, 62, 56 - 0, '', 'fixe', 's')
text(ax, 44, 4, 'toujours 0, jamais 1', 'limite', 'm')
save(fig, '12-121')
