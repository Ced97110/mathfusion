import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
text(ax, 44, 78, r"$(1\ 3)(1\ 2)$ : d'abord $(1\ 2)$, puis $(1\ 3)$", 'encre', 's')
xs = [34, 54, 74]
ys = [62, 38, 14]
def node(x, y, l, role): disc(ax, x, y, 3.6, role, label=l, size='m')
for k in range(3):
    for i in range(3): node(xs[i], ys[k], str(i + 1), 'sujet' if k == 0 else ('fixe' if k == 1 else 'resultat'))
s1 = {1: 2, 2: 1, 3: 3}; s2 = {1: 3, 2: 2, 3: 1}
for a in (1, 2, 3):
    arrow(ax, (xs[a-1], ys[0] - 3.8), (xs[s1[a]-1], ys[1] + 3.8), 'varie')
    arrow(ax, (xs[a-1], ys[1] - 3.8), (xs[s2[a]-1], ys[2] + 3.8), 'autre')
text(ax, 13, 50, r'$(1\ 2)$', 'varie', 'm'); text(ax, 13, 26, r'$(1\ 3)$', 'autre', 'm')
text(ax, 13, 62, 'départ', 'sujet', 's'); text(ax, 13, 14, 'arrivée', 'resultat', 's')
text(ax, 44, 3, r'$1\to2\to3\to1$ : $(1\ 2\ 3)$, paire', 'resultat', 's')
save(fig, '47-166')
