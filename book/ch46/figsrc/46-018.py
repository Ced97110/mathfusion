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

fig, ax = canvas(52)
a = (14, 26); b = (46, 26)
disc(ax, *a, 5, 'sujet', label='2'); disc(ax, *b, 5, 'sujet', label='6')
arrow(ax, (a[0] + 3.5, a[1] + 3.5), (b[0] - 3.5, b[1] + 3.5), 'sujet', curve=-0.4)
arrow(ax, (b[0] - 3.5, b[1] - 3.5), (a[0] + 3.5, a[1] - 3.5), 'sujet', curve=-0.4)
text(ax, 30, 38, '2 va sur 6', 'encre', 's')
text(ax, 30, 13.5, '6 va sur 2', 'encre', 's')
text(ax, 71, 31, '(2 6)', 'sujet', 'xl')
text(ax, 71, 21, 'échange de 2 et 6', 'encre', 's')
save(fig, '46-018')
