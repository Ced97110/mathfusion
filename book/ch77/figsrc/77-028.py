import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def mat(ax, x, y, rows, role="sujet", rh=5.6, hw=8, size="m"):
    n = len(rows); top = y + n * rh / 2 + 0.4; bot = y - n * rh / 2 - 0.4
    for i, r in enumerate(rows):
        text(ax, x, y + n * rh / 2 - rh * (i + 0.5), r, role, size)
    for s in (-1, 1):
        xx = x + s * hw
        line(ax, [(xx - s * 1.6, top), (xx, top), (xx, bot), (xx - s * 1.6, bot)], role, lw=0.9)

fig, ax = canvas(80)
text(ax, 44, 74, r'$a=2+i,\ b=i$', 'encre', 's')
box(ax, 2, 53, 12, 10, 'fixe', label='$1$'); arrow(ax, (15, 58), (31, 58), 'varie'); text(ax, 23, 62.5, r'$b_L$', 'varie', 's')
box(ax, 33, 53, 12, 10, 'sujet', label='$i$'); arrow(ax, (46, 58), (62, 58), 'varie'); text(ax, 54, 62.5, r'$a_L$', 'varie', 's')
box(ax, 63, 53, 23, 10, 'resultat', label=r'$-1+2i$', size='s')
box(ax, 2, 23, 12, 10, 'fixe', label='$1$'); arrow(ax, (15, 28), (61, 28), 'autre'); text(ax, 38, 32.5, r'$(ab)_L$', 'autre', 's')
box(ax, 63, 23, 23, 10, 'resultat', label=r'$-1+2i$', size='s')
text(ax, 74.5, 43, r'$=$', 'resultat', 'l')
text(ax, 44, 8, r'$(ab)x=a(bx)$', 'sujet', 'm')
save(fig, '77-028')
