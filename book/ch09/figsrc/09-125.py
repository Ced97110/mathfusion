import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
k, y0, bw = 0.4, 6, 20
xs = [4, 34, 64]
box(ax, xs[0], y0, bw, 100 * k, 'sujet', label='100')
box(ax, xs[1], y0, bw, 120 * k, 'varie', label='120')
box(ax, xs[2], y0, bw, 96 * k, 'limite', label='96')
box(ax, xs[2], y0 + 96 * k, bw, 24 * k, 'fixe', fill=False, dash=True, label='−24', size='s')
line(ax, [(xs[0] + bw, y0 + 100 * k), (xs[2] + bw, y0 + 100 * k)], 'fixe', dash=True)
arrow(ax, (xs[0] + bw + 1, 22), (xs[1] - 1, 22), 'varie'); arrow(ax, (xs[1] + bw + 1, 22), (xs[2] - 1, 22), 'varie')
text(ax, 29, 58, '+20 % de 100', 'varie', 's'); text(ax, 60, 64, '−20 % de 120', 'varie', 's')
text(ax, 78, 58, '≠ 100', 'limite', 's')
save(fig, '09-125')
