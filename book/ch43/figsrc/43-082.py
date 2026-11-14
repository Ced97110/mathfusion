import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 44, 66, r'$\nu\ :\ S\to S/E,\ \ a\mapsto\bar{a}$', 'encre', 'xl')
cx = [15, 44, 73]; roles = ['sujet', 'fixe', 'varie']
for x, r in zip(cx, roles):
    box(ax, x - 13, 49, 26, 9, r)
text(ax, 15, 53.5, r'$\nu$', 'sujet', 'l'); text(ax, 44, 53.5, r'$S\to S/E$', 'fixe', 'l'); text(ax, 73, 53.5, r'$a\mapsto\bar{a}$', 'varie', 'l')
for x, r in zip(cx, roles): arrow(ax, (x, 48.5), (x, 41), r)
# 2: départ -> arrivée
box(ax, 32, 22, 10, 9, 'fixe', label=r'$S$'); box(ax, 47, 22, 14, 9, 'sujet', label=r'$S/E$')
arrow(ax, (42.8, 26.5), (46.2, 26.5), 'fixe')
# 3: a -> classe
disc(ax, 66, 26.5, 3, 'varie', label=r'$a$'); box(ax, 76, 22, 10, 9, 'sujet', label=r'$\bar{a}$')
arrow(ax, (69.2, 26.5), (75.2, 26.5), 'varie')
text(ax, 15, 36, 'le nom de la règle', 'sujet', 's'); text(ax, 44, 38, 'départ et arrivée', 'fixe', 's')
text(ax, 73, 38, 'a va sur sa classe', 'varie', 's')
text(ax, 44, 12, 'une ligne : nom, départ, arrivée, règle', 'encre', 's')
save(fig, '43-082')
