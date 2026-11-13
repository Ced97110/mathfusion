import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Polygon as MPoly
fig, ax = canvas(50)
U, OX, OY = 14, 10, 8
P = lambda x, y: (OX + U * x, OY + U * y)
for i in range(4):
    for j in range(3):
        disc(ax, *P(i, j), 0.7, 'fixe')
ax.add_patch(MPoly([P(0, 0), P(2, 1), P(3, 2), P(1, 1)], closed=True, ec=COL['varie'], fc=FILL['varie'], alpha=0.7, lw=1.0, zorder=1.5))
ax.add_patch(MPoly([P(0, 0), P(1, 0), P(1, 1), P(0, 1)], closed=True, ec=COL['sujet'], fc=FILL['sujet'], alpha=0.85, lw=1.0, zorder=1.6))
arrow(ax, P(0, 0), P(1, 0), 'sujet', lw=1.2)
arrow(ax, P(0, 0), P(0, 1), 'sujet', lw=1.2)
arrow(ax, P(0, 0), P(2, 1), 'varie', lw=1.2)
arrow(ax, P(0, 0), P(1, 1), 'varie', lw=1.2)
text(ax, 17, 5, '$e_1$', 'sujet', 'm')
text(ax, 7, 15, '$e_2$', 'sujet', 'm')
text(ax, 41, 17.5, '$f_1$', 'varie', 'm')
text(ax, 20, 26.5, '$f_2$', 'varie', 'm')
text(ax, 17, 13.5, 'aire 1', 'sujet', 's')
text(ax, 36, 25, 'aire 1', 'varie', 's')
text(ax, 62, 44, 'points gris : réseau ℤ²', 'fixe', 's')
save(fig, '58-231')
