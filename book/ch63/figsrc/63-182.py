import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
# le chapitre 63 au centre, deux chapitres en amont, trois en aval
cx, cy = 44, 42
disc(ax, cx, cy, 11, 'sujet', label=r'ch. 63', size='l')
left = [(8, 66, 'ch. 61', 'constructibilité'), (8, 18, 'ch. 62', 'corps de décomposition')]
right = [(80, 70, 'ch. 64', 'radicaux'), (80, 42, 'ch. 66', 'polygones'), (80, 14, 'ch. 67', 'corps finis')]
for x, y, n, t in left:
    box(ax, x - 6, y - 5, 24, 10, 'fixe', label=n, size='s')
    text(ax, x + 6, y - 9, t, 'fixe', 's')
    dx, dy = cx - 11 * 0.8 - (x + 18), cy - y
    arrow(ax, (x + 19, y), (cx - 9 if y < cy else cx - 8, cy + (3 if y > cy else -3)), 'fixe', lw=0.9)
for x, y, n, t in right:
    box(ax, x - 18, y - 5, 24, 10, 'autre', label=n, size='s')
    text(ax, x - 6, y - 9, t, 'autre', 's')
    arrow(ax, (cx + 10, cy + (y - cy) * 0.15), (x - 19, y), 'varie', lw=0.9)
save(fig, '63-182')
