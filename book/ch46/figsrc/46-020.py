import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def hpos(cx, cy, R, k):
    th = math.radians(30 * k)
    return (cx + R * math.sin(th), cy + R * math.cos(th))

def clock(ax, cx, cy, R, spec, big=3.2, small=1.4):
    ax.add_patch(Circle((cx, cy), R, fill=False, ec=COL['fixe'], lw=0.5, zorder=1))
    for k in range(12):
        x, y = hpos(cx, cy, R, k)
        if k in spec:
            s = spec[k]; fill = s[2] if len(s) > 2 else True
            disc(ax, x, y, big, s[0], fill=fill, label=s[1], size='s')
        else:
            disc(ax, x, y, small, 'fixe')

def ar(ax, p, q, rr, role='sujet', curve=0.0):
    d = math.hypot(q[0] - p[0], q[1] - p[1]); u = ((q[0] - p[0]) / d, (q[1] - p[1]) / d)
    arrow(ax, (p[0] + u[0] * rr, p[1] + u[1] * rr), (q[0] - u[0] * rr, q[1] - u[1] * rr), role, curve=curve)

fig, ax = canvas(62)
r = 3.8
def group(xs, nums, y, role, pad=5.5, roles=None, skip=()):
    box(ax, xs[0] - pad, y - 7, xs[-1] - xs[0] + 2 * pad, 14, role, fill=False, lw=1.0)
    for i, (x, n) in enumerate(zip(xs, nums)):
        if n not in skip: disc(ax, x, y, r, (roles or {}).get(n, role), label=str(n))
group([11, 22, 33, 44], [1, 3, 5, 8], 50, 'sujet')
group([64, 76], [2, 6], 50, 'autre')
text(ax, 44, 37, 'disjointes : rien en commun', 'resultat', 's')
group([10, 22, 36], [1, 5, 3], 20, 'sujet', roles={3: 'limite'})
group([36, 50, 62], [3, 4, 7], 20, 'autre', roles={3: 'limite'}, skip=(3,))
text(ax, 36, 6, 'le 3 est en commun', 'limite', 's')
save(fig, '46-020')
