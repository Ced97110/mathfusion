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
cy = 30; R = 8.5
def ring(cx, n, members, role, rm, ro=1.1):
    ax.add_patch(Circle((cx, cy), R, fill=False, ec=COL[role], lw=0.6, zorder=1))
    for k in range(n):
        th = 2 * math.pi * k / n
        p = (cx + R * math.sin(th), cy + R * math.cos(th))
        if k in members: disc(ax, *p, rm, role)
        else: disc(ax, *p, ro, 'fixe')
ring(11, 12, {0, 4, 8}, 'sujet', 2.0)
ring(33, 12, set(range(12)), 'autre', 1.8)
ring(55, 4, {0, 1, 2, 3}, 'sujet', 2.4)
ring(77, 2, {0, 1}, 'autre', 2.4)
text(ax, 22, 49, 'horloge', 'fixe', 'm'); text(ax, 66, 49, 'cartes', 'fixe', 'm')
for cx, s in ((11, 'avancer de 4'), (33, 'avancer de 5'), (55, 'carte 1'), (77, 'carte 2')):
    text(ax, cx, 17, s, 'encre', 's')
for cx, s, role in ((11, 'tour de 3', 'sujet'), (33, 'tour de 12', 'autre'), (55, 'tour de 4', 'sujet'), (77, 'tour de 2', 'autre')):
    text(ax, cx, 10, s, role, 'm', weight='bold')
save(fig, '46-021')
