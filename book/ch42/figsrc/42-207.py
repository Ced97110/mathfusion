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

fig, ax = canvas(60)
specs = [(15, 2, 3, [(0, 0), (1, 1)], ['resultat', 'resultat', 'limite'], ('injective ✓', 'resultat'), ('surjective ✗', 'limite')),
         (44, 3, 2, [(0, 0), (1, 0), (2, 1)], ['limite', 'resultat'], ('injective ✗', 'limite'), ('surjective ✓', 'resultat')),
         (73, 3, 3, [(0, 0), (1, 1), (2, 2)], ['resultat'] * 3, ('injective ✓', 'resultat'), ('surjective ✓', 'resultat'))]
for cx, ns, nt, E, rt, t1, t2 in specs:
    panel(ax, cx, ns, nt, E, ['sujet'] * ns, rt, dx=8, yc=40, sp=12)
    text(ax, cx, 18, t1[0], t1[1], 's', weight='bold'); text(ax, cx, 11, t2[0], t2[1], 's', weight='bold')
text(ax, 44, 3.5, 'un point en rouge fait échouer un test', 'fixe', 's')
save(fig, '42-207')
