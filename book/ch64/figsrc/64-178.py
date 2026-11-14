import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(92)
assert 18 ** 2 + 4 * 5 * 27 == 864
text(ax, 44, 88, r"$f^\prime(x)=5x^4-18x^2-27$", 'sujet', 'm')
text(ax, 44, 82.5, r'$u=x^2$ : $5u^2-18u-27=0$', 'varie', 'm')
P = lambda u: 5 * u * u - 18 * u - 27
su, ux0, yz, ky = 9.0, 8, 60, 0.4
line(ax, [(ux0 + su * (u + 2), yz + ky * P(u)) for u in np.linspace(-2, 6, 120)], 'varie', lw=1.1)
line(ax, [(3, yz), (84, yz)], 'fixe', lw=0.5)
um, up = (18 - 864 ** .5) / 10, (18 + 864 ** .5) / 10
disc(ax, ux0 + su * (um + 2), yz, 1.5, 'limite'); disc(ax, ux0 + su * (up + 2), yz, 1.5, 'resultat')
text(ax, 22, 48, 'u < 0 : pas un carré', 'limite', 's')
text(ax, 62, 66, 'u > 0', 'resultat', 's')
arrow(ax, (ux0 + su * (up + 2), 56), (ux0 + su * (up + 2), 34), 'resultat')
text(ax, 67, 45, r'$x=\pm\sqrt{u}$', 'resultat', 's', ha='left')
# trois morceaux
a, b = 6 + 76 * (3.3 - 2.18) / 6.6, 6 + 76 * (3.3 + 2.18) / 6.6
box(ax, 6, 14, a - 6, 12, 'sujet', label='monte', size='s')
box(ax, a, 14, b - a, 12, 'varie', label='descend', size='s')
box(ax, b, 14, 82 - b, 12, 'sujet', label='monte', size='s')
text(ax, a, 8, '−2,18', 'fixe', 's'); text(ax, b, 8, '2,18', 'fixe', 's')
text(ax, 44, 30, '3 morceaux : au plus 3 racines', 'encre', 's')
save(fig, '64-178')
