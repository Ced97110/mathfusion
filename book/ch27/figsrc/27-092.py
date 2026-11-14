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
o = (30, 6); u = 4.5
p = pyr(ax, o, u)
line(ax, [p['V'], p['M']], 'sujet', lw=1.8); line(ax, [p['V'], p['O']], 'fixe', lw=1.4, dash=True); line(ax, [p['V'], p['A']], 'autre', lw=1.8)
for k, c in [('V', 'sujet'), ('M', 'sujet'), ('O', 'fixe'), ('A', 'autre')]:
    dx, dy = {'V': (0, 3.5), 'M': (3.5, -2), 'O': (-3, -2), 'A': (-3.5, 0)}[k]
    text(ax, p[k][0] + dx, p[k][1] + dy, k, c, 's')
for y, r, s in [(52, 'sujet', 'apothème VM = 6,5'), (40, 'fixe', 'hauteur VO = 6'), (28, 'autre', r'arête VA $\approx$ 6,96')]:
    line(ax, [(54, y), (58, y)], r, lw=1.8); text(ax, 59.5, y, s, r, 's', ha='left')
text(ax, 70, 18, 'unité : cm', 'fixe', 's')
save(fig, '27-092')
