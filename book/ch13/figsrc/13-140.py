import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(65)
y = 20
f = numberline(ax, 12, 70, y, -3, 3, 1)
for v, r in [(2, 'sujet'), (3, 'sujet'), (-2, 'varie'), (-3, 'varie')]:
    disc(ax, f(v), y, 1.5, r)
arrow(ax, (f(2), y + 3), (f(-2), y + 3), 'varie', curve=0.4)
arrow(ax, (f(3), y + 3), (f(-3), y + 3), 'varie', curve=0.35)
text(ax, f(0), y + 28, r'$\times (-1)$ retourne la droite', 'varie', 's')
text(ax, 24, 56, r'$2 < 3$', 'sujet', 'l')
text(ax, 64, 56, r'$-2 > -3$', 'varie', 'l')
save(fig, '13-140')
