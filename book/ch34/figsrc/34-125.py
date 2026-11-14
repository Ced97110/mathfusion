import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(66)
O = (44, 8); R = 34
P = lambda deg, r=R: (O[0] + r * math.cos(math.radians(deg)), O[1] + r * math.sin(math.radians(deg)))
line(ax, [P(t) for t in range(0, 181, 3)], 'fixe', lw=1.0)
line(ax, [(O[0] - R - 2, O[1]), (O[0] + R + 2, O[1])], 'fixe', lw=0.8)
top = P(90)
line(ax, [O, top], 'resultat', lw=2.2)
disc(ax, top[0], top[1], 1.6, 'resultat')
text(ax, P(0)[0], O[1] - 3.5, '0°', 'fixe', 's'); text(ax, P(180)[0], O[1] - 3.5, '180°', 'fixe', 's')
text(ax, top[0] + 3, top[1] + 3, '90°', 'resultat', 'm', ha='left')
text(ax, O[0] - 2, O[1] + R / 2, r'$\sin(\alpha+\beta)$ = 1', 'resultat', 's', ha='right')
text(ax, O[0] + 3, O[1] + 4, r'$\cos(\alpha+\beta)$ = 0', 'resultat', 's', ha='left')
text(ax, 44, 60, r'$\alpha+\beta$ entre 0° et 180° : un seul point', 'encre', 's')
text(ax, 44, 55, r'$\alpha+\beta=90°$', 'resultat', 'm')
save(fig, '34-125')
