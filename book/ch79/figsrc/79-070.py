import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
y = 22
x = lambda v: 12 + (v - 0.9) / 0.1 * 52
line(ax, [(4, y), (64, y)], 'sujet', lw=2.2)
line(ax, [(64, y - 3), (64, y + 3)], 'sujet', lw=1.2)
line(ax, [(64, y), (82, y)], 'fixe', dash=True)
line(ax, [(7, y - 2), (9, y + 2)], 'fixe'); line(ax, [(9.8, y - 2), (11.8, y + 2)], 'fixe')
for v in (0.9, 0.99, 0.999):
    disc(ax, x(v), y, 1.1, 'autre')
disc(ax, 64, y, 1.9, 'resultat')
text(ax, 4, 15, '0', 'sujet', 's')
text(ax, x(0.9), 29, '0,9', 'autre', 's'); text(ax, x(0.99) - 2, 29, '0,99', 'autre', 's')
text(ax, x(0.999) + 1, 38, '0,999', 'autre', 's')
line(ax, [(x(0.999), y + 2), (x(0.999) + 0.5, 35)], 'autre', lw=0.5)
text(ax, 36, 28, '…', 'autre', 'l')
text(ax, 58, 10, 'seul majorant : 1', 'resultat', 's')
text(ax, 30, 12, '[0, 1]', 'sujet', 'm')
text(ax, 76, 28, 'hors de [0, 1]', 'fixe', 's')
save(fig, '79-070')
