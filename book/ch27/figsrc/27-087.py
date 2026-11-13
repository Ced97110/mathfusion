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
fig, ax = canvas(64)
A, B, C, D = (8, 12), (48, 12), (48, 52), (8, 52); O = (28, 32)
box(ax, 8, 12, 40, 40, 'sujet')
line(ax, [A, C], 'fixe', dash=True); line(ax, [B, D], 'fixe', dash=True)
line(ax, [O, A], 'varie', lw=1.6)
disc(ax, O[0], O[1], 1.2, 'resultat')
text(ax, 28, 36.5, 'O', 'resultat', weight='bold')
for s, p, dx, dy in [('A', A, -3, -2.5), ('B', B, 3, -2.5), ('C', C, 3, 2.5), ('D', D, -3, 2.5)]: text(ax, p[0] + dx, p[1] + dy, s, 'encre', 's')
text(ax, 28, 7, 'carré de 5 cm', 'sujet', 's')
text(ax, 21, 22, r'$\mathrm{OA}\approx3{,}536$', 'varie', 's')
text(ax, 68, 44, 'diagonales', 'fixe', 's'); text(ax, 68, 39, r'$\approx7{,}07$ cm', 'fixe', 's')
text(ax, 68, 28, 'se croisent', 'resultat', 's'); text(ax, 68, 23, 'en O', 'resultat', 's')
save(fig, '27-087')
