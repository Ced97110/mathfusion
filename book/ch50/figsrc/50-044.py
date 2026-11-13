import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
box(ax, 2, 2, 84, 72, 'fixe', fill=False, dash=True)
text(ax, 44, 69, r'$G$ : 12 éléments', 'fixe', 'm')
box(ax, 6, 6, 76, 56, 'sujet')
text(ax, 44, 57, 'un 2-Sylow : 4 éléments', 'sujet', 'm')
box(ax, 9, 29, 70, 22, 'varie', fill=False, lw=1.1)
text(ax, 44, 47, 'sous-groupe : 2 éléments', 'varie', 's')
els = [(11, 31, 'e'), (47, 31, '(1 2)(3 4)'), (11, 12, '(1 3)(2 4)'), (47, 12, '(1 4)(2 3)')]
for x, y, lb in els:
    box(ax, x, y, 30, 8, 'sujet' if y < 20 else 'varie', label=lb, size='m')
save(fig, '50-044')
