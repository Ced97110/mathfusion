import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def arc(cx, cy, r, a0, a1, n=90):
    return [(cx + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), cy + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
fig, ax = canvas(40)
yc = 18
box(ax, 3, yc - 6, 18, 12, 'sujet', label=r'$\theta$ = 0,6', size='s')
arrow(ax, (22, yc), (32, yc), 'varie')
text(ax, 27, yc + 3.5, r'$\times$ 180', 'varie', 's')
box(ax, 33, yc - 6, 14, 12, 'fixe', label='108')
arrow(ax, (48, yc), (58, yc), 'varie')
text(ax, 53, yc + 3.5, r'÷ $\pi$', 'varie', 's')
box(ax, 59, yc - 6, 26, 12, 'resultat', label=r'$d$ ≈ 34,38°', size='s')
text(ax, 44, 34, 'radians vers degrés', 'encre', 's')
save(fig, '29-055')
