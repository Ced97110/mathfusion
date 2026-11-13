import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(74)
O = (33, 34); R = 30
c = 0.6; s = 0.8
P = (O[0] + c * R, O[1] + s * R); Q = (O[0] + c * R, O[1] - s * R)
line(ax, [(O[0] + R * math.cos(math.radians(t)), O[1] + R * math.sin(math.radians(t))) for t in range(0, 361, 4)], 'fixe', lw=0.9)
line(ax, [(O[0] - R - 2, O[1]), (O[0] + R + 2, O[1])], 'fixe', lw=0.7)
line(ax, [(O[0], O[1] - R - 2), (O[0], O[1] + R + 2)], 'fixe', lw=0.7)
poly(ax, [O] + [(O[0] + R * math.cos(math.radians(t)), O[1] + R * math.sin(math.radians(t))) for t in list(range(0, 89, 4)) + [90]], 'sujet')
line(ax, [O, P], 'sujet'); line(ax, [P, (P[0], O[1])], 'resultat', lw=2.0)
line(ax, [O, Q], 'limite', dash=True); line(ax, [Q, (Q[0], O[1])], 'limite', lw=2.0)
disc(ax, P[0], P[1], 1.5, 'resultat'); disc(ax, Q[0], Q[1], 1.5, 'limite')
text(ax, O[0] + 0.3 * R, O[1] - 3.5, '0,6', 'sujet', 's')
text(ax, O[0] + 6, O[1] + 4.2, r'$\alpha$ aigu', 'sujet', 's')
text(ax, P[0] + 5, P[1] + 1, r'$\sin\alpha$ = 0,8' + '\ngardé', 'resultat', 's', ha='left')
text(ax, Q[0] + 5, Q[1] - 1, '−0,8\nécarté', 'limite', 's', ha='left')
text(ax, 4, 72, r'$\sin^2\alpha$ = 1 − 0,36 = 0,64', 'encre', 's', ha='left')
save(fig, '34-124')
