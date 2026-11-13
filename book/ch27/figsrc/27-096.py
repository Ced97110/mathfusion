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
u = 6; V = (44, 54); O = (44, 54 - 6 * u); A = (44 - 3.536 * u, O[1]); C = (44 + 3.536 * u, O[1])
poly(ax, [A, O, V], 'sujet'); poly(ax, [O, C, V], 'sujet')
line(ax, [V, O], 'varie', lw=1.2, dash=True)
arc(ax, V, 8, 239.49, 270, 'varie', lw=1.1); arc(ax, V, 8, 270, 300.51, 'varie', lw=1.1)
arc(ax, V, 12, 239.49, 300.51, 'resultat', lw=1.2)
text(ax, V[0], V[1] + 3.5, r'$\mathrm{AVC}\approx61{,}02^\circ$', 'resultat', 's')
text(ax, 42.5, 30, '30,51°', 'varie', 's', ha='right'); text(ax, 45.5, 30, '30,51°', 'varie', 's', ha='left')
text(ax, 46.5, 44, '6', 'varie', 's', ha='left')
text(ax, A[0] - 3, A[1], 'A', 'encre', 's'); text(ax, C[0] + 3, C[1], 'C', 'encre', 's')
text(ax, 40.5, 53.5, 'V', 'encre', 's')
brace(ax, A[0], O[0], O[1] - 2, 'sujet', label='3,536'); brace(ax, O[0], C[0], O[1] - 2, 'sujet', label='3,536')
save(fig, '27-096')
