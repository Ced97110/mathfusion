import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
cx, cy, R = 26, 30, 15
ax.add_patch(Circle((cx, cy), R, ec=COL['fixe'], fc='none', lw=0.9, zorder=1))
line(ax, [(cx - R - 2, cy), (cx + R + 2, cy)], 'fixe', lw=0.5)
line(ax, [(cx, cy - R - 2), (cx, cy + R + 2)], 'fixe', lw=0.5)
ky = cy + 0.5 * R; dx = R * math.cos(math.radians(30))
line(ax, [(cx - R - 3, ky), (cx + R + 3, ky)], 'varie', lw=1.1)
disc(ax, cx + dx, ky, 1.7, 'sujet'); disc(ax, cx - dx, ky, 1.7, 'resultat')
text(ax, cx + dx + 2, ky + 4, 'θ', 'sujet', 'm'); text(ax, cx - dx + 1, ky + 4.2, '180° − θ', 'resultat', 's')
text(ax, 25, 58, '2 solutions par tour', 'encre', 's'); text(ax, 70, 58, 'autres tours', 'encre', 's')
labs = ['θ', 'θ + 360°', 'θ + 720°']; ys = [8, 26, 44]
for y, lb, r in zip(ys, labs, ['sujet', 'resultat', 'resultat']): box(ax, 56, y, 28, 9, r, label=lb, size='m')
for y in ys[:2]: arrow(ax, (70, y + 9.5), (70, y + 17.5), 'varie')
text(ax, 79, 21.5, '+ 360°', 'varie', 's'); text(ax, 79, 39.5, '+ 360°', 'varie', 's')
save(fig, '32-025')
