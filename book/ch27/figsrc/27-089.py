import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arc(ax, c, r, a0, a1, role, lw=0.9):
    pts = [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / 24)), c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / 24))) for i in range(25)]
    line(ax, pts, role, lw)
def rmark(ax, p, dx, dy, s=2.2, role='fixe'):
    line(ax, [(p[0] + dx * s, p[1]), (p[0] + dx * s, p[1] + dy * s), (p[0], p[1] + dy * s)], role, lw=0.7)
def pyr(ax, o, u, role='sujet', a=5, h=6):
    P = lambda x, y, z: iso(x, y, z, o, u)
    B, C, D, A = P(0, 0, 0), P(a, 0, 0), P(a, a, 0), P(0, a, 0)
    O, V, M = P(a / 2, a / 2, 0), P(a / 2, a / 2, h), P(a / 2, 0, 0)
    poly(ax, [B, C, D, A], 'fixe')
    poly(ax, [A, B, V], role); poly(ax, [B, C, V], role)
    for p, q in [(C, D), (D, A), (V, D)]: line(ax, [p, q], 'fixe', lw=0.6, dash=True)
    line(ax, [O, V], 'fixe', lw=0.6, dash=True)
    return dict(A=A, B=B, C=C, D=D, O=O, V=V, M=M)
fig, ax = canvas(72)
s = 28; y0 = 22
text(ax, 25, 58, 'V au-dessus de O', 'resultat', 's'); text(ax, 66, 58, 'V au-dessus de B', 'limite', 's')
x0 = 8
box(ax, x0, y0, s, s, 'fixe')
O = (x0 + s / 2, y0 + s / 2)
for p in [(x0, y0), (x0 + s, y0), (x0 + s, y0 + s), (x0, y0 + s)]: line(ax, [O, p], 'resultat', lw=1.4)
disc(ax, O[0], O[1], 1, 'resultat'); text(ax, O[0] + 3, O[1] + 3, 'O', 'resultat', 's')
text(ax, 25, 10, 'chaque projeté', 'resultat', 's'); text(ax, 25, 5.5, '= demi-diagonale', 'resultat', 's')
x1 = 52
box(ax, x1, y0, s, s, 'fixe')
B = (x1 + s, y0)
for p in [(x1, y0), (x1 + s, y0 + s), (x1, y0 + s)]: line(ax, [B, p], 'limite', lw=1.4)
disc(ax, B[0], B[1], 1, 'limite'); text(ax, B[0] - 2.5, B[1] + 3, 'B', 'limite', 's')
text(ax, x1 + 14, y0 - 3.5, 'BA = 5', 'limite', 's'); text(ax, x1 + s - 4.5, y0 + 19, 'BC = 5', 'limite', 's', rot=90)
text(ax, x1 + 11, y0 + 24, 'BD ≈ 7,07', 'limite', 's')
text(ax, 66, 10, 'aucune demi-diagonale', 'limite', 's')
save(fig, '27-089')
