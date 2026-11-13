import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(100)
X = lambda x: 44 + 13 * x
Y = lambda v: 50 + 3 * v
line(ax, [(6, 50), (82, 50)], 'fixe', lw=0.6)
for s in (-1, 1): line(ax, [(X(s * math.pi / 2), 4), (X(s * math.pi / 2), 96)], 'fixe', dash=True)
xm = math.atan(14.5); n = 80
line(ax, [(X(-xm + i * 2 * xm / n), Y(math.tan(-xm + i * 2 * xm / n))) for i in range(n + 1)], 'sujet', lw=1.5)
line(ax, [(6, 80), (82, 80)], 'limite', dash=True); line(ax, [(6, 20), (82, 20)], 'limite', dash=True)
text(ax, 8, 83.5, 'candidat max : 10 000', 'limite', 's', ha='left'); text(ax, 80, 16.5, 'candidat min : −10 000', 'limite', 's', ha='right')
text(ax, 76, 90, 'toujours dépassé', 'varie', 's'); text(ax, 12, 10, 'toujours dépassé', 'varie', 's')
arrow(ax, (X(xm) - 1, 82), (X(xm) - 0.3, 96), 'varie'); arrow(ax, (X(-xm) + 1, 18), (X(-xm) + 0.3, 4), 'varie')
text(ax, 13, 65, 'aucune\nplus grande\nvaleur', 'sujet', 's')
save(fig, '30-060')
