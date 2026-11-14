import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
y = 30
f = numberline(ax, 8, 78, y, -3, 5, labels=False, arrow_right=False)
box(ax, f(-3), 12, f(0) - f(-3) - 0.6, 7, 'autre', label='N')
box(ax, f(0) + 0.6, 12, f(5) - f(0) - 0.6, 7, 'resultat', label='P')
disc(ax, f(-2), y, 2, 'sujet')
poly(ax, [(f(4) - 1.5, y - 1.5), (f(4) + 1.5, y - 1.5), (f(4) + 1.5, y + 1.5), (f(4) - 1.5, y + 1.5)], 'sujet')
arrow(ax, (f(-2), y + 2.2), (f(4), y + 2.4), 'sujet', curve=-0.5)
text(ax, f(0), 25, '0', 'fixe', 's')
text(ax, f(-2), 25, 'a = −2', 'sujet', 's')
text(ax, f(4), 25, 'a² = 4', 'sujet', 's')
text(ax, 44, 50, '(−2) × (−2) = 4', 'varie', 'm')
save(fig, '69-011')
