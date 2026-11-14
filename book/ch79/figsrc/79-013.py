import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
rows = [('5', [('5', 'autre')], 1), ('4', [('2', 'sujet'), ('2', 'sujet')], 2), ('12', [('2', 'sujet'), ('2', 'sujet'), ('3', 'varie')], 3),
        ('60', [('2', 'sujet'), ('2', 'sujet'), ('3', 'varie'), ('5', 'autre')], 4)]
for i, (n, fs, e) in enumerate(rows):
    y = 8 + i * 15
    text(ax, 3, y + 4, f'{n} : étage {e}', 'resultat', 'm', ha='left')
    for j, (v, c) in enumerate(fs): box(ax, 46 + j * 10, y, 9, 8, c, label=v)
save(fig, '79-013')
