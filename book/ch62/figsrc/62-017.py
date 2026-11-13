import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
cx, cy, s = 44, 10, 36
h = math.sqrt(3) / 2
arrow(ax, (cx - 40, cy), (cx + 36, cy), 'fixe', lw=0.7)
arrow(ax, (cx, cy - 4), (cx, cy + 46), 'fixe', lw=0.7)
jx, jy = cx - 0.5 * s, cy + h * s
line(ax, [(jx, cy), (jx, jy)], 'fixe', lw=0.7, dash=True)
arrow(ax, (cx, cy + 2.5), (jx + 1.2, cy + 2.5), 'varie', lw=1.5)
arrow(ax, (jx - 4, cy), (jx - 4, jy - 1.5), 'autre', lw=1.5) if False else None
arrow(ax, (jx, cy + 2.5), (jx, jy - 1.8), 'autre', lw=1.5)
disc(ax, jx, jy, 1.7, 'sujet')
text(ax, jx - 3, jy + 3.5, '$j$', 'sujet', 'l')
text(ax, jx + 1.5, cy - 4, '−1/2', 'varie', 'm')
text(ax, jx - 2.5, cy + 15, '$\\sqrt{3}/2$\n≈ 0,87', 'autre', 's', ha='right')
text(ax, 44, 61, '$j$ = −1/2 + ($\\sqrt{3}$/2) $i$', 'encre', 'l')
text(ax, cx + 4, cy + 28, 'gauche de 0,\nau-dessus de l’axe', 'fixe', 's', ha='left')
save(fig, '62-017')
