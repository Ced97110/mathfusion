import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def mat(ax, x, y, rows, role="sujet", rh=5.6, hw=8, size="m"):
    n = len(rows); top = y + n * rh / 2 + 0.4; bot = y - n * rh / 2 - 0.4
    for i, r in enumerate(rows):
        text(ax, x, y + n * rh / 2 - rh * (i + 0.5), r, role, size)
    for s in (-1, 1):
        xx = x + s * hw
        line(ax, [(xx - s * 1.6, top), (xx, top), (xx, bot), (xx - s * 1.6, bot)], role, lw=0.9)

fig, ax = canvas(62)
for y, op, out, role in ((44, r'$\times(2+i)$', '$2+i$', 'sujet'), (22, r'$\times3$', '$3$', 'autre')):
    box(ax, 3, y - 4.5, 14, 9, 'fixe', label='$1$')
    arrow(ax, (19, y), (52, y), 'varie'); text(ax, 36, y + 4.5, op, 'varie', 's')
    box(ax, 54, y - 4.5, 28, 9, role, label=out)
text(ax, 68, 33, r'$\neq$', 'varie', 'l')
text(ax, 44, 6, r'$a_L(1)=a$', 'sujet', 'l')
save(fig, '77-027')
