import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math as _m
def ring(ax, cx, cy, R, labels, role='sujet', rd=4.0, arrow_role='varie', size='m', roles=None, aroles=None, curve=-0.3):
    n = len(labels); P = []
    for k in range(n):
        a = _m.radians(90 - 360 * k / n); P.append((cx + R * _m.cos(a), cy + R * _m.sin(a)))
    for k, (x, y) in enumerate(P):
        disc(ax, x, y, rd, (roles or [role] * n)[k], label=labels[k], size=size)
    for k in range(n):
        p, q = P[k], P[(k + 1) % n]; d = _m.hypot(q[0] - p[0], q[1] - p[1]); u = ((q[0] - p[0]) / d, (q[1] - p[1]) / d)
        arrow(ax, (p[0] + u[0] * (rd + .5), p[1] + u[1] * (rd + .5)), (q[0] - u[0] * (rd + .5), q[1] - u[1] * (rd + .5)),
              (aroles or [arrow_role] * n)[k], curve=curve)
    return P
def selfloop(ax, x, y, r, role='varie'):
    arrow(ax, (x - 1.4, y + r + .2), (x + 1.4, y + r + .2), role, curve=-1.7)
from matplotlib.patches import Ellipse
def ell(x, y, w, h, role, dash=False):
    ax.add_patch(Ellipse((x, y), w, h, ec=COL[role], fc='none' if dash else FILL[role], lw=0.9, ls='--' if dash else '-', zorder=2, alpha=1 if dash else 0.75))
fig, ax = canvas(76)
y = 62
ell(22, y, 36, 12, 'sujet'); ell(53, y, 16, 12, 'autre')
text(ax, 22, y, '1 3 5 8', 'sujet'); text(ax, 53, y, '2 6', 'autre')
text(ax, 22, y + 9.5, '(1 3 5 8)', 'sujet', 's'); text(ax, 53, y + 9.5, '(2 6)', 'autre', 's')
text(ax, 75, y, 'aucun commun', 'resultat', 's')
y = 36
ell(20, y, 30, 12, 'sujet'); ell(42, y, 30, 12, 'autre')
text(ax, 14, y, '1 5', 'sujet'); text(ax, 31, y, '3', 'limite', 'm', weight='bold'); text(ax, 48, y, '4 7', 'autre')
text(ax, 18, y + 9.5, '(1 3 5)', 'sujet', 's'); text(ax, 44, y + 9.5, '(3 4 7)', 'autre', 's')
text(ax, 73, y, '3 en commun', 'limite', 's')
y = 10
ell(28, y, 36, 11, 'sujet'); ell(28, y, 42, 15, 'autre', dash=True)
text(ax, 28, y, '1 3 5', 'sujet')
text(ax, 28, y + 10.5, '(1 3 5) et (1 3 5)', 'autre', 's')
text(ax, 73, y, 'tous communs', 'fixe', 's')
save(fig, '46-170')
