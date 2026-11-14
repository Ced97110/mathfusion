import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
plt.rcParams['hatch.linewidth'] = 0.45
def mk(ox, oy, u): return lambda x, y: (ox + x * u, oy + y * u)
def _clip(pts, a, b, c):
    out = []
    for i in range(len(pts)):
        p, q = pts[i], pts[(i + 1) % len(pts)]
        fp, fq = a * p[0] + b * p[1] + c, a * q[0] + b * q[1] + c
        if fp >= 0: out.append(p)
        if (fp >= 0) != (fq >= 0):
            t = fp / (fp - fq); out.append((p[0] + t * (q[0] - p[0]), p[1] + t * (q[1] - p[1])))
    return out
def region(ax, P, win, m, c, above=True, role='resultat', hatch=True):
    x0, x1, y0, y1 = win
    pts = [(x0, y0), (x1, y0), (x1, y1), (x0, y1)]
    s = 1 if above else -1
    pts = _clip(pts, -m * s, s, -c * s)
    pp = [P(*p) for p in pts]
    ax.add_patch(Polygon(pp, closed=True, fc=FILL[role], ec=COL[role], lw=0, hatch='////' if hatch else None, zorder=1))
def frontier(ax, P, win, m, c, role='sujet', dash=False, lw=1.3):
    x0, x1, y0, y1 = win
    cand = []
    for x in (x0, x1):
        y = m * x + c
        if y0 - 1e-9 <= y <= y1 + 1e-9: cand.append((x, y))
    if m != 0:
        for y in (y0, y1):
            x = (y - c) / m
            if x0 - 1e-9 <= x <= x1 + 1e-9: cand.append((x, y))
    cand = sorted(set(cand))
    line(ax, [P(*cand[0]), P(*cand[-1])], role, lw=lw, dash=dash)
def frame(ax, P, win, lab=True):
    x0, x1, y0, y1 = win
    poly(ax, [P(x0, y0), P(x1, y0), P(x1, y1), P(x0, y1)], 'fixe', fill=False, lw=0.6)
    if x0 < 0 < x1: line(ax, [P(0, y0), P(0, y1)], 'fixe', lw=0.5)
    if y0 < 0 < y1: line(ax, [P(x0, 0), P(x1, 0)], 'fixe', lw=0.5)
    if lab:
        text(ax, *P(x1 - 0.3, -0.7) if y0 < 0 < y1 else P(x1 - 0.3, y0 + 0.7), r'$x$', 'fixe', 's')
        text(ax, *P(0.6, y1 - 0.5) if x0 < 0 < x1 else P(x0 + 0.6, y1 - 0.5), r'$y$', 'fixe', 's')
def dot(ax, P, x, y, role, r=1.3, fill=True):
    p = P(x, y); ax.add_patch(Circle(p, r, ec=COL[role], fc=FILL[role] if fill else 'white', lw=1.0, zorder=6))
fig, ax = canvas(52)
win = (-1, 7, -1, 5)
P = mk(6, 14, 4.8)
region(ax, P, win, -2/3, 4, above=False, role='resultat', hatch=False)
frame(ax, P, win)
frontier(ax, P, win, -2/3, 4, 'sujet')
dot(ax, P, 0, 0, 'resultat', 1.1); dot(ax, P, 5, 1, 'autre', 1.1)
text(ax, *P(0.3, 0.7), r'$O$', 'resultat', 's', ha='left')
text(ax, *P(5.3, 1.7), r'$(5,1)$', 'autre', 's', ha='left')
box(ax, 45, 30, 41, 14, 'resultat')
text(ax, 65.5, 40.2, r'$(0,0)$', 'resultat', 's')
text(ax, 65.5, 34, r'$2\times0+3\times0=0$', 'resultat', 's')
box(ax, 45, 6, 41, 20, 'autre')
text(ax, 65.5, 22, r'$(5,1)$', 'autre', 's')
text(ax, 65.5, 16.5, r'$2\times5+3\times1$', 'autre', 's')
text(ax, 65.5, 10.5, r'$=10+3=13$', 'autre', 's')
text(ax, 65.5, 48, 'court', 'resultat', 'm'); 
save(fig, '20-053')
