import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
u, O = 9.0, (50, 26)
P = lambda p: iso(p[0], p[1], p[2], O, u)
A, B = (1, 2, 1), (0, 1, -1)
comb = lambda s, t, z=0: (s * A[0] + t * B[0], s * A[1] + t * B[1], s * A[2] + t * B[2] + z)
rng = [(-.6, -.6), (1.2, -.6), (1.2, 1.2), (-.6, 1.2)]
# le point (0,0,1) vérifie -3x+y+z = 1 : le plan décalé est le plan W monté de 1
assert -3 * 0 + 0 + 1 == 1
poly(ax, [P(comb(s, t)) for s, t in rng], 'sujet')
pts = [P(comb(s, t, 1)) for s, t in rng]
line(ax, pts + [pts[0]], 'limite', lw=1.2, dash=True)
disc(ax, *P((0, 0, 0)), 1.0, 'encre')
text(ax, O[0] + 3.5, O[1] - 3, r'$O$', 'encre', 'm')
disc(ax, *P((0, 0, 1)), 1.0, 'limite')
arrow(ax, P((0, 0, 0.15)), P((0, 0, 0.85)), 'varie', lw=1.0)
text(ax, 2, 22, r'$-3x+y+z=0$', 'sujet', 'm', ha='left')
text(ax, 2, 62, r'$-3x+y+z=1$', 'limite', 'm', ha='left')
text(ax, 86, 54, r'ne passe pas par $O$', 'limite', 's', ha='right')
save(fig, '58-131')
