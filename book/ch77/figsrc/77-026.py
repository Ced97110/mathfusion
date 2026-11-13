import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def mat(ax, x, y, rows, role="sujet", rh=5.6, hw=8, size="m"):
    n = len(rows); top = y + n * rh / 2 + 0.4; bot = y - n * rh / 2 - 0.4
    for i, r in enumerate(rows):
        text(ax, x, y + n * rh / 2 - rh * (i + 0.5), r, role, size)
    for s in (-1, 1):
        xx = x + s * hw
        line(ax, [(xx - s * 1.6, top), (xx, top), (xx, bot), (xx - s * 1.6, bot)], role, lw=0.9)

fig, ax = canvas(60)
xs = [11, 26, 41, 56, 72]
for x, t in zip(xs, ['$i$', r'$\times$', '$i$', '$=$', '$-1$']):
    text(ax, x, 51, t, 'sujet', 'l')
for x in (11, 41, 72):
    arrow(ax, (x, 45), (x, 31), 'varie')
text(ax, 15, 38, r'$\rho$', 'varie', 'm', ha='left')
mat(ax, 11, 20, [r'$0\quad-1$', r'$1\quad\hspace{0.7}0$'], 'autre')
text(ax, 26, 20, r'$\times$', 'autre', 'l')
mat(ax, 41, 20, [r'$0\quad-1$', r'$1\quad\hspace{0.7}0$'], 'autre')
text(ax, 56, 20, '$=$', 'autre', 'l')
mat(ax, 72, 20, [r'$-1\quad\hspace{0.7}0$', r'$\hspace{0.7}0\quad-1$'], 'autre')
save(fig, '77-026')
