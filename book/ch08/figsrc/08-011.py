import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Rectangle
fig, ax = canvas(78)
bx0, bx1 = 8, 80
step = (bx1 - bx0) / 10
brace(ax, bx0, bx1, 64, 'fixe', label='1 mètre', down=False)
for i in range(10):
    role = 'varie' if i < 3 else 'fixe'
    ax.add_patch(Rectangle((bx0 + i * step, 52), step, 8, ec=COL[role], fc=FILL[role], lw=0.8, zorder=2))
text(ax, bx0 + 1.5 * step, 47, r'$3\times\frac{1}{10}$', 'varie', 's')
box(ax, 28, 26, 16, 14, 'sujet', label='0', size='l')
box(ax, 46, 26, 16, 14, 'varie', label='3', size='l')
disc(ax, 45, 28, 0.9, 'encre')
arrow(ax, (bx0 + 1.5 * step + 6, 44), (54, 41.5), 'varie')
text(ax, 36, 21, 'unités', 'sujet', 's')
text(ax, 54, 21, 'dixièmes', 'varie', 's')
text(ax, 54, 14, 'vaut 1/10', 'varie', 's')
save(fig, '08-011')
