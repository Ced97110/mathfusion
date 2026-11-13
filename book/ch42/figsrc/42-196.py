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

fig, ax = canvas(66)
box(ax, 3, 52, 44, 10, 'fixe', label='toutes les images de S', size='s')
arrow(ax, (48, 57), (58, 57), 'varie')
box(ax, 59, 52, 26, 10, 'sujet', label=r'im $\alpha$', size='l')
box(ax, 10, 28, 26, 11, 'sujet', label='im', size='l')
box(ax, 52, 28, 26, 11, 'autre', label=r'$\alpha$', size='l')
text(ax, 23, 23, 'se lit « image »', 'sujet', 's')
text(ax, 65, 23, "nom de l'application", 'autre', 's', )
box(ax, 4, 3, 80, 12, 'resultat', label=r'im $\alpha=\alpha(S)=\{a,\,b\}$', size='l')
save(fig, '42-196')
