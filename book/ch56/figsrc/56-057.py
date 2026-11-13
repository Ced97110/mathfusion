import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(100)
h = 10
ys = [88, 72, 56, 40]
labs = [('sujet', 'dans ℤ[√3 i] : 2 = morceau × morceau'),
        ('sujet', 'normes : produit 4, norme 1 = unité'),
        ('varie', 'donc chaque morceau a la norme 2'),
        ('varie', 'norme = a² + 3b² : égale à 2 ?')]
for y, (role, lab) in zip(ys, labs):
    box(ax, 4, y, 80, h, role, label=lab, size='s')
for y0, y1 in zip(ys[:-1], ys[1:]):
    arrow(ax, (44, y0 - 0.5), (44, y1 + h + 0.5), 'fixe')
box(ax, 2, 24, 41, 9, 'limite', label='b ≠ 0 : 3b² ≥ 3, trop grand', size='s')
box(ax, 45, 24, 41, 9, 'limite', label='b = 0 : a² = 2, impossible', size='s')
arrow(ax, (22, ys[3] - 0.5), (22, 33.5), 'limite')
arrow(ax, (66, ys[3] - 0.5), (66, 33.5), 'limite')
text(ax, 44, 19, 'valeurs atteintes par a² + 3b²', 'encre', 's')
f = numberline(ax, 10, 70, 9, 0, 4, arrow_right=False, size='s')
for v in (0, 1, 3, 4):
    disc(ax, f(v), 9, 1.8, 'sujet')
disc(ax, f(2), 9, 2.4, 'limite', fill=False, lw=1.2)
text(ax, f(2), 14, 'jamais atteinte', 'limite', 's')
save(fig, '56-057')
