import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Rectangle
fig, ax = canvas(60)
bx0, bx1 = 8, 80
step = (bx1 - bx0) / 10
text(ax, 80, 55, '1 mètre', 'fixe', 's', ha='right')
text(ax, 8, 55, '1/10', 'varie', 's', ha='left')
for i in range(10):
    role = 'varie' if i == 0 else 'fixe'
    ax.add_patch(Rectangle((bx0 + i * step, 40), step, 8, ec=COL[role], fc=FILL[role], lw=0.8, zorder=2))
line(ax, [(bx0, 39), (bx0, 30)], 'varie', dash=True)
line(ax, [(bx0 + step, 39), (bx1, 30)], 'varie', dash=True)
for i in range(10):
    role = 'resultat' if i == 0 else 'varie'
    fc = FILL[role]
    ax.add_patch(Rectangle((bx0 + i * step, 22), step, 8, ec=COL[role], fc=fc, lw=0.8, zorder=2))
text(ax, 8, 17, '1/100', 'resultat', 's', ha='left')
text(ax, 44, 9, '10 centièmes font 1 dixième', 'encre', 's')
save(fig, '08-012')
