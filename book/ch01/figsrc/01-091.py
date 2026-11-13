import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 44, 75, '41 450 arrondi', 'sujet', 'm')
# (y, libellé, x du point, bout gauche, bout droit, rôle des bouts, rôle du bout gauche)
segs = [(60, 'à la dizaine de mille', 30.4, '40 000', '50 000', 65),
        (38, 'au millier', 48.1, '41 000', '42 000', 43),
        (16, 'à la centaine', 51.0, '41 400', '41 500', 21)]
for k, (y, lab, xp, g, d, ylab) in enumerate(segs):
    line(ax, [(22, y), (80, y)], 'fixe')
    for x in (22, 80):
        line(ax, [(x, y - 1.2), (x, y + 1.2)], 'fixe', lw=0.8)
    text(ax, 4, ylab, lab, 'fixe', 's', ha='left')
    disc(ax, xp, y, 1.3, 'sujet')
    if k < 2:
        text(ax, 22, y - 5, g, 'resultat', 's')
        text(ax, 80, y - 5, d, 'fixe', 's')
        arrow(ax, (xp, y + 2), (22, y + 2), 'resultat')
    else:
        text(ax, 22, y - 5, g, 'varie', 's')
        text(ax, 80, y - 5, d, 'varie', 's')
        arrow(ax, (51, 18), (22, 18), 'varie')
        arrow(ax, (51, 18), (80, 18), 'varie')
        text(ax, 51, 22, 'à égale distance', 'varie', 's')
save(fig, '01-091')
