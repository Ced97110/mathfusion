import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
x0, w, h = 26, 17, 14
text(ax, x0 + 1.5 * w, 62, '3 termes', 'autre', 's')
text(ax, 2, 40, '2 termes', 'sujet', 's', ha='left')
for j in range(3): text(ax, x0 + w * (j + .5), 56, ['$x^2$', '$7x$', '$2$'][j], 'autre', 's')
for i in range(2):
    y = 40 - i * h
    text(ax, x0 - 5, y + h / 2, ['$x^2$', '$4$'][i], 'sujet', 's')
    for j in range(3): box(ax, x0 + w * j, y, w, h, 'resultat', label=str(3 * i + j + 1), size='l')
text(ax, 44, 20, 'un choix dans chaque groupe', 'encre', 's')
text(ax, 44, 12, r'$2\times 3 = 6$ produits', 'resultat', 'l', weight='bold')
save(fig, '15-120')
