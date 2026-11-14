import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
cols = [14, 44, 74]
for x, s, r in zip(cols, ['impair', 'impair', 'pair'], ['varie', 'varie', 'sujet']):
    text(ax, x, 51, s, r, 'm', weight='bold')
for y, trio in [(36, ('3', '5', '8')), (22, ('7', '9', '16'))]:
    for x, s, r in zip(cols, trio, ['varie', 'varie', 'sujet']):
        box(ax, x - 8, y, 16, 9, r, label=s, size='l')
    text(ax, 29, y + 4.5, '+', 'encre', 'l')
    text(ax, 59, y + 4.5, '=', 'encre', 'l')
box(ax, 20, 4, 48, 11, 'resultat', label='1 + 1 = 0', size='xl', weight='bold')
text(ax, 77, 9.5, 'impair = 1\npair = 0', 'fixe', 's')
save(fig, '68-024')
