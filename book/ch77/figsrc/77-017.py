import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def mat(ax, x, y, rows, role="sujet", rh=5.6, hw=8, size="m"):
    n = len(rows); top = y + n * rh / 2 + 0.4; bot = y - n * rh / 2 - 0.4
    for i, r in enumerate(rows):
        text(ax, x, y + n * rh / 2 - rh * (i + 0.5), r, role, size)
    for s in (-1, 1):
        xx = x + s * hw
        line(ax, [(xx - s * 1.6, top), (xx, top), (xx, bot), (xx - s * 1.6, bot)], role, lw=0.9)

fig, ax = canvas(70)
text(ax, 44, 65, r'$3+4i = 3\times1+4\times i$', 'sujet', 'm')
box(ax, 3, 46, 39, 11, 'varie', label=r'image de 1 : $2+i$', size='s')
box(ax, 46, 46, 39, 11, 'varie', label=r'image de $i$ : $-1+2i$', size='s')
arrow(ax, (22.5, 46), (22.5, 34), 'varie'); text(ax, 25, 40, r'$\times3$', 'varie', 's', ha='left')
arrow(ax, (65.5, 46), (65.5, 34), 'varie'); text(ax, 68, 40, r'$\times4$', 'varie', 's', ha='left')
box(ax, 3, 23, 39, 11, 'sujet', label=r'$6+3i$')
box(ax, 46, 23, 39, 11, 'sujet', label=r'$-4+8i$')
text(ax, 44, 28.5, r'$+$', 'encre', 'l')
box(ax, 22, 3, 44, 11, 'resultat', label=r'$2+11i$')
arrow(ax, (22.5, 23), (36, 14), 'resultat'); arrow(ax, (65.5, 23), (52, 14), 'resultat')
save(fig, '77-017')
