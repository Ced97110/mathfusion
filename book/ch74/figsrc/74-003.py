import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
def lattice(x0, y0, kind, role):
    box(ax, x0, y0, 24, 22, 'encre')
    for a in range(3):
        for b in range(3):
            x, y = x0 + 4.5 + a * 7.5, y0 + 4 + b * 7
            if kind == 0: disc(ax, x, y, 2.2, role)
            else: box(ax, x - 2, y - 2, 4, 4, role, r=0.3)
lattice(3, 48, 0, 'varie'); lattice(3, 10, 1, 'autre')
text(ax, 15, 74, 'papier 1', 'varie', 's'); text(ax, 15, 6, 'papier 2', 'autre', 's')
box(ax, 40, 8, 46, 66, 'resultat', fill=False, lw=1.0)
text(ax, 63, 69, 'même liste de mouvements', 'resultat', 's')
arrow(ax, (28, 59), (39, 56), 'fixe', lw=0.8); arrow(ax, (28, 21), (39, 26), 'fixe', lw=0.8)
# glisser
text(ax, 55, 56, 'glisser', 'encre', 'm'); arrow(ax, (68, 56), (80, 56), 'varie')
# tourner
text(ax, 55, 41, 'tourner', 'encre', 'm')
import math
pts = [(74 + 6 * math.cos(math.radians(a)), 41 + 6 * math.sin(math.radians(a))) for a in range(20, 300, 10)]
line(ax, pts, 'varie', lw=1.0); arrow(ax, pts[-2], pts[-1], 'varie')
# retourner
text(ax, 55, 24, 'retourner', 'encre', 'm')
line(ax, [(74, 17), (74, 31)], 'varie', lw=1.0, dash=True)
poly(ax, [(68, 21), (72, 21), (72, 27)], 'varie'); poly(ax, [(80, 21), (76, 21), (76, 27)], 'varie')
save(fig, '74-003')
