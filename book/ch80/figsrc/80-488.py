import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
xs = [3, 31, 59]
for x, t in zip(xs, ['groupe', 'anneau', 'module']):
    box(ax, x, 56, 26, 9, 'sujet', label=t, weight='bold')
    box(ax, x, 12, 26, 40, 'fixe')
for x in xs[:2]: text(ax, x + 13, 44, 'nombres entiers', 'encre', 's')
text(ax, 16, 32, '+', 'sujet', 'xl', weight='bold'); text(ax, 44, 32, r'$+$ et $\times$', 'sujet', 'l', weight='bold')
text(ax, 16, 18, '1 opération', 'fixe', 's'); text(ax, 44, 18, '2 opérations', 'fixe', 's')
text(ax, 72, 44, 'flèches du plan', 'encre', 's')
arrow(ax, (63, 20), (69, 24.5), 'sujet'); arrow(ax, (63, 20), (78, 31.3), 'varie')
text(ax, 68, 15.5, 'flèche', 'sujet', 's'); text(ax, 72, 37, 'nombre × flèche', 'varie', 's')
text(ax, 44, 5, 'un anneau agit sur un groupe', 'fixe', 's')
save(fig, '80-488')
