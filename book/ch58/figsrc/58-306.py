import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
u = 5.0; O = (30, 33)
A = (1, 2, 1)
P = lambda t: iso(t * A[0], t * A[1], t * A[2], O, u)
for d in ((1, 0, 0), (0, 1, 0), (0, 0, 1)):
    arrow(ax, O, iso(d[0] * 2, d[1] * 2, d[2] * 2, O, u), 'fixe', lw=0.5)
line(ax, [P(-1.1), P(2.1)], 'sujet', lw=1.2)
arrow(ax, P(0), P(1), 'varie', lw=1.8)
disc(ax, O[0], O[1], 1.1, 'encre')
for t in (-1, 2):
    disc(ax, P(t)[0], P(t)[1], 0.9, 'sujet')
text(ax, O[0] - 9, O[1] - 4, r'$O = 0\cdot a$', 'encre', 's')
text(ax, P(1)[0] + 13, P(1)[1] + 1, r'$a=(1,\ 2,\ 1)$', 'varie', 's')
text(ax, P(2)[0] + 8, P(2)[1], r'$2a$', 'sujet', 's')
text(ax, P(-1)[0] + 9, P(-1)[1], r'$-a$', 'sujet', 's')
text(ax, 62, 58, 'droite des multiples de a', 'sujet', 's')
box(ax, 50, 4, 36, 9, 'resultat', label='base : (a), dim = 1', size='s')
save(fig, '58-306')
