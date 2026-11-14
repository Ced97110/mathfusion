import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
y = 34
f = numberline(ax, 8, 58, y, -3, 1)
disc(ax, f(0), y, 1.7, 'encre')
disc(ax, f(-2), y, 1.9, 'autre'); disc(ax, f(-1), y, 1.9, 'sujet')
arrow(ax, (f(-2), y + 3), (f(-1), y + 3), 'resultat', curve=-0.5)
text(ax, f(-1.5), y + 8, 'plus à droite', 'resultat', 's')
text(ax, 44, y + 15, r'$-1 > -2$', 'resultat', 'l', weight='bold')
brace(ax, f(-2), f(0), y - 6, 'fixe', label='2 unités de $O$')
brace(ax, f(-1), f(0), y - 14, 'fixe', label='1 unité de $O$')
save(fig, '12-014')
