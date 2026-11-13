import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
text(ax, 44, 53, r'le petit $i$ dit la position', 'fixe', 's')
vals = ['2', '−1', '0', '3', '0']
for i, v in enumerate(vals):
    cx = 10.5 + 16 * i
    hi = i in (0, 3)
    box(ax, cx - 6.5, 33, 13, 12, 'varie' if hi else 'sujet', label=v)
    text(ax, cx, 28, rf'$a_{i}$', 'varie' if hi else 'sujet', 'm')
text(ax, 85, 39, '…', 'fixe', 'm')
arrow(ax, (10.5, 25), (20, 17), 'varie')
text(ax, 25, 13, r'$a_0$ = 2', 'varie', 'm')
arrow(ax, (58.5, 25), (58.5, 18), 'varie')
text(ax, 58.5, 13, r'$a_3$ = 3', 'varie', 'm')
save(fig, '54-086')
