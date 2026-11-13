import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
s = 7                     # 1 unité = 7 mm ; rayon 4 = 28 mm
cx, cy = 44, 34
arrow(ax, (cx - 33, cy), (cx + 33, cy), 'fixe', lw=0.7)
arrow(ax, (cx, cy - 31), (cx, cy + 31), 'fixe', lw=0.7)
pts = [(cx + 4 * s * math.cos(t), cy + 4 * s * math.sin(t)) for t in [2 * math.pi * i / 300 for i in range(301)]]
line(ax, pts, 'sujet', lw=1.3)
# t augmente
arc = [(cx + 4 * s * math.cos(t), cy + 4 * s * math.sin(t)) for t in [0.15 + (math.pi / 2 - 0.3) * i / 30 for i in range(31)]]
ax.add_patch(FancyArrowPatch(arc[0], arc[-1], arrowstyle='-|>', mutation_scale=7, lw=1.2, color=COL['varie'], connectionstyle='arc3,rad=0.28', zorder=4))
text(ax, cx + 24, cy + 24, 't augmente', 'varie', 's')
for t, lab, dx, dy, ha in [(0, 't = 0\n(4 ; 0)', 2.5, 5.5, 'left'), (math.pi / 2, 'quart de tour\n(0 ; 4)', 0, 6.5, 'center'), (math.pi, 'demi-tour\n(−4 ; 0)', -2.5, 5.5, 'right')]:
    px, py = cx + 4 * s * math.cos(t), cy + 4 * s * math.sin(t)
    disc(ax, px, py, 1.2, 'varie')
    text(ax, px + dx, py + dy, lab, 'varie', 's', ha=ha)
text(ax, 4, 4, 'x = 4 cos t', 'sujet', 'm', ha='left')
text(ax, 84, 4, 'y = 4 sin t', 'sujet', 'm', ha='right')
save(fig, '40-093')
