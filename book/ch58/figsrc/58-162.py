import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
box(ax, 4, 66, 80, 11, 'sujet', label=r'$3\times(2,\,0)-2\times(3,\,0)=(0,\,0)$')
text(ax, 44, 61, r'pour isoler $(2,\,0)$ : diviser par 3', 'varie', 's')
arrow(ax, (24, 59), (24, 51), 'varie'); arrow(ax, (64, 59), (64, 51), 'varie')
# deux mondes
box(ax, 4, 38, 38, 12, 'resultat', label='fractions : ok')
text(ax, 23, 33, r'$(2,0)=\frac{2}{3}\,(3,0)$', 'resultat', 's')
box(ax, 46, 38, 38, 12, 'limite', label='entiers : non')
text(ax, 65, 33, r'$\frac{2}{3}$ n’est pas entier', 'limite', 's')
# droite graduée : 2/3 entre deux entiers
f = numberline(ax, 52, 76, 18, 0, 1, step=1, arrow_right=False)
disc(ax, f(2 / 3), 18, 1.3, 'limite')
text(ax, f(2 / 3), 24, r'$\frac{2}{3}$', 'limite', 's')
text(ax, 26, 18, 'entre 0 et 1', 'fixe', 's')
text(ax, 44, 6, 'la division sort des entiers', 'fixe', 's')
save(fig, '58-162')
