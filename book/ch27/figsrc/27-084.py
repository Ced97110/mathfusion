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
for x, y, k, a, b, ss, ts in [(6, 16, 5, '3', '4,24', 'a = 3', r'$3\div4{,}24\approx0{,}7071$'), (40, 16, 2.5, '10', '14,14', 'a = 10', r'$10\div14{,}14\approx0{,}7071$')]:
    bw = (3 * math.sqrt(2) if a == '3' else 10 * math.sqrt(2)) * k; h = (3 if a == '3' else 10) * k
    poly(ax, [(x, y), (x + bw, y), (x + bw, y + h)], 'sujet')
    rmark(ax, (x + bw, y), -1, 1)
    arc(ax, (x, y), 7, 0, 35.26, 'resultat')
    text(ax, x + 13, y + 3.3, '35,26°', 'resultat', 's')
    text(ax, x + bw + 3.5, y + h / 2, a, 'sujet', 's'); text(ax, x + bw / 2, y - 3.5, b, 'sujet', 's')
    text(ax, x + bw / 2, 52, ss, 'encre', 'm')
    text(ax, x + bw / 2, 44, ts, 'resultat', 's')
save(fig, '27-084')
