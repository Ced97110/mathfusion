import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(46)
x0, x1, y = 8, 76, 24
f = lambda v: x0 + v / 160 * (x1 - x0)
line(ax, [(x0, y), (x1, y)], 'fixe')
for v, role, lab in [(0, 'fixe', '0°'), (72, 'sujet', '72°'), (144, 'sujet', None), (150, 'autre', '150°')]:
    ax.plot([f(v)]*2, [y - 1.3, y + 1.3], color=COL[role], lw=1.0, zorder=3)
    if lab: text(ax, f(v), y - 4, lab, role, 's')
arrow(ax, (f(0), y + 1.5), (f(72), y + 1.5), 'sujet', curve=-0.4)
arrow(ax, (f(72), y + 1.5), (f(144), y + 1.5), 'sujet', curve=-0.4)
text(ax, f(36), y + 8.5, '72°', 'sujet', 's'); text(ax, f(108), y + 8.5, '72°', 'sujet', 's')
brace(ax, f(144), f(150), y + 4, 'limite', label='reste 6°', down=False)
text(ax, 44, 12, r'$150 = 2 \times 72 + 6$', 'autre', 'm')
text(ax, 44, 5, r'6° < 72° : impossible', 'limite', 'm')
save(fig, '74-069')
