import sys, os, math; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(82)
ox, oy, u = 8, 44, 17
X = lambda x: ox + u * x
Yv = lambda y: oy + u * y
p = lambda x: (x - 2) * (x - 1) * (x - 3)
arrow(ax, (ox - 2, oy), (X(3.95), oy), 'fixe', lw=0.6)
n = 160
up = [(1.5 + 0.5 * math.cos(math.pi * i / n), math.sqrt(max(p(1.5 + 0.5 * math.cos(math.pi * i / n)), 0))) for i in range(n + 1)]
loop = [(X(x), Yv(y)) for x, y in up] + [(X(x), Yv(-y)) for x, y in reversed(up)]
line(ax, loop, 'sujet', lw=1.4)
br = [(3 + 0.8 * (i / n) ** 2, ) for i in range(n + 1)]
bu = [(X(x[0]), Yv(math.sqrt(max(p(x[0]), 0)))) for x in reversed(br)]
bl = [(X(x[0]), Yv(-math.sqrt(max(p(x[0]), 0)))) for x in br]
line(ax, bu + bl, 'sujet', lw=1.4)
for xv, lab, role in ((0.5, '0,5', 'fixe'), (1.5, '1,5', 'varie'), (2.5, '2,5', 'fixe'), (3.4, '3,4', 'varie')):
    line(ax, [(X(xv), Yv(-1.6)), (X(xv), Yv(1.6))], role, lw=1.0, dash=True)
    text(ax, X(xv), Yv(1.85), lab, role, 's')
for v in (1, 2, 3):
    text(ax, X(v), oy - 5.5, str(v), 'fixe', 's')
disc(ax, ox, oy, 1.0, 'fixe')
text(ax, ox - 1.5, oy + 3.5, r'$O$', 'fixe', 's')
line(ax, [(ox, oy), (X(1), oy)], 'resultat', lw=1.6)
disc(ax, X(1), oy, 1.3, 'resultat')
text(ax, X(1) - 3.2, oy + 3.5, r'$P$', 'resultat', 's')
for i, (role, lab, dash) in enumerate([('varie', 'coupe la courbe', True), ('fixe', 'ne coupe pas', True), ('sujet', r'courbe $f=0$', False)]):
    yy = 16 - 6 * i
    line(ax, [(4, yy), (12, yy)], role, lw=1.2, dash=dash)
    text(ax, 14, yy, lab, role, 's', ha='left')
save(fig, '70-135')
