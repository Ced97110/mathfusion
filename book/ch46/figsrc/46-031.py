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
c = (34, 34); R = 17
clock(ax, *c, R, {0: ('sujet', '0'), 1: ('sujet', '1'), 2: ('sujet', '2'), 3: ('limite', '3'), 11: ('limite', '11')})
ar(ax, hpos(*c, R, 2), hpos(*c, R, 3), 3.4, 'limite', curve=0.2)
text(ax, 58, 46, r'$1+2=3$', 'limite', 'l', ha='left')
text(ax, 58, 34, "3 n'est pas dedans", 'limite', 's', ha='left')
text(ax, 20, 52, 'inverse de 1', 'limite', 's', ha='right')
text(ax, 58, 20, "11 non plus", 'limite', 's', ha='left')
save(fig, '46-031')
