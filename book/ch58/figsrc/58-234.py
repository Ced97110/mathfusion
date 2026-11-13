import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Polygon as MPoly
fig, ax = canvas(52)
U, OX, OY = 12, 10, 12
P = lambda x, y: (OX + U * x, OY + U * y)
ax.add_patch(MPoly([P(0, 0), P(2, 0), P(2, 1), P(0, 1)], closed=True, ec=COL['varie'], fc=FILL['varie'], alpha=0.8, lw=1.0, zorder=1.5))
for i in range(5):
    for j in range(3):
        if i % 2 == 0:
            disc(ax, *P(i, j), 1.0, 'resultat')
        else:
            disc(ax, *P(i, j), 1.0, 'limite', fill=False, lw=1.0)
arrow(ax, P(0, 0), P(2, 0), 'varie', lw=1.3)
arrow(ax, P(0, 0), P(0, 1), 'varie', lw=1.3)
text(ax, 30, 15.5, '$f_1$', 'varie', 'm')
text(ax, 6.5, 18, '$f_2$', 'varie', 'm')
text(ax, 22, 6, '(1, 0) : il faudrait ½ $f_1$', 'limite', 's')
text(ax, 44, 46, 'déterminant 2 : aire 2', 'varie', 'm')
disc(ax, 66, 36, 1.0, 'resultat')
text(ax, 69, 36, 'atteint', 'resultat', 's', ha='left')
disc(ax, 66, 30, 1.0, 'limite', fill=False, lw=1.0)
text(ax, 69, 30, 'non atteint', 'limite', 's', ha='left')
save(fig, '58-234')
