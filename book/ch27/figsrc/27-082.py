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
text(ax, 44, 66, r'diagonale $\div$ arête $=\sqrt{3}\approx 1{,}73$', 'resultat', 's')
for a, yt, v in [(1, 52, '1,73'), (2, 34, '3,46'), (5, 16, '8,66')]:
    text(ax, 3, yt, f'$a={a}$', 'encre', 's', ha='left')
    box(ax, 22, yt, a * 5, 3, 'fixe', r=0.3); text(ax, 22 + a * 5 + 2, yt + 1.5, str(a), 'fixe', 's', ha='left')
    w = a * 5 * math.sqrt(3)
    box(ax, 22, yt - 5, w, 3, 'resultat', r=0.3); text(ax, 22 + w + 2, yt - 3.5, v, 'resultat', 's', ha='left')
box(ax, 4, 2, 5, 3, 'fixe', r=0.3); text(ax, 11, 3.5, 'arête', 'fixe', 's', ha='left')
box(ax, 30, 2, 5, 3, 'resultat', r=0.3); text(ax, 37, 3.5, 'grande diagonale', 'resultat', 's', ha='left')
save(fig, '27-082')
