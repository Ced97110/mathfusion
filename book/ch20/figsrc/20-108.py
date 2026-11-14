import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
ox, oy, u = 2, 8, 7
m = lambda x, y: (ox + (x + 1) * u, oy + (y + 1) * u)
poly(ax, [m(-1, -1), m(7, -1), m(7, 5), m(-1, 5)], 'fixe', fill=False)
poly(ax, [m(0, 0), m(6, 0), m(0, 4)], 'sujet')
for p in [(0, 0), (6, 0), (0, 4)]:
    c = m(*p); disc(ax, c[0], c[1], 1.5, 'varie')
text(ax, 70, 26, 'sommets', 'varie', 'm', weight='bold')
text(ax, 70, 21.5, '(équations)', 'varie', 's')
arrow(ax, (62, 21), (m(6, 0)[0] + 2, m(6, 0)[1] + 0.5), 'varie')
text(ax, 70, 44, 'région', 'sujet', 'm', weight='bold')
text(ax, 70, 39.5, '(inéquations)', 'sujet', 's')
arrow(ax, (60, 40), m(2, 1.8), 'sujet')
save(fig, '20-108')
