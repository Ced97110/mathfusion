import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def mat(ax, x, y, rows, role="sujet", rh=5.6, hw=8, size="m"):
    n = len(rows); top = y + n * rh / 2 + 0.4; bot = y - n * rh / 2 - 0.4
    for i, r in enumerate(rows):
        text(ax, x, y + n * rh / 2 - rh * (i + 0.5), r, role, size)
    for s in (-1, 1):
        xx = x + s * hw
        line(ax, [(xx - s * 1.6, top), (xx, top), (xx, bot), (xx - s * 1.6, bot)], role, lw=0.9)

fig, ax = canvas(44)
box(ax, 39, 6, 16, 22, 'varie'); box(ax, 59, 6, 16, 22, 'varie')
for xc, (a, b) in ((47, ('$2$', '$1$')), (67, ('$-1$', '$2$'))):
    text(ax, xc, 22, a, 'encre', 'l'); text(ax, xc, 12, b, 'encre', 'l')
for s, xx in ((-1, 37), (1, 77)):
    line(ax, [(xx - s * 1.6, 29.5), (xx, 29.5), (xx, 4.5), (xx - s * 1.6, 4.5)], 'sujet', lw=0.9)
text(ax, 47, 35, 'image de 1', 'varie', 's'); text(ax, 67, 35, r'image de $i$', 'varie', 's')
text(ax, 17, 17, r'$\rho(2+i)=$', 'sujet', 'l')
save(fig, '77-018')
