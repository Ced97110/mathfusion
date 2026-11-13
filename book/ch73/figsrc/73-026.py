import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
cell = 11; gap = 1.8; gx, gy = 3, 6
mats = [(a, b, c, d) for a in (0, 1) for b in (0, 1) for c in (0, 1) for d in (0, 1)]
inv = [(a * d - b * c) % 2 == 1 for a, b, c, d in mats]
order = sorted(range(16), key=lambda i: not inv[i])
for pos, i in enumerate(order):
    a, b, c, d = mats[i]; role = 'sujet' if inv[i] else 'limite'
    x = gx + (pos % 4) * (cell + gap); y = gy + (3 - pos // 4) * (cell + gap)
    box(ax, x, y, cell, cell, role, r=0.6)
    q = 3.4
    for (v, dx, dy) in [(a, 0, 1), (b, 1, 1), (c, 0, 0), (d, 1, 0)]:
        ax.add_patch(Rectangle((x + 1.8 + dx * (q + 0.5), y + 1.8 + dy * (q + 0.5)), q, q, fc=COL[role] if v else 'white', ec=COL[role], lw=0.4, zorder=3))
text(ax, 64, 60, 'case pleine = 1, vide = 0', 'fixe', 's')
text(ax, 64, 53, '16 matrices', 'encre', 'm')
text(ax, 64, 40, '6 peuvent être', 'sujet', 's'); text(ax, 64, 35.5, 'défaites', 'sujet', 's')
text(ax, 64, 24, '10 écrasent', 'limite', 's'); text(ax, 64, 19.5, 'le plan', 'limite', 's')
text(ax, 64, 9, r'$GL_2(\mathbb{F}_2)$ : 6', 'sujet', 'm')
text(ax, 64, 46.5, 'case pleine = 1', 'fixe', 's') if False else None
save(fig, '73-026')
