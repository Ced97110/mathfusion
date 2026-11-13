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

fig, ax = canvas(66)
vals = (0, 4, 8)
for i, a in enumerate(vals):
    for j, b in enumerate(vals):
        s = (a + b) % 12
        role = 'fixe' if (a == 0 or b == 0) else ('varie' if s == 0 else 'resultat')
        box(ax, 3 + 28 * j, 55 - 11 * i, 26, 9, role, label=rf'${a}+{b}={s}$', size='s')
for y, role, t in ((24, 'fixe', 'avec 0 : rien ne change'), (16, 'resultat', 'les autres : dans la partie'), (8, 'varie', 'somme 0 : inverses')):
    box(ax, 3, y - 2.5, 5, 5, role, r=0.4); text(ax, 11, y, t, 'encre', 's', ha='left')
save(fig, '46-030')
