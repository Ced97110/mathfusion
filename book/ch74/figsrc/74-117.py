import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
f = numberline(ax, 8, 68, 12, 0, 6, step=1, arrow_right=True)
for k, v in enumerate([0, 1, 2]):
    y = 26 + k * 8
    line(ax, [(f(v), 12), (f(v), y)], 'fixe', lw=0.6, dash=True)
    line(ax, [(f(v + 3), 12), (f(v + 3), y)], 'fixe', lw=0.6, dash=True)
    disc(ax, f(v), 12, 1.2, 'sujet'); disc(ax, f(v + 3), 12, 1.2, 'resultat')
    arrow(ax, (f(v), y), (f(v + 3), y), 'varie', lw=1.2)
    text(ax, (f(v) + f(v + 3)) / 2, y + 2.4, '+ 3', 'varie', 's')
box(ax, 18, 50, 52, 10, 'limite', label=r'$x_1+3=x_1$ : impossible', size='m')
text(ax, 44, 3, 'départ ≠ arrivée, pour tout point', 'limite', 's')
save(fig, '74-117')
