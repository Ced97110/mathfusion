import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
s = 22
poly(ax, [(6, 46), (6 + s, 46), (6 + s, 46 + s), (6, 46 + s)], 'sujet')
line(ax, [(6, 46), (6 + s, 46 + s)], 'varie', lw=1.4)
text(ax, 17, 72, 'carré', 'sujet', 'm')
e = 24; h = e * math.sqrt(3) / 2
poly(ax, [(52, 46), (52 + e, 46), (52 + e / 2, 46 + h)], 'autre')
line(ax, [(52 + e / 2, 46), (52 + e / 2, 46 + h)], 'varie', lw=1.4)
text(ax, 64, 72, 'triangle équilatéral', 'autre', 'm')
text(ax, 40, 58, 'on coupe', 'varie', 's')
arrow(ax, (17, 43), (17, 36), 'varie')
arrow(ax, (64, 43), (64, 36), 'varie')
poly(ax, [(6, 12), (6 + s, 12), (6 + s, 12 + s)], 'sujet')
text(ax, 17, 6, '45° et 45°', 'sujet', 's')
poly(ax, [(52, 12), (64, 12), (64, 12 + h)], 'autre')
text(ax, 64, 6, '60° et 30°', 'autre', 's')
text(ax, 44, 1.5, '', 'encre', 's')
save(fig, '25-084')
