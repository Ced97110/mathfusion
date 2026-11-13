import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(96)
T = lambda p: (2 * p[0] + p[1], p[0] + 3 * p[1])
def place(pts, ox, oy, u): return [(ox + u * x, oy + u * y) for x, y in pts]
# haut : le carré de côté 1 et son image
u = 6.5
sq = [(0, 0), (1, 0), (1, 1), (0, 1)]
poly(ax, place(sq, 12, 62, u), 'sujet'); poly(ax, place([T(p) for p in sq], 50, 62, u), 'resultat')
arrow(ax, (22, 66), (46, 66), 'varie'); text(ax, 34, 70, r'$T$', 'varie', 'm')
text(ax, 15.5, 56, 'aire 1', 'sujet', 's'); text(ax, 65, 56, 'aire 5', 'resultat', 's')
text(ax, 26, 90, r'$(1,0)\to(2,1)$', 'fixe', 's'); text(ax, 26, 85.5, r'$(0,1)\to(1,3)$', 'fixe', 's')
# bas : le logo
import math
blob = [(1.0 + 0.25 * math.sin(3 * a) + 0.12 * math.cos(5 * a)) * 1.0 for a in [i * 2 * math.pi / 40 for i in range(40)]]
b0 = [(r * math.cos(i * 2 * math.pi / 40), r * math.sin(i * 2 * math.pi / 40)) for i, r in enumerate(blob)]
ub = 3.2
poly(ax, place(b0, 14, 26, ub), 'sujet'); poly(ax, place([T(p) for p in b0], 58, 26, ub), 'resultat')
arrow(ax, (24, 26), (44, 26), 'varie'); text(ax, 34, 30, r'$T$', 'varie', 'm')
text(ax, 14, 8, '12 cm²', 'sujet', 'm'); text(ax, 58, 8, '60 cm²', 'resultat', 'm')
save(fig, '76-003')
