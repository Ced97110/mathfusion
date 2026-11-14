import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(48)
y = 26
f = numberline(ax, 8, 68, y, 0, 6, 1)
for v in range(6):
    arrow(ax, (f(v) + 0.5, y + 1.5), (f(v + 1) - 0.5, y + 1.5), 'varie', curve=-0.6)
disc(ax, f(0), y, 1.3, 'resultat')
text(ax, 38, 42, '+1 par pas : 1, 2, … 100', 'varie', 'm')
arrow(ax, (f(6), y - 7.5), (f(0), y - 7.5), 'limite', curve=0.0)
text(ax, 38, 9, 'jamais de retour sur 0', 'limite', 's')
save(fig, '51-128')
