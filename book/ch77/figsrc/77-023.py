import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def mat(ax, x, y, rows, role="sujet", rh=5.6, hw=8, size="m"):
    n = len(rows); top = y + n * rh / 2 + 0.4; bot = y - n * rh / 2 - 0.4
    for i, r in enumerate(rows):
        text(ax, x, y + n * rh / 2 - rh * (i + 0.5), r, role, size)
    for s in (-1, 1):
        xx = x + s * hw
        line(ax, [(xx - s * 1.6, top), (xx, top), (xx, bot), (xx - s * 1.6, bot)], role, lw=0.9)

fig, ax = canvas(54)
for ylab, ybox, lab, b1, b2, res in ((49, 34, r'somme : $x=1,\ y=i$', r'$(2+i)(1+i)$', r'$(2+i)+(-1+2i)$', r'$1+3i$'),
                                    (27, 12, r'scalaire : $c=3,\ x=i$', r'$(2+i)(3i)$', r'$3(-1+2i)$', r'$-3+6i$')):
    text(ax, 44, ylab, lab, 'encre', 's')
    box(ax, 2, ybox, 29, 10, 'sujet', label=b1, size='s'); text(ax, 34, ybox + 5, '$=$', 'encre', 'm')
    box(ax, 37, ybox, 29, 10, 'autre', label=b2, size='s'); text(ax, 69, ybox + 5, '$=$', 'encre', 'm')
    box(ax, 72, ybox, 14, 10, 'resultat', label=res, size='s')
save(fig, '77-023')
