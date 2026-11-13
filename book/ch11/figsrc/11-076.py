import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
c = 4.2; x0 = 16; y0 = 18
for i in range(12):
    for j in range(8):
        ax.add_patch(Rectangle((x0 + i * c, y0 + j * c), c, c, fc=FILL['autre'], ec=COL['autre'], lw=0.3, zorder=2))
ax.add_patch(Rectangle((x0, y0), 12 * c, 8 * c, fc='none', ec=COL['sujet'], lw=2.2, zorder=3))
text(ax, x0 + 6 * c, y0 + 8 * c + 3, '12 m', 'fixe', 's'); text(ax, x0 - 2, y0 + 4 * c, '8 m', 'fixe', 's', ha='right')
text(ax, 44, 74, 'bord : périmètre = 40 m', 'sujet', 'm', weight='bold')
text(ax, 44, 8, 'intérieur : aire = 96 m²', 'autre', 'm', weight='bold')
save(fig, '11-076')
