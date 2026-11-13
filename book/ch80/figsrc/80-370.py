import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
xs = [18, 44, 70]
text(ax, 44, 75, 'personnes', 'fixe', 's')
for i, x in enumerate(xs):
    disc(ax, x, 62, 6, 'sujet', label=str(i + 1), size='l')
    box(ax, x - 10, 18, 20, 10, 'autre', label=f'chapeau de {i + 1}', size='s')
for i in range(3):
    j = (i + 1) % 3
    arrow(ax, (xs[i], 55.5), (xs[j], 29), 'varie')
text(ax, 44, 8, 'personne ne reçoit le sien', 'resultat', 'm')
save(fig, '80-370')
