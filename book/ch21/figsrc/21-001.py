import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
text(ax, 44, 53, 'route de 120 km', 'fixe', 'l')
for i, (v, t) in enumerate([(60, 2), (40, 3), (30, 4)]):
    y = 37 - i * 13
    box(ax, 2, y, 21, 9, 'varie', label=f'{v} km/h', size='s')
    box(ax, 25, y, 14 * t, 9, 'sujet', label=f'120 \u00f7 {v} = {t} h', size='s')
text(ax, 44, 5, 'vitesse plus basse : temps plus long', 'encre', 's')
save(fig, '21-001')
