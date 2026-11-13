import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from math import cos, sin, radians

u = 0.019
fig, ax = canvas(72)
O = (41, 34)
AHd, hh = 1796.0, 2420.0
th = radians(146.8)
G = lambda x, y, z=0: iso(x, y, z, O, u)
A = G(0, 0); B = G(1000, 0)
hx, hy = AHd * cos(th), -AHd * sin(th)          # pied H du ballon, dans le plan du sol
H = G(hx, hy); S = G(hx, hy, hh)
# le sol : un grand losange gris sous les deux triangles
poly(ax, [G(-1650, -1100), G(1150, -1100), G(1150, 350), G(-1650, 350)], 'fixe')
text(ax, G(1000, -950)[0] - 2, G(1000, -950)[1] + 2, 'sol', 'fixe', 's')
poly(ax, [A, B, H], 'sujet'); line(ax, [A, B, H, A], 'sujet', 1.0)          # triangle horizontal (sol)
poly(ax, [A, H, S], 'autre'); line(ax, [A, S, H], 'autre', 1.0)             # triangle vertical
line(ax, [A, H], 'resultat', 2.4); line(ax, [H, S], 'resultat', 2.4)
# angle droit en H entre le sol et la verticale
disc(ax, S[0], S[1], 1.3, 'resultat'); text(ax, S[0], S[1] + 4, 'ballon', 'resultat', 's')
for p, nm, dx, dy in ((A, 'A', 3, -2.5), (B, 'B', 3, 2.5), (H, 'H', 0, -3.8)):
    disc(ax, p[0], p[1], 1.0, 'encre'); text(ax, p[0] + dx, p[1] + dy, nm, 'encre', 'm')
ya = H[1] + 12.3
xa = H[0] + (A[0] - H[0]) * (ya - H[1]) / (A[1] - H[1])
line(ax, [(H[0] - 3, ya), (xa, ya)], 'resultat', 0.7)
text(ax, H[0] - 3.5, ya, 'AH ≈ 1796 m', 'resultat', 's', ha='right', weight='bold')
text(ax, S[0] - 2.8, (H[1] + S[1]) / 2 + 12, 'h ≈ 2420 m', 'resultat', 's', ha='right', weight='bold')
cH = ((A[0] + B[0] + H[0]) / 3, (A[1] + B[1] + H[1]) / 3)
cV = ((A[0] + H[0] + S[0]) / 3, (A[1] + H[1] + S[1]) / 3)
line(ax, [(62, 14), cH], 'sujet', 0.7); disc(ax, cH[0], cH[1], 0.8, 'sujet')
text(ax, 73, 11, 'triangle\nhorizontal (sol)', 'sujet', 's', weight='bold')
line(ax, [(62, 58), cV], 'autre', 0.7); disc(ax, cV[0], cV[1], 0.8, 'autre')
text(ax, 73, 61, 'triangle vertical\n(plan debout)', 'autre', 's', weight='bold')
save(fig, '38-072')
