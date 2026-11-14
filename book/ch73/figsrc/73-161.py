import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def mat(ax, cx, cy, s, role, w=7.5, h=5.5):
    text(ax, cx, cy, s, role, "m")
    for g in (-1, 1):
        x = cx + g * w
        line(ax, [(x - g * 1.2, cy + h), (x, cy + h), (x, cy - h), (x - g * 1.2, cy - h)], role)

fig, ax = canvas(74)
yA, yB = 52, 24
mat(ax, 12, yA, '2   0\n0   ½', 'sujet'); text(ax, 24, yA, r'$\times$', 'encre', 'l')
mat(ax, 36, yA, '1   2\n0   1', 'varie'); text(ax, 48, yA, '=', 'encre', 'l')
mat(ax, 62, yA, '2   4\n0   ½', 'fixe')
text(ax, 12, yA + 10, r'$D$', 'sujet'); text(ax, 36, yA + 10, r'$T_{12}(2)$', 'varie')
arrow(ax, (62, yA - 8), (14, yB + 8), 'fixe', curve=0.15)
mat(ax, 12, yB, '2   4\n0   ½', 'fixe'); text(ax, 24, yB, r'$\times$', 'encre', 'l')
mat(ax, 36, yB, '½   0\n0   2', 'sujet'); text(ax, 48, yB, '=', 'encre', 'l')
mat(ax, 62, yB, '1   8\n0   1', 'resultat')
text(ax, 36, yB - 10, r'$D^{-1}$', 'sujet'); text(ax, 62, yB - 10, 'pente 8 = 2 × 4', 'resultat', 's')
save(fig, '73-161')
