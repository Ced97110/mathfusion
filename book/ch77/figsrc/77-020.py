import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def mat(ax, x, y, rows, role="sujet", rh=5.6, hw=8, size="m"):
    n = len(rows); top = y + n * rh / 2 + 0.4; bot = y - n * rh / 2 - 0.4
    for i, r in enumerate(rows):
        text(ax, x, y + n * rh / 2 - rh * (i + 0.5), r, role, size)
    for s in (-1, 1):
        xx = x + s * hw
        line(ax, [(xx - s * 1.6, top), (xx, top), (xx, bot), (xx - s * 1.6, bot)], role, lw=0.9)

fig, ax = canvas(60)
rows = [(48, r'$\mathbb{C}$ sur $\mathbb{R}$', ['1', '$i$'], '$n=2$'),
        (30, r'$a+b\sqrt{2}$ sur $\mathbb{Q}$', ['1', r'$\sqrt{2}$'], '$n=2$'),
        (12, 'matrices $2\\times2$', ['1', '2', '3', '4'], '$n=4$')]
for y, lab, cells, n in rows:
    text(ax, 3, y, n, 'varie', 'm', ha='left')
    text(ax, 18, y, lab, 'sujet', 's', ha='left')
    for k, c in enumerate(cells):
        box(ax, 52 + 9 * k, y - 4, 6.5, 8, 'fixe', label=c, size='s', r=0.6)
save(fig, '77-020')
