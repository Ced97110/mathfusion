import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(48)
g = 3.6; gx, gy = 4, 6
for col in range(10):
    for r in range(10):
        k = col * 10 + (9 - r)
        fc = COL['sujet'] if k < 35 else FILL['fixe']
        ax.add_patch(Rectangle((gx + col * g, gy + r * g), g, g, ec='white', fc=fc, lw=0.3, zorder=2))
ax.add_patch(Rectangle((gx, gy), 10 * g, 10 * g, ec=COL['fixe'], fc='none', lw=0.8, zorder=3))
text(ax, 64, 39, 'parts colorées', 'sujet', 's')
text(ax, 64, 31, '35', 'sujet', 'l', weight='bold')
line(ax, [(56, 26.5), (72, 26.5)], 'encre', lw=1.0)
text(ax, 64, 21, '100', 'fixe', 'l', weight='bold')
text(ax, 64, 12, 'parts en tout', 'fixe', 's')
save(fig, '08-028')
