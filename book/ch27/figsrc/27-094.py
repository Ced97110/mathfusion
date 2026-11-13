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
fig, ax = canvas(70)
u = 7; O = (22, 22); V = (22, 22 + 6 * u); M = (22 + 2.5 * u, 22); A = (22 + 3.54 * u, 22)
line(ax, [O, V], 'fixe', lw=1.2, dash=True); line(ax, [O, A], 'fixe', lw=1.0)
line(ax, [V, M], 'varie', lw=1.8); line(ax, [V, A], 'sujet', lw=1.8)
rmark(ax, O, 1, 1)
arc(ax, M, 4.5, 112.62, 180, 'varie', lw=1.0); arc(ax, A, 6.5, 120.5, 180, 'sujet', lw=1.0)
text(ax, 34.5, 27, r'$\beta$', 'varie', 's'); text(ax, 43.5, 26, r'$\alpha$', 'sujet', 's')
text(ax, 20.5, 43, 'hauteur 6', 'fixe', 's', ha='right')
brace(ax, O[0], M[0], 20, 'varie', label='2,5'); brace(ax, O[0], A[0], 12.5, 'sujet', label=r'$\approx3{,}54$')
text(ax, 67, 58, 'face : raide', 'varie', 's'); text(ax, 67, 52, r'$\tan\beta=6\div2{,}5$', 'varie', 's')
text(ax, 67, 40, 'arête : moins raide', 'sujet', 's'); text(ax, 67, 34, r'$\tan\alpha=6\div3{,}54$', 'sujet', 's')
text(ax, 67, 22, r'$\beta>\alpha$', 'resultat', 'l')
save(fig, '27-094')
