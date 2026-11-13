import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
R = 14; O = (36, 30)
e1 = (R, 0); e2 = (R * math.cos(math.radians(144)), R * math.sin(math.radians(144)))
V = (O[0] + e1[0], O[1] + e1[1]); W = (O[0] + e2[0], O[1] + e2[1]); Q = (V[0] + e2[0], V[1] + e2[1])
for i in range(-4, 5):
    for j in range(-4, 5):
        p = (O[0] + i * e1[0] + j * e2[0], O[1] + i * e1[1] + j * e2[1])
        if 3 < p[0] < 85 and 6 < p[1] < 60 and (i, j) not in [(0, 0), (1, 0), (0, 1), (1, 1)]:
            disc(ax, p[0], p[1], 0.8, 'fixe')
line(ax, [V, Q, W], 'fixe', dash=True)
arrow(ax, O, V, 'sujet', lw=1.2); arrow(ax, O, W, 'varie', lw=1.2)
disc(ax, V[0], V[1], 1.5, 'sujet'); disc(ax, W[0], W[1], 1.5, 'varie'); disc(ax, Q[0], Q[1], 1.9, 'resultat')
disc(ax, O[0], O[1], 1.2, 'encre')
text(ax, V[0] + 5, V[1] - 3, r'$v$', 'sujet', 'm')
text(ax, W[0] - 2, W[1] + 4, r'$\rho^2(v)$', 'varie', 's', ha='right')
text(ax, Q[0] + 3, Q[1] + 3.5, r'$Q$', 'resultat', 'l')
text(ax, O[0] - 3, O[1] - 3.5, r'$O$', 'encre', 's')
text(ax, 44, 66, r'points gris : le réseau $L$', 'fixe', 's')
text(ax, 44, 3, r'$Q=v+\rho^2(v)$ est dans $L$', 'resultat', 's')
text(ax, O[0] - 2, O[1] + 5, '144°', 'varie', 's')
save(fig, '74-134')
