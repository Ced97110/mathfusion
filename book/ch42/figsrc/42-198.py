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
text(ax, 44, 67, 'un seul signe, trois morceaux', 'fixe', 's')
for x, role, lab, cap in [(6, 'sujet', r'$\alpha$', "l'application"), (33, 'varie', r'$^{-1}$', 'sens inverse'), (60, 'autre', r'$(B)$', 'partie de T')]:
    box(ax, x, 44, 22, 14, role, label=lab, size='xl')
    text(ax, x + 11, 39, cap, role, 's')
box(ax, 4, 11, 24, 11, 'autre', label=r'$B=\{a\}$', size='m')
arrow(ax, (29, 16.5), (51, 16.5), 'varie'); text(ax, 40, 21, r'$\alpha^{-1}$', 'varie', 's')
box(ax, 52, 11, 28, 11, 'resultat', label=r'$\{1,\,2\}$', size='m')
text(ax, 66, 6, 'antécédents de a', 'resultat', 's')
save(fig, '42-198')
