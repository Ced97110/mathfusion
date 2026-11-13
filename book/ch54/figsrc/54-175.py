import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
box(ax, 6, 54, 30, 11, 'varie', label=r'$4u+6v$')
text(ax, 21, 49.5, r'$u$, $v$ entiers', 'fixe', 's')
text(ax, 62, 59.5, 'donne les multiples de 2', 'encre', 's')
f = numberline(ax, 6, 76, 34, -6, 8, 1, arrow_right=False, every=2)
for v in range(-6, 9, 2):
    disc(ax, f(v), 34, 1.6, 'sujet')
arrow(ax, (21, 53), (f(-2), 37.5), 'varie')
arrow(ax, (44, 26), (44, 18), 'sujet')
box(ax, 10, 6, 68, 11, 'resultat', label=r'$(2)$ : un seul générateur')
save(fig, '54-175')
