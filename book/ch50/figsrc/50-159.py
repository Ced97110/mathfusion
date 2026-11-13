import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 44, 66, r'$n_2$ possible ? ($q = 3$)', 'encre', 's')
cx = [58, 78]
for x, v in zip(cx, [1, 3]): box(ax, x - 7, 52, 14, 9, 'sujet', label=rf'$n_2 = {v}$', size='s')
for y, lab in [(40, 'divise 3 ?'), (28, 'impair ?')]:
    text(ax, 4, y, lab, 'fixe', 's', ha='left')
    for x in cx: box(ax, x - 7, y - 4.5, 14, 9, 'resultat', label='oui', size='s')
text(ax, 68, 19.5, 'les deux conviennent', 'resultat', 's')
box(ax, 4, 3, 80, 11, 'varie', label='seul un comptage choisit', size='m', weight='bold')
save(fig, '50-159')
