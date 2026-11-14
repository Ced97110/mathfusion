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

fig, ax = canvas(54)
cL = (22, 28); cR = (66, 28); R = 15
clock(ax, *cL, R, {0: ('sujet', '0')})
spec = {k: ('sujet', '0' if k == 0 else None) for k in range(12)}
clock(ax, *cR, R, spec)
text(ax, 44, 50, 'deux sous-groupes toujours', 'fixe', 'm')
text(ax, 22, 5, r'$\{e\}$ : le neutre seul', 'sujet', 's')
text(ax, 66, 5, r'$G$ : tout le groupe', 'sujet', 's')
save(fig, '46-032')
