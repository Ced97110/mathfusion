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

fig, ax = canvas(74)
S = pts(22, 3, 40, 15); T = pts(62, 3, 40, 15)
box(ax, 50, 14, 24, 51, 'fixe', fill=False, dash=True)
box(ax, 53, 32, 18, 31, 'resultat', fill=False)
dots(ax, S, ['1', '2', '3'], ['fixe'] * 3)
dots(ax, T, ['a', 'b', 'c'], ['resultat', 'resultat', 'limite'])
for i, j in [(0, 0), (1, 0), (2, 1)]:
    link(ax, S[i], T[j], 'varie')
text(ax, 22, 68, r'$S$', 'fixe', 'l'); text(ax, 62, 68, r'$T$', 'fixe', 'l')
text(ax, 81, 48, r'im $\alpha$', 'resultat', 'm'); text(ax, 81, 25, 'aucune\nflèche', 'limite', 's')
text(ax, 38, 8, r'im $\alpha\subseteq T$, pas toujours $=T$', 'encre', 's')
save(fig, '42-195')
