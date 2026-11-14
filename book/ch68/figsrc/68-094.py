import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
U = 16  # mm par unité de distance
cy = 30
xs = [28, 28 + U, 28 + 2 * U]
disc(ax, xs[0], cy, U, 'sujet', fill=False)
disc(ax, xs[2], cy, U, 'autre', fill=False)
text(ax, xs[0], 52, 'boule de 0000', 'sujet', 's')
text(ax, xs[2], 52, 'boule de 0011', 'autre', 's')
for x, w, role in zip(xs, ['0000', '0001', '0011'], ['sujet', 'limite', 'autre']):
    disc(ax, x, cy + 3, 1.5, role)
    text(ax, x, cy - 3, w, role, 's')
text(ax, 44, 9, 'rayon 1 : 0001 dans les deux boules', 'limite', 's')
text(ax, 44, 3, r'$2t=2 \geq d=2$ : aucune règle', 'limite', 's')
save(fig, '68-094')
