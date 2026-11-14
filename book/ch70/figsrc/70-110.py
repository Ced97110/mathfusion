import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
s, ox, oy = 14.0, 44.0, 44.0
P = lambda x, y: (ox + s * x, oy + s * y)
disc(ax, *P(0, 0), 2 * s, 'sujet', fill=False, lw=1.2)
line(ax, [P(t / 20, (t / 20) ** 2 - 2) for t in range(-40, 41)], 'fixe', lw=0.9, dash=True)
line(ax, [P(t / 20, (t / 20) ** 2 - 1) for t in range(-38, 39)], 'varie', lw=1.3)
arrow(ax, P(0, -2), P(0, -1.1), 'varie', lw=1.2)
text(ax, P(1.2, -1.55)[0], P(1.2, -1.55)[1], r'$e=1$', 'varie', 's')
u = (1 + 13 ** 0.5) / 2
x = u ** 0.5
for sx in (-1, 1):
    disc(ax, *P(sx * x, u - 1), 1.3, 'resultat')
text(ax, 44, 8, '2 points communs', 'resultat', 'm')
text(ax, 14, 24, 'avant : $e=0$', 'fixe', 's')
text(ax, 74, 24, r'$y=x^2-1$', 'varie', 's')
save(fig, '70-110')
