import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
box(ax, 2, 40, 84, 18, 'fixe', fill=False, dash=True)
text(ax, 84, 54, "liste d'axiomes", 'sujet', 'm', ha='right')
text(ax, 84, 48, 'Peano, 1889', 'fixe', 's', ha='right')
for y, s in ((54, '1 · il y a un début'), (49, '2 · suivants tous différents'), (44, "3 · tout s'atteint du début")):
    text(ax, 4, y, s, 'encre', 's', ha='left')
xs = [4 + 11 * i for i in range(7)]
for i, x in enumerate(xs):
    box(ax, x, 24, 7, 7, 'sujet' if i == 0 else 'fixe', r=0.6)
text(ax, 82, 27.5, '…', 'fixe', 'm')
for x in xs[:-1]:
    arrow(ax, (x + 7.3, 27.5), (x + 10.7, 27.5), 'varie')
disc(ax, 7.5, 36, 2.2, 'sujet', label='1', size='s')
disc(ax, 35, 36, 2.2, 'varie', label='2', size='s')
brace(ax, 4, 77, 22, 'resultat')
disc(ax, 40.5, 15, 2.2, 'resultat', label='3', size='s')
save(fig, '01-026')
