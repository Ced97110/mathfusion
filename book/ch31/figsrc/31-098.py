import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(54)
vals = [(60, '2', 2.0), (80, '5,76', 5.76), (85, '11,47', 11.47), (89, '57,30', 57.30)]
x0, k = 24, 0.9
text(ax, 44, 48, r'$\theta$ : longueur $OT$ = sec $\theta$', 'encre', 's')
line(ax, [(x0, 8), (x0, 42)], 'fixe')
for i, (a, s, v) in enumerate(vals):
    y = 37 - i * 9
    ax.add_patch(Rectangle((x0, y - 3), v * k, 6, ec=COL['varie'], fc=FILL['varie'], lw=0.8, zorder=2))
    text(ax, x0 - 2, y, f'{a}° : {s}', 'encre', 's', ha='right')
arrow(ax, (x0 + 57.3 * k + 1, 10), (86, 10), 'varie')
text(ax, 44, 4, r'$T$ monte sans limite', 'varie', 's', ha='center')
save(fig, '31-098')
