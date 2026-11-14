import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
y = 34
f = numberline(ax, 8, 56, y, 0, 4, 1, arrow_right=False)
arrow(ax, (f(1), y + 2), (f(2), y + 2), 'varie', curve=-0.5)
text(ax, (f(1) + f(2)) / 2, y + 8.5, '×2', 'varie', 's')
arrow(ax, (f(2), y + 2), (f(4), y + 2), 'varie', curve=-0.5)
text(ax, f(3), y + 12, '×2', 'varie', 's')
disc(ax, f(0.5), y, 1.4, 'limite', fill=False, lw=1.2)
arrow(ax, (f(1), 25), (f(0.5), 25), 'limite')
line(ax, [(f(0.5), 32.5), (f(0.5), 25)], 'limite', dash=True)
text(ax, 22, 19, 'un demi : pas entier', 'limite', 's')
text(ax, 44, 57, r'$(a,b)\mapsto(2a,b)$', 'varie', 'm')
def mat(cx, cy, rows, role, cw=6.0, rh=5.6):
    w, h = 2 * cw, 2 * rh; x0, y0 = cx - w / 2, cy - h / 2
    for sx, d in ((x0 - 0.6, 1), (x0 + w + 0.6, -1)):
        line(ax, [(sx + 1.3 * d, y0 - 0.4), (sx, y0 - 0.4), (sx, y0 + h + 0.4), (sx + 1.3 * d, y0 + h + 0.4)], 'fixe', lw=0.9)
    for i, row in enumerate(rows):
        text(ax, cx, y0 + h - (i + 0.5) * rh, '    '.join(row), role, 'm')
mat(75, 34, [['2', '0'], ['0', '1']], 'sujet')
text(ax, 75, 45, 'tableau', 'sujet', 's')
save(fig, '58-224')
