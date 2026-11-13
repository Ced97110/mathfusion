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
fig, ax = canvas(62)
k = 0.2; O = (36, 24); L = (O[0] - 115 * k, 24); R = (O[0] + 115 * math.sqrt(2) * k, 24); V = (36, 24 + 146 * k)
poly(ax, [L, O, V], 'varie'); poly(ax, [O, R, V], 'sujet'); line(ax, [O, V], 'fixe', lw=1.0, dash=True)
arc(ax, L, 6, 0, 51.8, 'varie', lw=1.1); arc(ax, R, 6, 138.1, 180, 'sujet', lw=1.1)
text(ax, 24.5, 21, r'$\beta\approx51{,}8^\circ$', 'varie', 's'); text(ax, 55, 21, r'$\alpha\approx41{,}9^\circ$', 'sujet', 's')
text(ax, 34.5, 38, '146 m', 'fixe', 's', ha='right')
text(ax, 18, 44, 'face', 'varie', 's'); text(ax, 58, 44, 'arête', 'sujet', 's')
brace(ax, L[0], O[0], 21 - 4.5, 'varie', label='115 m'); brace(ax, O[0], R[0], 21 - 4.5, 'sujet', label=r'$115\sqrt{2}$ m')
text(ax, 44, 6.4, r'$\tan\beta=146\div115\approx1{,}27$', 'varie', 's'); text(ax, 44, 2.2, r'$\tan\alpha=1{,}27\div\sqrt{2}\approx0{,}90$', 'sujet', 's')
text(ax, 36, 13.2, r'$\times\sqrt{2}$', 'encre', 's')
arrow(ax, (31, 10.4), (41, 10.4), 'encre', lw=0.8)
save(fig, '27-095')
