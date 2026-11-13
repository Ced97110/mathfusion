import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
text(ax, 38, 58, '−', 'varie', 28, weight='bold'); text(ax, 50, 58, r'$a$', 'fixe', 28)
text(ax, 30, 45, 'opposé de', 'varie', 'm'); text(ax, 58, 45, 'le nombre', 'fixe', 'm')
arrow(ax, (33, 48), (37, 52), 'varie'); arrow(ax, (56, 48), (51, 52), 'fixe')
for y, a, b in [(31, '3', '−3'), (14, '−3', '3')]:
    box(ax, 8, y - 4.5, 26, 9, 'fixe', label=r'$a$ = ' + a)
    arrow(ax, (37, y), (51, y), 'varie')
    box(ax, 54, y - 4.5, 26, 9, 'sujet', label=r'$-a$ = ' + b)
save(fig, '12-107')
