import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(76)
box(ax, 24, 62, 40, 10, 'fixe', label='les entiers', size='m', weight='bold')
arrow(ax, (36, 62), (22, 55), 'fixe'); arrow(ax, (52, 62), (66, 55), 'fixe')
for x, role, title, sy, ex in [(2, 'sujet', 'avec l’addition', '+', [('3 + 4 = 7'), ('0 + 3 = 3')]),
                               (46, 'autre', 'avec la multiplication', '×', [('3 × 4 = 12'), ('0 × 3 = 0')])]:
    box(ax, x, 6, 40, 49, role)
    text(ax, x + 20, 48, title, role, 's', weight='bold')
    for k, e in enumerate(ex):
        box(ax, x + 4, 28 - k * 17 + 0, 32, 12, 'encre', label=e, size='m')
save(fig, '42-007')
