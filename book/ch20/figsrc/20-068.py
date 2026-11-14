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
        pg = Polygon([P(*p) for p in pts], closed=True, fc=FILL[role], ec='none', zorder=1)
        ax.add_patch(pg)
        for k in range(-40, 40):
            l, = ax.plot([0, 60], [k * 2.2, k * 2.2 + 60], color=COL[role], lw=0.6, zorder=1.2)
            l.set_clip_path(pg)

def dot(ax, P, x, y, role, fill=True, r=1.1):
    ax.add_patch(Circle(P(x, y), r, ec=COL[role], fc=FILL[role] if fill else 'white', lw=0.9, zorder=4))

fig, ax = canvas(64); u = 7.0; xr = (-2, 3); yr = (-2, 4); ox, oy = 18, 14
P = plane(ax, ox, oy, u, xr, yr)
shade(ax, P, xr, yr, [(-1, 1, 1)], 'sujet')
line(ax, [P(-2, -1), P(3, 4)], 'sujet', lw=1.3)
dot(ax, P, 0, 0, 'resultat'); text(ax, ox + 3.0, oy - 2.8, '$O$', 'resultat', 'm')
text(ax, 30, 58, r'$y\leq x+1$', 'sujet', 'l')
box(ax, 53, 44, 34, 9, 'sujet', label=r'$0\leq 0+1$')
box(ax, 53, 28, 34, 9, 'resultat', label=r'$0\leq 1$ : vrai')
box(ax, 53, 12, 34, 9, 'resultat', label='hachure : côté de O', size='s')
arrow(ax, (70, 43.5), (70, 37.5), 'fixe'); arrow(ax, (70, 27.5), (70, 21.5), 'fixe')
save(fig, '20-068')
