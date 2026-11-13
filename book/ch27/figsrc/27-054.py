import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
box(ax, 10, 14, 68, 56, 'fixe')
line(ax, [(10, 14), (78, 14)], 'sujet', lw=2.4)
text(ax, 44, 8, 'bord bas, au sol', 'sujet', 's')
text(ax, 20, 66, 'planche inclinée', 'fixe', 's', ha='left')
bx, by = 44, 44
for k in range(1, 4):
    disc(ax, bx, by - 6 * k, 0.9, 'varie')
arrow(ax, (bx, by - 20), (bx, 17), 'varie', lw=1.4)
disc(ax, bx, by, 3.2, 'varie')
text(ax, bx + 6, by + 1, 'bille lâchée', 'varie', 's', ha='left')
s = 4
line(ax, [(bx, 14 + s), (bx + s, 14 + s), (bx + s, 14)], 'encre', lw=0.7)
text(ax, bx + 8, 25, 'trajet : le plus raide', 'varie', 's', ha='left')
text(ax, bx + 8, 21.5, 'perpendiculaire au bord', 'varie', 's', ha='left')
save(fig, '27-054')
