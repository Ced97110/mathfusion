import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def mat(ax, x, y, rows, role="sujet", rh=5.6, hw=8, size="m"):
    n = len(rows); top = y + n * rh / 2 + 0.4; bot = y - n * rh / 2 - 0.4
    for i, r in enumerate(rows):
        text(ax, x, y + n * rh / 2 - rh * (i + 0.5), r, role, size)
    for s in (-1, 1):
        xx = x + s * hw
        line(ax, [(xx - s * 1.6, top), (xx, top), (xx, bot), (xx - s * 1.6, bot)], role, lw=0.9)

fig, ax = canvas(62)
box(ax, 24, 50, 40, 9, 'sujet', label=r'$a=2+i$ fixé')
for y, xin, xout in ((34, '$1$', '$2+i$'), (16, '$i$', '$-1+2i$')):
    box(ax, 6, y - 4.5, 18, 9, 'fixe', label=xin)
    arrow(ax, (26, y), (60, y), 'varie'); text(ax, 43, y + 4.5, r'$a_L$', 'varie', 'm')
    box(ax, 62, y - 4.5, 24, 9, 'resultat', label=xout)
text(ax, 44, 4, r'$a_L:\ x\mapsto ax$', 'varie', 'l')
save(fig, '77-021')
