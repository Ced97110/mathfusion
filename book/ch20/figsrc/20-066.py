import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def _clip(pts, a, b, c):
    out = []
    for i in range(len(pts)):
        p, q = pts[i], pts[(i + 1) % len(pts)]
        fp = a * p[0] + b * p[1] - c; fq = a * q[0] + b * q[1] - c
        if fp <= 1e-9: out.append(p)
        if (fp < -1e-9 and fq > 1e-9) or (fp > 1e-9 and fq < -1e-9):
            t = fp / (fp - fq); out.append((p[0] + t * (q[0] - p[0]), p[1] + t * (q[1] - p[1])))
    return out

def plane(ax, ox, oy, u, xr, yr, labels=True):
    P = lambda x, y: (ox + x * u, oy + y * u)
    arrow(ax, P(xr[0], 0), P(xr[1] + 0.7, 0), 'fixe', lw=0.8)
    arrow(ax, P(0, yr[0]), P(0, yr[1] + 0.7), 'fixe', lw=0.8)
    for k in range(xr[0], xr[1] + 1):
        if k: ax.plot([P(k, 0)[0]] * 2, [oy - 0.7, oy + 0.7], color=COL['fixe'], lw=0.6, zorder=1.5)
    for k in range(yr[0], yr[1] + 1):
        if k: ax.plot([ox - 0.7, ox + 0.7], [P(0, k)[1]] * 2, color=COL['fixe'], lw=0.6, zorder=1.5)
    if labels:
        text(ax, P(xr[1] + 0.7, 0)[0] + 2.0, oy, '$x$', 'fixe', 's')
        text(ax, ox, P(0, yr[1] + 0.7)[1] + 2.2, '$y$', 'fixe', 's')
    return P

def shade(ax, P, xr, yr, cons, role):
    pts = [(xr[0], yr[0]), (xr[1], yr[0]), (xr[1], yr[1]), (xr[0], yr[1])]
    for a, b, c in cons: pts = _clip(pts, a, b, c)
    if len(pts) > 2:
        ax.add_patch(Polygon([P(*p) for p in pts], closed=True, fc=FILL[role], ec='none', zorder=1))

def dot(ax, P, x, y, role, fill=True, r=1.1):
    ax.add_patch(Circle(P(x, y), r, ec=COL[role], fc=FILL[role] if fill else 'white', lw=0.9, zorder=4))

fig, ax = canvas(64); u = 7.0; xr = (-2, 3); yr = (-2, 4); ox, oy = 18, 14
P = plane(ax, ox, oy, u, xr, yr)
shade(ax, P, xr, yr, [(-1, 1, 1)], 'sujet')
line(ax, [P(-2, -1), P(3, 4)], 'sujet', lw=1.3)
text(ax, 30, 58, r'$y\leq x+1$', 'sujet', 'l')
for (x, y, role, lab) in ((0, 3, 'limite', '(0, 3) : 3 ≤ 1 faux'), (1, 2, 'resultat', '(1, 2) : 2 ≤ 2 vrai'), (0, 0, 'resultat', '(0, 0) : 0 ≤ 1 vrai')):
    dot(ax, P, x, y, role)
    px, py = P(x, y)
    box(ax, 52, py - 3.5, 34, 7, role, label=lab, size='s')
    arrow(ax, (px + 1.4, py), (51.5, py), role, lw=0.7)
save(fig, '20-066')
