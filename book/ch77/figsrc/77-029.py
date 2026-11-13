import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def mat(ax, x, y, rows, role="sujet", rh=5.6, hw=8, size="m"):
    n = len(rows); top = y + n * rh / 2 + 0.4; bot = y - n * rh / 2 - 0.4
    for i, r in enumerate(rows):
        text(ax, x, y + n * rh / 2 - rh * (i + 0.5), r, role, size)
    for s in (-1, 1):
        xx = x + s * hw
        line(ax, [(xx - s * 1.6, top), (xx, top), (xx, bot), (xx - s * 1.6, bot)], role, lw=0.9)

fig, ax = canvas(54)
text(ax, 44, 46, r'$(2+i)+3=5+i$', 'encre', 'm')
mat(ax, 14, 28, [r'$2\quad-1$', r'$1\quad\hspace{0.7}2$'], 'sujet')
text(ax, 29.5, 28, r'$+$', 'encre', 'l')
mat(ax, 43, 28, [r'$3\quad0$', r'$0\quad3$'], 'autre', hw=6)
text(ax, 57, 28, r'$=$', 'encre', 'l')
mat(ax, 73, 28, [r'$5\quad-1$', r'$1\quad\hspace{0.7}5$'], 'resultat')
text(ax, 14, 12, r'$\rho(2+i)$', 'sujet', 's'); text(ax, 43, 12, r'$\rho(3)$', 'autre', 's'); text(ax, 73, 12, r'$\rho(5+i)$', 'resultat', 's')
save(fig, '77-029')
