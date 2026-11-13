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
O = (42, 12); u = 7.5; V = (42, 12 + 6 * u); A = (42 - 3.536 * u, 12); M = (42 + 2.5 * u, 12)
poly(ax, [O, A, V], 'sujet'); poly(ax, [O, M, V], 'varie')
rmark(ax, O, -1, 1); rmark(ax, O, 1, 1)
arc(ax, A, 7, 0, 59.49, 'sujet', lw=1.1); arc(ax, M, 6, 112.62, 180, 'varie', lw=1.1)
text(ax, 26.5, 15.5, r'$\alpha$', 'sujet'); text(ax, 52.5, 15.5, r'$\beta$', 'varie')
text(ax, V[0], V[1] + 3.5, 'V', 'encre', 's'); text(ax, 42, 8, 'O', 'encre', 's')
text(ax, A[0] - 3, 12, 'A', 'encre', 's'); text(ax, M[0] + 3, 12, 'M', 'encre', 's')
text(ax, 40.5, 33, 'h = 6', 'fixe', 's', ha='right')
text(ax, 28.5, 5, r'$\mathrm{OA}\approx3{,}536$', 'sujet', 's'); text(ax, 52, 5, r'$\mathrm{OM}=2{,}5$', 'varie', 's')
text(ax, 77, 40, r'$\beta>\alpha$', 'resultat', 'l')
save(fig, '27-088')
