import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
px = [6 + i * 4.4 for i in range(12)]
rows = [(48, 'sujet', ['0', '22'], r'$0+H$', 'heures paires : $H$'), (26, 'varie', ['1', '23'], r'$1+H$', 'heures impaires')]
for y, role, ends, name, cap in rows:
    for x in px:
        disc(ax, x, y, 1.7, role)
    text(ax, px[0], y - 4.6, ends[0], role, 's')
    text(ax, px[-1], y - 4.6, ends[1], role, 's')
    text(ax, 31, y + 6, cap, role, 's')
    arrow(ax, (px[-1] + 3, y), (60, y), role)
    box(ax, 62, y - 5, 22, 10, role, label=name, size='m')
text(ax, 44, 7, r'$G/H$ : $24/12=2$ éléments', 'resultat', 'm', weight='bold')
save(fig, '64-048')
