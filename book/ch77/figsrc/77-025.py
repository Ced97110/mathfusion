import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def mat(ax, x, y, rows, role="sujet", rh=5.6, hw=8, size="m"):
    n = len(rows); top = y + n * rh / 2 + 0.4; bot = y - n * rh / 2 - 0.4
    for i, r in enumerate(rows):
        text(ax, x, y + n * rh / 2 - rh * (i + 0.5), r, role, size)
    for s in (-1, 1):
        xx = x + s * hw
        line(ax, [(xx - s * 1.6, top), (xx, top), (xx, bot), (xx - s * 1.6, bot)], role, lw=0.9)

fig, ax = canvas(70)
rows = [(58, '$2$', r'$\times2$'), (44, '$3$', r'$\times3$'), (28, '$2+3$', r'$\times5$'), (14, r'$2\times3$', r'$\times6$')]
for y, a, op in rows:
    box(ax, 2, y - 4.5, 20, 9, 'sujet', label=a)
    arrow(ax, (24, y), (38, y), 'varie')
    box(ax, 40, y - 4.5, 22, 9, 'varie', label=op)
line(ax, [(64, 58), (65.5, 58), (65.5, 44), (64, 44)], 'resultat')
text(ax, 68, 51, 'injectif', 'resultat', 's', ha='left')
text(ax, 65, 28, 'somme', 'resultat', 's', ha='left'); text(ax, 65, 14, 'produit', 'resultat', 's', ha='left')
save(fig, '77-025')
