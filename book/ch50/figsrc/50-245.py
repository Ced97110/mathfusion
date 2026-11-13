import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
for i, (n, r) in enumerate([('12', 'sujet'), ('30', 'sujet'), (r'60 = $A_5$', 'limite')]):
    x = 3 + 28 * i
    box(ax, x, 18, 26, 32, r); text(ax, x + 13, 56, n, r, 'm', weight='bold')
    if i < 2:
        box(ax, x + 5, 25, 16, 18, 'resultat', label='normal', size='s')
        text(ax, x + 13, 11, 'résoluble', 'resultat', 's')
    else:
        box(ax, x + 5, 25, 16, 18, 'limite', fill=False, dash=True, label='aucun', size='s')
        text(ax, x + 13, 11, 'non résoluble', 'limite', 's')
save(fig, '50-245')
