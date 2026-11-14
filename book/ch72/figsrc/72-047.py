import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
def ax2(ax, cx, cy, r):
    arrow(ax, (cx - r, cy), (cx + r, cy), 'fixe', lw=0.6)
    arrow(ax, (cx, cy - r), (cx, cy + r), 'fixe', lw=0.6)

x0, y0, c = 8, 24, 11
for i, r in enumerate([[1, 0], [0, -1]]):
    for j, v in enumerate(r):
        box(ax, x0 + j * c, y0 + (1 - i) * c, c, c, 'sujet', label=str(v).replace('-', '\u2212'))
text(ax, x0 + c, y0 + 2 * c + 5, r'$b$', 'sujet', 'l')
text(ax, x0 + c, y0 - 6, r'$\det b = -1$', 'resultat', 'm')
ax2(ax, 62, 34, 20)
line(ax, [(46, 18), (78, 50)], 'limite', lw=1.6)
text(ax, 76, 55, '(1, 1)', 'limite', 's')
text(ax, 62, 10, 'carré 0 : isotrope', 'limite', 's')
text(ax, 44, 60, 'dimension 2', 'sujet', 'm') if False else None
text(ax, x0 + c, y0 - 14, 'dimension 2', 'sujet', 's')
save(fig, '72-047')
