import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(82)
xs = [12 + 14 * i for i in range(6)]
text(ax, 2, 78, 'un seul cas : x = 3', 'varie', 'm', ha='left')
for i, x in enumerate(xs):
    disc(ax, x, 66, 3.4, 'varie' if i == 2 else 'fixe', label=str(i + 1))
box(ax, 14, 46, 60, 9, 'limite', label='vrai pour 3, rien de plus', size='s')
text(ax, 2, 38, r'$x$ quelconque : rien supposé', 'sujet', 'm', ha='left')
for x in xs: disc(ax, x, 28, 3.4, 'resultat')
brace(ax, xs[0] - 3.4, xs[-1] + 3.4, 22, 'resultat', label='tous les éléments')
box(ax, 14, 1, 60, 9, 'resultat', label='vrai pour tous', size='s')
save(fig, '42-283')
