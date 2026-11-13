import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
y0, u = 16, 7.0
f = numberline(ax, 16, 72, y0, -2, 2, step=1)
xs = [i / 40 * 4 - 2 for i in range(41)]
pts = [(f(x), y0 + (x * x + 1) * u) for x in xs]
line(ax, pts, 'sujet', lw=1.2)
arrow(ax, (f(0) + 4, y0 + 0.2), (f(0) + 4, y0 + u - 0.2), 'varie', both=True)
text(ax, f(0) + 7, y0 + u / 2, 'toujours ≥ 1', 'varie', 's', ha='left')
text(ax, f(2) + 1, y0 + 5 * u + 3, r'$x^2+1$', 'sujet', 'l')
text(ax, 44, 62, 'aucune racine réelle', 'limite', 'l', weight='bold')
text(ax, 44, 56, 'la courbe ne touche pas l’axe', 'limite', 'm')
save(fig, '55-104')
