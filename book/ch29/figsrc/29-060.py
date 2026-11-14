import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def arc(cx, cy, r, a0, a1, n=90):
    return [(cx + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), cy + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
fig, ax = canvas(46)
yc = 26
box(ax, 3, yc - 6, 16, 12, 'sujet', label='10°')
arrow(ax, (20, yc), (34, yc), 'varie')
text(ax, 27, yc + 3.5, r'$\times\ \pi$/180', 'varie', 's')
box(ax, 35, yc - 6, 22, 12, 'fixe', label=r'10$\pi$/180', size='s')
arrow(ax, (58, yc), (70, yc), 'varie')
text(ax, 64, yc + 3.5, '÷ 10', 'varie', 's')
text(ax, 64, yc - 8, 'haut et bas', 'varie', 's')
box(ax, 71, yc - 6, 14, 12, 'resultat', label=r'$\pi$/18')
text(ax, 78, 14, '≈ 0,1745', 'resultat', 's')
text(ax, 30, 8, r'valeur exacte : on garde $\pi$', 'resultat', 's')
save(fig, '29-060')
