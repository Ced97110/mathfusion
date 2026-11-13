import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(82)
cols = [44, 70]; rows = [60, 36, 12]; rl = ['de 360° à 720°', 'de 0° à 360°', 'de −360° à 0°']
vals = [['390°', '510°'], ['30°', '150°'], ['−330°', '−210°']]
rr = ['resultat', 'sujet', 'resultat']
for y, lb, vs, r in zip(rows, rl, vals, rr):
    text(ax, 2, y + 6, lb, 'fixe', 's', ha='left')
    for c, v in zip(cols, vs): box(ax, c - 11, y, 22, 12, r, label=v, size='m')
for c in cols:
    arrow(ax, (c, 48.5), (c, 59.5), 'varie'); arrow(ax, (c, 35.5), (c, 24.5), 'varie')
text(ax, 51, 54, '+ 360°', 'varie', 's'); text(ax, 51, 30, '− 360°', 'varie', 's')
save(fig, '32-024')
