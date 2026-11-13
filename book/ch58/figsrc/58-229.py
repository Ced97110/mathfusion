import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
y = 34
f = numberline(ax, 10, 70, y, -3, 3, 1, arrow_right=False)
for v in (-1, 1):
    disc(ax, f(v), y, 1.8, 'resultat')
disc(ax, f(2), y, 1.8, 'limite')
text(ax, 44, 44, 'inversible dans M₂(ℤ)', 'resultat', 's')
text(ax, 44, 53, 'déterminant d’une matrice entière', 'encre', 's')
def mat(cx, cy, rows, role, cw=6.0, rh=5.6):
    w, h = 2 * cw, 2 * rh; x0, y0 = cx - w / 2, cy - h / 2
    for sx, d in ((x0 - 0.6, 1), (x0 + w + 0.6, -1)):
        line(ax, [(sx + 1.3 * d, y0 - 0.4), (sx, y0 - 0.4), (sx, y0 + h + 0.4), (sx + 1.3 * d, y0 + h + 0.4)], 'fixe', lw=0.9)
    for i, row in enumerate(rows):
        text(ax, cx, y0 + h - (i + 0.5) * rh, '    '.join(row), role, 'm')
mat(14, 17, [['2', '0'], ['0', '1']], 'limite')
text(ax, 50, 17, r'$2\times1-0\times0=2$', 'limite', 'm')
arrow(ax, (24, 17), (31, 17), 'limite')
text(ax, 44, 5, 'inverse : (½, 0) et (0, 1)', 'limite', 's')
save(fig, '58-229')
