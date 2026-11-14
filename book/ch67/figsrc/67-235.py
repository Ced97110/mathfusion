import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
disc(ax, 11, 40, 9.5, 'varie', label='Frobenius', size='s')
rows = [(71, 'points fixes', 'corps finis'), (53, 'puissances', 'groupes de Galois'),
        (35, 'fixes des puissances', 'sous-corps'), (17, 'son image', r'réduction mod. $p$')]
line(ax, [(20.5, 40), (26, 40)], 'varie', lw=1.0)
line(ax, [(26, rows[-1][0]), (26, rows[0][0])], 'varie', lw=1.0)
for y, how, what in rows:
    arrow(ax, (26, y), (52.5, y), 'varie')
    text(ax, 39.3, y + 3.6, how, 'varie', 's')
    box(ax, 53, y - 5, 33, 10, 'sujet', label=what, size='s')
save(fig, '67-235')
