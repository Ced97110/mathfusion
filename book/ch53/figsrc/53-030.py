import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
box(ax, 14, 62, 60, 12, 'fixe', label='famille : décaler de ? crans')
keys = [(2, 'clé 3', 'aujourd’hui', 'décale de 3'), (46, 'clé 5', 'demain', 'décale de 5')]
for x, k, d, f in keys:
    cx = x + 20
    arrow(ax, (44 + (cx - 44) * 0.5, 62), (cx, 51), 'fixe')
    box(ax, x, 40, 40, 10, 'varie', label=k, weight='bold')
    text(ax, cx, 35, d, 'varie', 's')
    arrow(ax, (cx, 32), (cx, 24), 'sujet')
    box(ax, x, 12, 40, 11, 'sujet', label=f)
text(ax, 44, 4, 'seul le nombre change', 'fixe', 's')
save(fig, '53-030')
