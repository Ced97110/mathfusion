import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 44, 66, 'nombres de quarts de tour', 'fixe', 's')
xs = [8 + i * 13 for i in range(6)]
for i, x in enumerate(xs): box(ax, x, 48, 11, 9, 'fixe', label=str(i))
ys = [20 + i * 15 for i in range(4)]
px = [22 + i * 15 for i in range(4)]
box(ax, 14, 14, 64, 20, 'resultat', fill=False, dash=True)
for i, x in enumerate(px): disc(ax, x + 5, 24, 4.5, 'resultat', label=str(i))
for i, x in enumerate(xs): arrow(ax, (x + 5.5, 47), (px[i % 4] + 5, 29.5), 'varie')
text(ax, 44, 8, r'$\mathrm{im}\ f$ : les 4 positions', 'resultat', 's')
save(fig, '48-030')
