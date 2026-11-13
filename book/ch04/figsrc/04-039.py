import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from figstyle import *
fig, ax = canvas(55)

# le signe, la même forme dans les trois écritures (décalée de 28 mm)
base = [(6, 30), (8, 31.5), (11, 22), (14, 38), (28, 38)]
for dx in (0, 28, 56):
    line(ax, [(x + dx, y) for x, y in base], 'sujet', lw=1.5)
text(ax, 64.6, 35, '3', 'sujet', 's', weight='bold')

# le nombre sur lequel on agit : il change d'une écriture à l'autre
for k, n in enumerate(['16', '25', '8']):
    text(ax, 21 + 28 * k, 31, n, 'fixe', 'l')
text(ax, 44, 48, 'le nombre sur lequel on agit', 'fixe', 's')

# le nom « radical » donné au signe commun
text(ax, 44, 13, 'radical', 'sujet', 'l')
text(ax, 44, 7, 'le signe : cherche la racine', 'sujet', 's')
for x in (11, 39, 67):
    line(ax, [(44, 16), (x, 22)], 'sujet', lw=0.6)

save(fig, '04-039')
