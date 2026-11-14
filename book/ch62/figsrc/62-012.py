import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
cx, cy, s = 34, 35, 20
R = 2 ** (1 / 3)
P = [(cx + R * s, cy), (cx - R / 2 * s, cy + R * math.sqrt(3) / 2 * s), (cx - R / 2 * s, cy - R * math.sqrt(3) / 2 * s)]
ax.add_patch(Circle((cx, cy), R * s, fill=False, ec=COL['fixe'], ls='--', lw=0.8, zorder=1))
arrow(ax, (cx - 28, cy), (cx + 40, cy), 'fixe', lw=0.7)
arrow(ax, (cx, cy - 31), (cx, cy + 33), 'fixe', lw=0.7)
text(ax, cx + 40, cy - 4, 'axe réel', 'fixe', 's', ha='right')
text(ax, cx + 2, cy + 33, 'axe imaginaire', 'fixe', 's', ha='left')
poly(ax, P, 'sujet', fill=False)
for (x, y), nm, ha, dx, dy in zip(P, ['$r_1$\n1,26 ; 0', '$r_2$\n−0,63 ; 1,09', '$r_3$\n−0,63 ; −1,09'],
                                 ['left', 'right', 'right'], [3, -2.5, -2.5], [4, 3.5, -3.5]):
    disc(ax, x, y, 1.5, 'sujet')
    text(ax, x + dx, y + dy, nm, 'sujet', 's', ha=ha)
text(ax, 80, 62, 'même distance\nau centre', 'fixe', 's', ha='right')
save(fig, '62-012')
