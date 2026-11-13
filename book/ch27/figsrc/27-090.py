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
fig, ax = canvas(66)
u = 8; A = (8, 12); O = (8 + 3.536 * u, 12); V = (O[0], 12 + 6 * u)
poly(ax, [A, O, V], 'sujet'); rmark(ax, O, -1, 1)
arc(ax, A, 8, 0, 59.49, 'resultat', lw=1.2); text(ax, 17.5, 17.5, r'$\alpha$', 'resultat')
text(ax, V[0], V[1] + 3.5, 'V', 'encre', 's'); text(ax, A[0] - 3, 12, 'A', 'encre', 's'); text(ax, O[0] + 3, 12, 'O', 'encre', 's')
text(ax, 34.5, 36, 'opposé : 6', 'sujet', 's', ha='right'); text(ax, 22, 7.5, 'adjacent ≈ 3,536', 'sujet', 's')
text(ax, 66, 42, r'$\tan\alpha=6\div3{,}536$', 'sujet', 's'); text(ax, 66, 34, r'$\approx1{,}697$', 'sujet', 's')
text(ax, 66, 24, r'$\alpha\approx59{,}49^\circ$', 'resultat', 'm')
save(fig, '27-090')
