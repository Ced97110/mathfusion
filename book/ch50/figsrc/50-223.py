import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 23, 61, r'$n=2$ : 9 éléments', 'encre', 's')
text(ax, 65, 61, r'$n=1$ : 3 éléments', 'encre', 's')
cx = 23
box(ax, cx - 16, 41.5, 32, 9, 'sujet')
for j in range(3):
    for dx in (-11, 0, 11):
        disc(ax, cx + dx, 46 - 8 * j, 3, 'sujet' if j == 0 else 'fixe')
text(ax, cx, 20, 'sous-groupe normal\nde 3 éléments', 'sujet', 's')
text(ax, cx, 8, 'pas simple', 'resultat', 'm')
cx = 65
for dx in (-11, 0, 11):
    disc(ax, cx + dx, 46, 3, 'limite')
text(ax, cx, 34, 'sous-groupes : seulement\n$\{e\}$ et $G$', 'limite', 's')
text(ax, cx, 8, 'simple : contre-exemple', 'limite', 's')
save(fig, '50-223')
