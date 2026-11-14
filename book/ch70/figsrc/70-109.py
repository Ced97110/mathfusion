import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
s, ox, oy = 11.5, 30.0, 40.0
P = lambda x, y: (ox + s * x, oy + s * y)
r3 = 3 ** 0.5
disc(ax, *P(0, 0), 2 * s, 'sujet', fill=False, lw=1.2)
line(ax, [P(t / 20, (t / 20) ** 2 - 2) for t in range(-40, 41)], 'varie', lw=1.2)
line(ax, [P(-1.1, -2), P(1.1, -2)], 'fixe', lw=0.9, dash=True)
for (a, b, n, dx, dy) in [(-r3, 1, 'A', -3, 2.5), (r3, 1, 'B', 3, 2.5), (0, -2, 'C', 0, -4)]:
    disc(ax, *P(a, b), 1.3, 'resultat')
    text(ax, P(a, b)[0] + dx, P(a, b)[1] + dy, n, 'resultat', 'm')
text(ax, 71, 62, r'$x^2(x^2-3)$', 'sujet', 'l')
text(ax, 71, 52, r'$x^2$', 'varie', 'l')
text(ax, 71, 46, 'racine double 0', 'varie', 's')
text(ax, 71, 41, 'en $C$ : tangentes', 'varie', 's')
text(ax, 71, 28, r'$\pm\sqrt{3}$', 'resultat', 'm')
text(ax, 71, 22, 'racines simples', 'resultat', 's')
text(ax, 71, 17, 'en $A$, $B$ : traversée', 'resultat', 's')
save(fig, '70-109')
