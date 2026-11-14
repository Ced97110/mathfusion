import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(62)
y0, y1 = 14.0, 44.0
x = 30.0
poly(ax, [(4, y0), (84, y0), (84, y1), (4, y1)], 'fixe')
line(ax, [(4, y0), (84, y0)], 'fixe', lw=1.2)
line(ax, [(4, y1), (84, y1)], 'fixe', lw=1.2)
arrow(ax, (x, y0 + 1.5), (x, y1 - 1.5), 'sujet', lw=1.5, both=True)
disc(ax, x, y0, 1.4, 'sujet'); disc(ax, x, y1, 1.4, 'sujet')
line(ax, [(x + 2.4, y0), (x + 2.4, y0 + 2.4), (x, y0 + 2.4)], 'encre', lw=0.7)
text(ax, x, y0 - 4, 'H', 'sujet', 'm')
text(ax, x, y1 + 4, 'P', 'sujet', 'm')
text(ax, x + 4, (y0 + y1) / 2, 'w', 'sujet', 'xl', ha='left', weight='bold')
text(ax, 62, (y0 + y1) / 2 + 3, '= longueur PH', 'sujet', 's')
text(ax, 62, (y0 + y1) / 2 - 3, 'pas encore calculée', 'fixe', 's')
text(ax, 72, y1 + 4, 'autre rive', 'fixe', 's')
text(ax, 72, y0 - 4, 'votre rive', 'fixe', 's')
save(fig, '38-047')
