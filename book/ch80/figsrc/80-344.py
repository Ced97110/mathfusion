import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(66)
xs = {2: 20, 3: 34, 5: 48}
for p, x in xs.items():
    text(ax, x, 58, str(p), 'encre', 'm')
text(ax, 76, 58, 'diviseur', 'resultat', 'm')
rows = [(6, (2, 3)), (10, (2, 5)), (1, ())]
for i, (d, ps) in enumerate(rows):
    y = 46 - 16 * i
    for p, x in xs.items():
        if p in ps: disc(ax, x, y, 4, 'sujet')
        else: disc(ax, x, y, 4, 'fixe', fill=False)
    arrow(ax, (57, y), (66, y), 'varie')
    box(ax, 68, y - 5, 16, 10, 'resultat', label=str(d))
text(ax, 26, 2, 'plein = présent', 'sujet', 's')
text(ax, 62, 2, 'vide = absent', 'fixe', 's')
save(fig, '80-344')
