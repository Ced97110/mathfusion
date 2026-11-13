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

fig, ax = canvas(62)
S = pts(10, 2, 40, 14); T = pts(34, 3, 40, 14)
dots(ax, S, [r'$s_1$', r'$s_2$'], ['sujet', 'varie'], 3.2, 's')
dots(ax, T, ['a', 'b', 'c'], ['sujet', 'varie', 'fixe'], 3.2, 's')
link(ax, S[0], T[0], 'sujet', 3.2); link(ax, S[1], T[1], 'varie', 3.2)
S2 = pts(56, 2, 40, 14); T2 = pts(80, 3, 40, 14)
dots(ax, S2, [r'$s_1$', r'$s_2$'], ['sujet', 'varie'], 3.2, 's')
dots(ax, T2, ['a', 'b', 'c'], ['limite', 'fixe', 'fixe'], 3.2, 's')
link(ax, S2[0], T2[0], 'limite', 3.2); link(ax, S2[1], T2[0], 'limite', 3.2)
text(ax, 22, 18, 'injective ✓', 'resultat', 'm', weight='bold'); text(ax, 68, 18, 'pas injective ✗', 'limite', 'm', weight='bold')
text(ax, 22, 8, 'c reste vide : permis', 'fixe', 's'); text(ax, 68, 8, 'deux flèches, un point', 'limite', 's')
save(fig, '42-203')
