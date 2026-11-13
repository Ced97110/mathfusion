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
fig, ax = canvas(80)
box(ax, 8, 36, 22, 22, 'sujet')
line(ax, [(8, 36), (30, 58)], 'resultat', lw=1.3)
text(ax, 19, 32.5, '1', 'sujet'); text(ax, 4.5, 47, '1', 'sujet')
text(ax, 14, 55, r'$\sqrt{2}$', 'resultat')
o = (62, 36); u = 16
cubes(ax, [(0, 0, 0)], o, u, 'sujet')
p, q = iso(1, 0, 0, o, u), iso(0, 1, 1, o, u)
line(ax, [p, q], 'resultat', lw=1.3)
text(ax, 45, 50, '1', 'sujet'); text(ax, 66, 54, r'$\sqrt{3}$', 'resultat')
text(ax, 20, 73, 'carré : 2 directions', 'sujet', 's'); text(ax, 62, 73, 'cube : 3 directions', 'sujet', 's')
text(ax, 19, 24, r'$\sqrt{1^2+1^2}=\sqrt{2}$', 'sujet', 's')
text(ax, 66, 24, r'$\sqrt{1^2+1^2+1^2}=\sqrt{3}$', 'sujet', 's')
arrow(ax, (34, 20), (45, 20), 'varie'); text(ax, 39.5, 24, r'$+\,1^2$', 'varie', 's')
save(fig, '27-083')
