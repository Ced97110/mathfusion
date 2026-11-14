import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
box(ax, 2, 56, 30, 10, 'autre', label=r'$(-5)\times3$')
box(ax, 56, 56, 30, 10, 'sujet', label=r'$3\times(-5)$')
arrow(ax, (33, 61), (55, 61), 'varie', both=True)
text(ax, 44, 66.5, 'échanger', 'varie', 's')
y = 28
f = numberline(ax, 6, 78, y, -16, 1, labels=False)
text(ax, f(0), y - 3.6, r'$0$', 'fixe')
text(ax, f(-15), y - 3.6, r'$-15$', 'resultat')
disc(ax, f(-15), y, 1.8, 'resultat')
for a in (0, -5, -10):
    arrow(ax, (f(a) - 0.8, y + 2.5), (f(a - 5) + 0.8, y + 2.5), 'varie', curve=0.7)
    text(ax, f(a - 2.5), y + 12, r'$-5$', 'varie', 's')
text(ax, 44, 8, r'$(-5)\times3=-15$', 'resultat', 'l')
save(fig, '13-073')
