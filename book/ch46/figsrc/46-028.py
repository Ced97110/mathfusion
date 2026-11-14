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

fig, ax = canvas(58)
y = 26
f = lambda v: 8 + (v + 3) / 6 * 72
for v in range(-3, 3): line(ax, [(f(v) + 3.3, y), (f(v + 1) - 3.3, y)], 'fixe')
for v in range(-3, 4):
    lab = str(v).replace('-', '−')
    if v >= 0: disc(ax, f(v), y, 3.3, 'sujet', label=lab)
    elif v == -1: disc(ax, f(v), y, 3.3, 'limite', label=lab)
    else: disc(ax, f(v), y, 3.3, 'fixe', fill=False, label=lab)
arrow(ax, (f(1), y + 3.3), (f(-1), y + 3.3), 'varie', curve=0.5)
text(ax, f(0) + 2, 41, r'$a=1$ : inverse $-1$', 'varie', 's')
box(ax, 8, 46, 72, 10, 'sujet', label=r'$a\in H \Rightarrow a^{-1}\in H$', size='m')
brace(ax, f(0) - 4.2, f(3) + 4.2, 19, 'sujet', r'$H$ : entiers naturels')
brace(ax, f(-3) - 4.2, f(-1) + 4.2, 19, 'limite', r'hors de $H$ : échec')
save(fig, '46-028')
