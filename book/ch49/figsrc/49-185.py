import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
# left: m = 0
box(ax, 6, 22, 30, 22, 'limite')
disc(ax, 21, 33, 3, 'limite', label='1', size='m')
text(ax, 21, 49, r'$2^0$ = 1 élément', 'limite', 's')
text(ax, 21, 16, r'centre = {1}', 'limite', 'm', weight='bold')
text(ax, 21, 8, r'$m$ = 0 : échec', 'limite', 's')
# right: m = 3
box(ax, 46, 22, 36, 22, 'fixe')
for i in range(8):
    disc(ax, 51 + 4.4 * (i % 4) * 1.55 if False else 51.5 + 8.2 * (i % 4), 38.5 - 10 * (i // 4), 2.6, 'resultat' if i < 2 else 'fixe')
text(ax, 64, 49, r'$2^3$ = 8 éléments', 'fixe', 's')
text(ax, 64, 16, 'centre : 2 éléments', 'resultat', 'm', weight='bold')
text(ax, 64, 8, r'$m \geq 1$ : réussite', 'resultat', 's')
save(fig, '49-185')
