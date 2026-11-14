import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(62)
y = 30
f = numberline(ax, 8, 72, y, 0, 6)
arrow(ax, (f(0), y + 1.5), (f(2), y + 1.5), 'varie', curve=-0.45); text(ax, f(1), y + 8.5, r'$+2$', 'varie', 's')
arrow(ax, (f(2), y + 1.5), (f(5), y + 1.5), 'varie', curve=-0.45); text(ax, f(3.5), y + 11, r'$+3$', 'varie', 's')
arrow(ax, (f(0), y + 1.5), (f(5), y + 1.5), 'resultat', curve=-0.6); text(ax, f(2.5), y + 21, r'$+5$', 'resultat', 's')
arrow(ax, (f(5), 15), (f(3), 15), 'limite')
text(ax, f(4), 10, '−2 : pas un entier naturel', 'limite', 's')
save(fig, '44-005')
