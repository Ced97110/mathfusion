import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
s, ox, oy = 14.0, 44.0, 52.0
P = lambda x, y: (ox + s * x, oy + s * y)
r3 = 3 ** 0.5
disc(ax, *P(0, 0), 2 * s, 'sujet', fill=False, lw=1.2)
line(ax, [P(t / 20, (t / 20) ** 2 - 2) for t in range(-40, 41)], 'varie', lw=1.2)
ay = 14
line(ax, [(6, ay), (82, ay)], 'fixe', lw=0.8)
for (a, b, n) in [(-r3, 1, 'A'), (r3, 1, 'B'), (0, -2, 'C')]:
    line(ax, [P(a, b), P(a, 0), (P(a, 0)[0], ay)] if False else [P(a, b), (P(a, b)[0], ay)], 'resultat', lw=0.7, dash=True)
    disc(ax, *P(a, b), 1.3, 'resultat')
    dx, dy = (-3.2, 2.2) if n == 'A' else ((3.2, 2.2) if n == 'B' else (0, -4))
    text(ax, P(a, b)[0] + dx, P(a, b)[1] + dy, n, 'resultat', 'm')
    ax.plot([P(a, 0)[0]] * 2, [ay - 1, ay + 1], color=COL['fixe'], lw=0.8)
text(ax, P(-r3, 0)[0], ay - 4, r'$-\sqrt{3}$', 'resultat', 's')
text(ax, P(0, 0)[0], ay - 4, '0 (double)', 'resultat', 's')
text(ax, P(r3, 0)[0], ay - 4, r'$\sqrt{3}$', 'resultat', 's')
text(ax, 44, 4, 'racines de $x^2(x^2-3)$', 'sujet', 's')
save(fig, '70-106')
