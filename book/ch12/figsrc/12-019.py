import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
for y, role, lab, out, kind in ((46, 'sujet', 'addition', '13', 'un nombre'), (14, 'autre', 'comparaison', '$8 > 5$', 'une phrase vraie')):
    box(ax, 3, y - 4, 10, 8, 'fixe', label='8')
    box(ax, 15, y - 4, 10, 8, 'fixe', label='5')
    arrow(ax, (27, y), (52, y), role)
    text(ax, 40, y + 4, lab, role, 's')
    box(ax, 54, y - 4.5, 22, 9, role, label=out)
    text(ax, 65, y - 9, kind, role, 's')
line(ax, [(2, 30), (86, 30)], 'fixe', lw=0.5, dash=True)
text(ax, 44, 61, 'deux nombres : que sort-il ?', 'encre', 'm')
save(fig, '12-019')
