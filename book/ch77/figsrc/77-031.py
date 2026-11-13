import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def mat(ax, x, y, rows, role="sujet", rh=5.6, hw=8, size="m"):
    n = len(rows); top = y + n * rh / 2 + 0.4; bot = y - n * rh / 2 - 0.4
    for i, r in enumerate(rows):
        text(ax, x, y + n * rh / 2 - rh * (i + 0.5), r, role, size)
    for s in (-1, 1):
        xx = x + s * hw
        line(ax, [(xx - s * 1.6, top), (xx, top), (xx, bot), (xx - s * 1.6, bot)], role, lw=0.9)

fig, ax = canvas(70)
box(ax, 22, 56, 44, 10, 'varie', label=r'multiplier par $i$')
arrow(ax, (32, 56), (22, 47), 'varie'); arrow(ax, (56, 56), (66, 47), 'varie')
box(ax, 6, 37, 32, 10, 'sujet', label=r'base $1,\ i$'); box(ax, 50, 37, 32, 10, 'autre', label=r'base $i,\ 1$')
arrow(ax, (22, 37), (22, 28), 'sujet'); arrow(ax, (66, 37), (66, 28), 'autre')
mat(ax, 22, 17, [r'$0\quad-1$', r'$1\quad\hspace{0.7}0$'], 'sujet')
mat(ax, 66, 17, [r'$\hspace{0.7}0\quad1$', r'$-1\quad0$'], 'autre')
text(ax, 44, 17, r'$\neq$', 'varie', 'l')
text(ax, 22, 5, r'$\rho(i)$', 'sujet', 's'); text(ax, 66, 5, r'$\rho(i)$', 'autre', 's')
save(fig, '77-031')
