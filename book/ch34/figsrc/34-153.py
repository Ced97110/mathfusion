import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
x0, y0, L = 22, 34, 50
a = 0.866 * L; b = 0.5 * L
poly(ax, [(x0, y0), (x0 + a, y0), (x0, y0 + b)], 'fixe')
line(ax, [(x0, y0), (x0 + a, y0)], 'autre', lw=1.6); line(ax, [(x0, y0), (x0, y0 + b)], 'sujet', lw=1.6)
line(ax, [(x0 + 2, y0), (x0 + 2, y0 + 2), (x0, y0 + 2)], 'fixe', lw=0.6)
text(ax, x0 + a - 9, y0 + 2.5, '30°', 'sujet', 's'); text(ax, x0 + 2, y0 + b - 8, '60°', 'autre', 's', ha='left')
text(ax, x0 - 2, y0 + b / 2, '0,5', 'sujet', 'm', ha='right')
text(ax, x0 + a / 2, y0 - 3.5, '0,866', 'autre', 'm')
text(ax, 44, 20, 'sin 30° = cos 60° = 0,5', 'sujet', 'm')
text(ax, 44, 12, 'sin 60° = cos 30° = 0,866', 'autre', 'm')
text(ax, 44, 4, '30° + 60° = 90°', 'varie', 'm')
save(fig, '34-153')
