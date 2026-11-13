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
S = pts(10, 3, 40, 12); T = pts(34, 2, 40, 14)
box(ax, 28, 26, 13, 28, 'resultat', fill=False, dash=True)
dots(ax, S, ['1', '2', '3'], ['sujet'] * 3, 3.0, 's'); dots(ax, T, ['a', 'b'], ['resultat'] * 2, 3.0, 's')
for i, j in [(0, 0), (1, 0), (2, 1)]:
    link(ax, S[i], T[j], 'sujet', 3.0)
S2 = pts(56, 2, 40, 14); T2 = pts(80, 2, 40, 14)
dots(ax, S2, ['1', '2'], ['sujet'] * 2, 3.0, 's'); dots(ax, T2, ['a', 'b'], ['resultat', 'limite'], 3.0, 's')
link(ax, S2[0], T2[0], 'sujet', 3.0); link(ax, S2[1], T2[0], 'sujet', 3.0)
text(ax, 22, 18, 'surjective ✓', 'resultat', 'm', weight='bold'); text(ax, 68, 18, 'pas surjective ✗', 'limite', 'm', weight='bold')
text(ax, 22, 8, 'chaque arrivée reçoit\nau moins une flèche', 'fixe', 's'); text(ax, 68, 8, 'b ne reçoit rien', 'limite', 's')
save(fig, '42-204')
