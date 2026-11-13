import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
cx, cy, R = 22, 32, 17
ax.add_patch(Circle((cx, cy), R, ec=COL['fixe'], fc='none', lw=0.9, zorder=1))
line(ax, [(cx - R - 2, cy), (cx + R + 2, cy)], 'fixe', lw=0.5)
line(ax, [(cx, cy - R - 2), (cx, cy + R + 2)], 'fixe', lw=0.5)
ky = cy + 0.5 * R; dx = R * math.cos(math.radians(30)); xa = 50
line(ax, [(xa, cy - R), (xa, cy + R + 2)], 'fixe', lw=0.8)
line(ax, [(xa - 1.2, cy), (xa + 1.2, cy)], 'fixe'); line(ax, [(xa - 1.2, ky), (xa + 1.2, ky)], 'fixe')
line(ax, [(cx - dx, ky), (xa, ky)], 'varie', lw=1.1)
disc(ax, cx + dx, ky, 1.7, 'sujet'); disc(ax, cx - dx, ky, 1.7, 'resultat')
text(ax, cx + dx + 3.5, ky + 3, '30°', 'sujet', 's'); text(ax, cx - dx + 1, ky + 3.6, '150°', 'resultat', 's')
text(ax, xa + 4.5, ky + 3, '0,5', 'varie', 's'); text(ax, xa, cy + R + 5, 'hauteur', 'fixe', 's')
text(ax, 71, 52, 'sin 30° = 0,5', 'sujet', 'm'); text(ax, 71, 38, 'sin 150° = 0,5', 'resultat', 'm')
text(ax, 71, 18, '30° + 150° = 180°', 'varie', 'm')
save(fig, '32-022')
