import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
g = 1.8; s = 10 * g
for i in range(2):
    ax.add_patch(Rectangle((4 + i * (s + 3), 16), s, s, ec=COL['fixe'], fc=FILL['fixe'], lw=0.8, zorder=2))
gx = 4 + 2 * (s + 3) + 4
for c in range(10):
    for r in range(10):
        k = c * 10 + (9 - r)
        ax.add_patch(Rectangle((gx + c * g, 16 + r * g), g, g, ec='white', fc=COL['autre'] if k < 35 else FILL['fixe'], lw=0.3, zorder=2))
ax.add_patch(Rectangle((gx, 16), s, s, ec=COL['fixe'], fc='none', lw=0.8, zorder=3))
text(ax, 4 + s + 1.5, 46, '2 entiers', 'fixe', 'm', weight='bold')
text(ax, gx + s / 2, 46, '35 centièmes', 'autre', 'm', weight='bold')
brace(ax, 4, 4 + 2 * s + 3, 35, 'fixe', 'partie entière', down=False)
brace(ax, gx, gx + s, 35, 'autre', 'partie décimale', down=False)
text(ax, 44, 7, r'$2{,}35 = 2 + 35$ centièmes', 'encre', 'm')
save(fig, '08-030')
