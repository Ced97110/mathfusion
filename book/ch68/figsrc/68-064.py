import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 13, 52, r'$\mathbb{F}_2$', 'sujet', 'xl')
arrow(ax, (22, 52), (35, 52), 'fixe')
for x, b in [(43, '0'), (59, '1')]:
    disc(ax, x, 52, 5, 'sujet', label=b, size='l')
text(ax, 51, 62, r"l'ensemble $\{0,\,1\}$", 'sujet', 's')
box(ax, 2, 20, 22, 10, 'fixe', label='1 + 1 = 2')
arrow(ax, (25, 25), (33, 25), 'varie')
text(ax, 29, 32, r'$\div\,2$', 'varie', 's')
box(ax, 34, 20, 24, 10, 'varie', label='reste 0')
arrow(ax, (59, 25), (65, 25), 'varie')
box(ax, 66, 20, 20, 10, 'resultat', label='1 + 1 = 0')
save(fig, '68-064')
