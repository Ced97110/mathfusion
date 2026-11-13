import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
x0, y0, L = 4, 42, 62
rise = L * 0.1
line(ax, [(x0, y0), (x0 + L, y0)], 'fixe', lw=1.4)
line(ax, [(x0 + L, y0), (x0 + L, y0 + rise)], 'varie', lw=1.8)
line(ax, [(x0, y0), (x0 + L, y0 + rise)], 'sujet', lw=1.4)
text(ax, x0 + L / 2, y0 - 3.5, 'avancée 100 m', 'fixe', 's')
text(ax, x0 + L + 2, y0 + rise / 2, 'montée 10 m', 'varie', 's', ha='left')
box(ax, 2, 14, 22, 11, 'sujet', label='pente 0,1', size='m')
box(ax, 34, 14, 22, 11, 'fixe', label='× 100', size='m')
box(ax, 64, 14, 22, 11, 'resultat', label='10 %', size='l', weight='bold')
arrow(ax, (24.8, 19.5), (33.2, 19.5), 'varie'); arrow(ax, (56.8, 19.5), (63.2, 19.5), 'varie')
text(ax, 44, 7, 'angle ≈ 5,71° : arctan(0,1)', 'fixe', 's')
save(fig, '26-087')
