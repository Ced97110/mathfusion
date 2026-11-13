import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 22, 58, 'pour tout', 'sujet', 'l', weight='bold'); text(ax, 66, 58, 'il existe', 'varie', 'l', weight='bold')
for i, v in enumerate([2, 4, 6, 8]):
    y = 46 - i * 9
    disc(ax, 22, y, 3.6, 'sujet', label=str(v), size='s')
    disc(ax, 66, y, 3.6, 'varie' if v == 4 else 'fixe', fill=(v == 4), label=str(v), size='s')
box(ax, 8, 3, 28, 8, 'sujet', fill=False, label='tous les objets', size='s')
box(ax, 52, 3, 28, 8, 'varie', fill=False, label='au moins un', size='s')
save(fig, '42-088')
