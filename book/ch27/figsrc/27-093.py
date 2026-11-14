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
u = 5
for x, bw, role, b, hyp, calc1, calc2 in [(10, 2.5, 'varie', '2,5', '6,5', r'$\sqrt{6^2+2{,}5^2}=\sqrt{42{,}25}$', r'$=6{,}5$ cm'),
                                          (52, 3.536, 'sujet', '3,536', r'6,96', r'$\sqrt{6^2+12{,}5}=\sqrt{48{,}5}$', r'$\approx6{,}96$ cm')]:
    w = bw * u
    poly(ax, [(x, 22), (x + w, 22), (x, 22 + 6 * u)], role); rmark(ax, (x, 22), 1, 1)
    text(ax, x - 2.5, 37, '6', role, 's'); text(ax, x + w / 2, 18.5, b, role, 's')
    text(ax, x + w / 2 + 4.5, 22 + 3 * u + 3, hyp, role, 's')
    text(ax, x + 14, 11, calc1, role, 's'); text(ax, x + 14, 5, calc2, role, 's')
text(ax, 20, 59, 'face : apothème', 'varie', 's'); text(ax, 66, 59, 'arête', 'sujet', 's')
save(fig, '27-093')
