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
o = (34, 8); u = 4.5
p = pyr(ax, o, u)
line(ax, [p['O'], p['V']], 'resultat', lw=1.2, dash=True)
disc(ax, p['O'][0], p['O'][1], 0.9, 'resultat'); disc(ax, p['V'][0], p['V'][1], 0.9, 'sujet')
text(ax, p['V'][0], p['V'][1] + 3.5, 'V', 'sujet'); text(ax, p['O'][0] + 3, p['O'][1] - 2.5, 'O', 'resultat')
B_, C_ = p['B'], p['C']
nx, ny = 0.5, -0.866
Bd, Cd = (B_[0] + 3*nx, B_[1] + 3*ny), (C_[0] + 3*nx, C_[1] + 3*ny)
arrow(ax, Bd, Cd, 'sujet', lw=0.8, both=True)
text(ax, 66, 8, 'côté 5 cm', 'sujet', 's')
H = p['V'][1] - p['O'][1]
hx = p['O'][0] + 14
arrow(ax, (hx, p['O'][1]), (hx, p['V'][1]), 'resultat', lw=0.8, both=True)
line(ax, [(p['V'][0], p['V'][1]), (hx, p['V'][1])], 'resultat', lw=0.4, dash=True)
line(ax, [(p['O'][0], p['O'][1]), (hx, p['O'][1])], 'resultat', lw=0.4, dash=True)
text(ax, hx + 2, p['O'][1] + H / 2, 'hauteur 6 cm', 'resultat', 's', ha='left')
text(ax, p['O'][0] - 3, p['O'][1] - 3.5, 'centre', 'resultat', 's', ha='right')
text(ax, 44, 2.5, 'sommet au-dessus du centre', 'fixe', 's')
save(fig, '27-086')
