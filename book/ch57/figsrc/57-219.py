import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
ox, oy, dx, dy = 8, 14, 7, 10
for a in range(6):
    text(ax, ox + a * dx, 8, str(a), 'fixe', 's')
    for b in range(4):
        disc(ax, ox + a * dx, oy + b * dy, 1.0, 'fixe')
text(ax, 3.5, oy + 2 * dy, '2', 'fixe', 's')
p1 = (ox + 1 * dx, oy + 2 * dy)
p4 = (ox + 4 * dx, oy + 2 * dy)
disc(ax, p1[0], p1[1], 1.9, 'resultat')
disc(ax, p4[0], p4[1], 1.9, 'resultat')
arrow(ax, (p1[0] + 2.2, p1[1] + 1), (p4[0] - 2.2, p4[1] + 1), 'varie', curve=-0.4)
text(ax, (p1[0] + p4[0]) / 2, p1[1] + 7.3, '+ (3 ; 0)', 'varie', 's')
text(ax, 69, 54, 'classe de (1 ; 2)', 'encre', 'm')
box(ax, 54, 36, 30, 11, 'resultat', label='ℤ/3ℤ : reste 1', size='s')
box(ax, 54, 21, 30, 11, 'resultat', label='ℤ : nombre 2', size='s')
save(fig, '57-219')
