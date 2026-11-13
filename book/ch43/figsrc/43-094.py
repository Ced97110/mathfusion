import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
vy = {1: 52, 2: 34, 0: 16}
text(ax, 22, 74, r'$E_f$ : $g$ injective', 'resultat', 's', weight='bold')
text(ax, 66, 74, 'égalité : ' + r'$g$' + ' non injective', 'limite', 's', weight='bold')
for v, y in vy.items(): disc(ax, 44, y, 3.2, 'fixe', label=str(v))
text(ax, 44, 63, r'restes', 'fixe', 's')
for els, v in [([1, 4], 1), ([2, 5], 2), ([3, 6], 0)]:
    y = vy[v]
    box(ax, 2, y - 5, 28, 10, 'sujet', label=f'{els[0]}, {els[1]}', size='s')
    arrow(ax, (31, y), (40.5, y), 'resultat')
    for k, n in enumerate(els):
        yy = y + (4.5 if k == 0 else -4.5)
        disc(ax, 82, yy, 2.9, 'sujet', label=str(n), size='s')
        arrow(ax, (79, yy), (47.5, y), 'limite', lw=0.9)
save(fig, '43-094')
