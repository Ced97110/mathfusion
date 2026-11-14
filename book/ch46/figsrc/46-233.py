import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
for y, n, f, h in [(58, 3, 6, 3), (36, 4, 24, 12), (14, 5, 120, 60)]:
    text(ax, 3, y + 5, f'$n={n}$', 'encre', 'm', ha='left')
    text(ax, 84, y + 13, f'${n}! = {f}$'.replace('120', '120'), 'encre', 'm', ha='right')
    box(ax, 18, y - 3, 33, 10, 'sujet', label=f'${h}$')
    box(ax, 51, y - 3, 33, 10, 'autre', label=f'${h}$')
text(ax, 18, 76, 'paires = moitié', 'sujet', 's', ha='left'); text(ax, 84, 76, 'impaires', 'autre', 's', ha='right')
save(fig, '46-233')
