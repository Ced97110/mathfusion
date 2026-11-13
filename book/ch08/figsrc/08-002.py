import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Rectangle
fig, ax = canvas(62)
text(ax, 53, 58, 'Le même mètre, coupé', 'encre', 'm')
bx0, bx1 = 24, 82
rows = [('décimètre', 10, 'autre', '10 parts de 1/10', 44),
        ('centimètre', 100, 'sujet', '100 parts de 1/100', 27),
        ('millimètre', 1000, 'autre', '1 000 parts de 1/1000', 10)]
for name, n, role, lab, y in rows:
    step = (bx1 - bx0) / n
    ax.add_patch(Rectangle((bx0, y), bx1 - bx0, 6, ec=COL[role], fc=FILL['fixe'], lw=0.8, zorder=1))
    ax.add_patch(Rectangle((bx0, y), max(step, 0.7), 6, ec=COL[role], fc=COL[role], lw=0.4, zorder=2))
    for i in range(1, n):
        ax.plot([bx0 + i * step] * 2, [y, y + 6], color=COL[role], lw=0.9 if n == 10 else 0.25 if n == 100 else 0.08, zorder=1.5)
    text(ax, 3, y + 3, name, role, 'm', ha='left')
    text(ax, bx0, y - 3.5, lab, role, 's', ha='left')
save(fig, '08-002')
