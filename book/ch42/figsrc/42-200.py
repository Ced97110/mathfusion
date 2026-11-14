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

fig, ax = canvas(68)
ox, oy, xu, yu = 14, 14, 11, 3.8
arrow(ax, (10, oy), (78, oy), 'fixe', lw=0.9); arrow(ax, (ox, 10), (ox, 56), 'fixe', lw=0.9)
text(ax, 83, oy, r'$n$', 'fixe', 'm')
for n in range(6):
    x = ox + n * xu; y = oy + 2 * n * yu
    ro = 'sujet' if n < 3 else 'fixe'
    line(ax, [(x, oy), (x, y)], ro, lw=0.5, dash=True)
    text(ax, x, 10.2, str(n), ro, 's')
    disc(ax, x, y, 1.7, ro)
for n in range(3):
    x = ox + n * xu; y = oy + 2 * n * yu
    text(ax, x + 2.5, y + 3.6, f'({n}, {2 * n})', 'sujet', 's', ha='left')
brace(ax, 11, 39, 8, 'sujet', label=r'$S_1=\{0,1,2\}$')
text(ax, 4, 63, 'même règle, départ réduit à $S_1$', 'sujet', 'm', ha='left')
text(ax, 65, 52, 'couples abandonnés', 'fixe', 's', ha='right')
save(fig, '42-200')
