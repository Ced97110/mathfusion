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
box(ax, 8, 28, 24, 24, 'sujet')
line(ax, [(8, 28), (32, 52)], 'resultat', lw=1.3)
text(ax, 20, 24.5, '3', 'sujet'); text(ax, 35, 40, '3', 'sujet')
text(ax, 15, 49, r'$d\approx 4{,}24$', 'resultat', 's')
text(ax, 20, 18, 'face du cube', 'fixe', 's')
ys = [55, 41, 27, 13]
labs = [(r'$3^2=9$', 'varie'), (r'$9+9=18$', 'varie'), (r'$\sqrt{18}\approx 4{,}24$', 'resultat'), (r'$\sqrt{18}=3\sqrt{2}$', 'resultat')]
for y, (s, r) in zip(ys, labs): box(ax, 44, y, 42, 10, r, label=s)
for y in ys[:-1]: arrow(ax, (65, y), (65, y - 4), 'fixe')
text(ax, 65, 5, r'$a\sqrt{2}$ avec $a=3$', 'sujet', 's')
save(fig, '27-081')
