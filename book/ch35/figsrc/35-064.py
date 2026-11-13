import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(52)
cols = [14, 32, 50, 68]
text(ax, cols[1], 47, 'premier angle', 'sujet', 's'); text(ax, cols[3], 47, 'second angle', 'fixe', 's')
rows = [(36, 'P', 'Q'), (22, '75°', '15°'), (8, '50°', '10°')]
for k, (y, p, q) in enumerate(rows):
    text(ax, cols[0], y, 'sin', 'encre', 'm')
    box(ax, cols[1] - 8, y - 5, 16, 10, 'sujet', label=p, size='m')
    text(ax, cols[2], y, '+ sin', 'encre', 'm')
    box(ax, cols[3] - 8, y - 5, 16, 10, 'fixe', label=q, size='m')
    if k < 2: arrow(ax, (cols[1], y - 5.5), (cols[1], y - 8.5), 'varie', lw=1.0)
save(fig, '35-064')
