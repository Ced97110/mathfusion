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
u = 9; A = (6, 16); C = (A[0] + 4.243 * u, 16); G = (C[0], 16 + 3 * u)
poly(ax, [A, C, G], 'fixe'); rmark(ax, C, -1, 1)
arc(ax, A, 9, 0, 35.26, 'fixe')
arc(ax, G, 8, 215.26, 270, 'sujet', lw=1.2)
text(ax, 19.5, 19.8, '35,26°', 'fixe', 's'); text(ax, 38, 30, '54,74°', 'sujet', 's')
text(ax, 47.5, 29.5, '3', 'fixe', 's'); text(ax, 25, 12, '4,24', 'fixe', 's'); text(ax, 20, 35.5, '5,20', 'fixe', 's')
text(ax, 3.5, 13.5, 'A', 'encre', 's'); text(ax, 47.5, 13.5, 'C', 'encre', 's'); text(ax, G[0] + 3.5, G[1] + 2, 'G', 'encre', 's')
text(ax, 68, 46, r'$\cos=3\div5{,}20$', 'sujet', 's'); text(ax, 68, 38, r'$\approx0{,}5774$', 'sujet', 's')
text(ax, 44, 4, r'$35{,}26^\circ+54{,}74^\circ=90^\circ$', 'resultat', 's')
save(fig, '27-085')
