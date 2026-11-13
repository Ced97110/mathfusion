import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
text(ax, 38, 62, '2', 'varie', 'xl', weight='bold'); text(ax, 47, 62, 'ℤ', 'sujet', 'xl', weight='bold')
arrow(ax, (24, 55), (36, 60), 'varie'); text(ax, 22, 51, 'on multiplie par 2', 'varie', 's')
arrow(ax, (60, 55), (49, 60), 'sujet'); text(ax, 62, 51, 'tous les entiers', 'sujet', 's')
xs = [14, 30, 46, 62]
for x, k in zip(xs, [-1, 0, 1, 2]):
    box(ax, x - 7, 28, 14, 9, 'sujet', label=str(k).replace('-', '−'))
    arrow(ax, (x, 27), (x, 17), 'varie')
    box(ax, x - 7, 6, 14, 9, 'resultat', label=str(2 * k).replace('-', '−'))
text(ax, 78, 22, '× 2', 'varie', 'm')
save(fig, '51-093')
