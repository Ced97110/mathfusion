import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(66)
xs = [34, 46, 58]
for k, x in enumerate(xs):
    text(ax, x, 58, str(k + 1), 'encre', 'm')
rows = [(r'$\{1,3\}$', (1, 0, 1)), (r'$\emptyset$', (0, 0, 0)), (r'$\{1,2,3\}$', (1, 1, 1))]
for i, (s, bits) in enumerate(rows):
    y = 46 - 16 * i
    text(ax, 4, y, s, 'sujet', 'm', ha='left')
    for x, b in zip(xs, bits):
        if b: disc(ax, x, y, 4, 'sujet')
        else: disc(ax, x, y, 4, 'fixe', fill=False)
    arrow(ax, (65, y), (71, y), 'varie')
    text(ax, 79, y, ''.join(map(str, bits)), 'resultat', 'l')
text(ax, 28, 4, 'plein = 1', 'sujet', 's')
text(ax, 58, 4, 'vide = 0', 'fixe', 's')
save(fig, '80-359')
