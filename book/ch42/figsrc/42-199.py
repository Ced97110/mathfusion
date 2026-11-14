import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def pts(x, n, yc, sp):
    return [(x, yc + (n - 1) / 2 * sp - i * sp) for i in range(n)]
def link(ax, p, q, role, r=3.2, curve=0.0, both=False, lw=1.0):
    dx, dy = q[0] - p[0], q[1] - p[1]; d = math.hypot(dx, dy); ux, uy = dx / d, dy / d
    arrow(ax, (p[0] + ux * (r + 0.3), p[1] + uy * (r + 0.3)), (q[0] - ux * (r + 0.6), q[1] - uy * (r + 0.6)), role, lw=lw, curve=curve, both=both)
def dots(ax, P, labels, roles, r=3.2, size='m'):
    for p, l, ro in zip(P, labels, roles):
        disc(ax, p[0], p[1], r, ro, label=l, size=size)
def panel(ax, cx, ns, nt, E, rs, rt, dx=8, r=2.4, yc=34, sp=12, ls=None, lt=None, ar=None):
    S = pts(cx - dx, ns, yc, sp); T = pts(cx + dx, nt, yc, sp)
    dots(ax, S, ls or [None] * ns, rs, r, 's'); dots(ax, T, lt or [None] * nt, rt, r, 's')
    for k, (i, j) in enumerate(E):
        link(ax, S[i], T[j], (ar[k] if ar else 'sujet'), r)
    return S, T

fig, ax = canvas(72)
S = pts(22, 2, 44, 16); a = (66, 44)
box(ax, 13, 28, 18, 32, 'resultat', fill=True)
box(ax, 56, 36, 20, 16, 'autre', fill=True)
dots(ax, S, ['1', '2'], ['sujet'] * 2); dots(ax, [a], ['a'], ['autre'])
link(ax, a, S[0], 'varie'); link(ax, a, S[1], 'varie')
text(ax, 22, 66, r'$S$', 'fixe', 'l'); text(ax, 66, 66, r'$T$', 'fixe', 'l')
text(ax, 83, 44, r'$B$', 'autre', 'l')
text(ax, 66, 27, 'a vient de 1\net de 2', 'limite', 's')
text(ax, 44, 16, r'$\alpha^{-1}(B)=\{1,\,2\}$', 'resultat', 'm')
text(ax, 44, 8, "c'est un ensemble de S", 'resultat', 's')
save(fig, '42-199')
