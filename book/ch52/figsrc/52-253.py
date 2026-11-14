import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 44, 76, 'quatre processeurs séparés', 'fixe', 's')
for i, (m, s) in enumerate([(95, '44 × 11 = 9'), (97, '0 × 76 = 0'), (98, '76 × 61 = 30'), (99, '55 × 46 = 55')]):
    x = 2 + i * 21.7
    box(ax, x, 60, 19.5, 9, 'sujet', label=str(m), weight='bold')
    arrow(ax, (x + 9.75, 60), (x + 9.75, 52), 'varie')
    box(ax, x, 42, 19.5, 10, 'varie', label=s, size='s')
    arrow(ax, (x + 9.75, 42), (44 + (x + 9.75 - 44) * 0.5, 19), 'varie')
box(ax, 24, 8, 40, 11, 'resultat', label='3 267 154', size='l')
text(ax, 2, 13, 'recollage', 'resultat', 's', ha='left')
save(fig, '52-253')
