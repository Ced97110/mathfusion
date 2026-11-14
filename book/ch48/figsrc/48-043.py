import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
xs = [14 + i * 20 for i in range(4)]
text(ax, 4, 74, 'positions du bouton', 'sujet', 's', ha='left')
text(ax, 4, 17, 'rotations du carré', 'autre', 's', ha='left')
for x, n, r in zip(xs, '0123', ['0°', '90°', '180°', '270°']):
    disc(ax, x, 63, 5, 'sujet', label=n, size='m')
    disc(ax, x, 27, 5, 'autre', label=r, size='s')
    arrow(ax, (x, 57.5), (x, 32.5), 'resultat', lw=1.1)
text(ax, 4, 9.5, 'deux départs : deux arrivées', 'resultat', 's', ha='left')
text(ax, 4, 4, 'aucune arrivée oubliée', 'resultat', 's', ha='left')
save(fig, '48-043')
