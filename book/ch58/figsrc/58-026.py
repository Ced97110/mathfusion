import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
# les flèches u, v et le point w, avec leurs couples
x0, y0, u = 8, 8, 7.4
P = lambda a, b: (x0 + a * u, y0 + b * u)
for a in range(0, 7):
    line(ax, [P(a, 0), P(a, 5)], 'fixe', lw=0.2)
for b in range(0, 6):
    line(ax, [P(0, b), P(6, b)], 'fixe', lw=0.2)
arrow(ax, P(0, 0), P(2, 1), 'sujet', lw=2.0)
arrow(ax, P(0, 0), P(1, 2), 'autre', lw=2.0)
disc(ax, *P(0, 0), 1.2, 'encre')
disc(ax, *P(5, 4), 1.7, 'resultat')
text(ax, P(0, 0)[0] - 2.5, P(0, 0)[1] - 2.5, 'O', 'encre', 's')
text(ax, P(2, 1)[0] + 2, P(2, 1)[1] - 3.2, r'$u = (2,\ 1)$', 'sujet', 's', ha='left', weight='bold')
text(ax, P(1, 2)[0] - 1.5, P(1, 2)[1] + 3.5, r'$v = (1,\ 2)$', 'autre', 's', ha='left', weight='bold')
text(ax, P(5, 4)[0] - 2.5, P(5, 4)[1] + 3.8, r'$w = (5,\ 4)$', 'resultat', 's', ha='right', weight='bold')
text(ax, 70, 30, 'deux flèches', 'fixe', 's')
text(ax, 70, 25, 'pas alignées', 'fixe', 's')
save(fig, '58-026')
