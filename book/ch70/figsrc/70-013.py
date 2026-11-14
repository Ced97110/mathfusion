import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
s, ox, oy = 8.0, 28.0, 30.0
P = lambda x, y: (ox + s * x, oy + s * y)
r3 = 3 ** 0.5
arrow(ax, P(-2.6, 0), P(2.7, 0), 'fixe', lw=0.6)
arrow(ax, P(0, -2.5), P(0, 3.6), 'fixe', lw=0.6)
disc(ax, *P(0, 0), 2 * s, 'sujet', fill=False, lw=1.3)
line(ax, [P(t / 20, (t / 20) ** 2 - 2) for t in range(-46, 47)], 'varie', lw=1.3)
for name, a, b, dx, dy in [('A', -r3, 1, -3.2, 3.2), ('B', r3, 1, -3.2, 3.2), ('C', 0, -2, 3.2, -2.5)]:
    disc(ax, *P(a, b), 1.2, 'resultat')
    text(ax, P(a, b)[0] + dx, P(a, b)[1] + dy, name, 'resultat', 'm', weight='bold')
disc(ax, *P(2, 0), 1.1, 'sujet')
disc(ax, *P(2, 2), 1.1, 'varie')
text(ax, 50, 29, r'$f=0$ seul', 'sujet', 's', ha='left')
text(ax, 47, 47, r'$g=0$ seul', 'varie', 's', ha='left')
text(ax, 62, 8, r'$A$, $B$, $C$ : $f=0$ et $g=0$', 'resultat', 's')
save(fig, '70-013')
