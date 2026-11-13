import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def arc(ax, c, r, a0, a1, role, lw=0.9):
    pts = [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / 120)), c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / 120))) for i in range(121)]
    line(ax, pts, role, lw)

fig, ax = canvas(80)
c = (30, 42); R = 24
P = lambda r, a: (c[0] + r * math.cos(math.radians(a)), c[1] + r * math.sin(math.radians(a)))
for a in range(360):
    r1 = R - (3.0 if a % 10 == 0 else 1.5)
    ax.plot([P(r1, a)[0], P(R, a)[0]], [P(r1, a)[1], P(R, a)[1]], color=COL['fixe'], lw=0.35, zorder=1.5)
arc(ax, c, R, 0, 360, 'sujet', 1.0)
poly(ax, [c, P(R, 0), P(R, 1.0)], 'varie')
line(ax, [c, P(R, 0)], 'varie', lw=0.8); line(ax, [c, P(R, 1)], 'varie', lw=0.8)
text(ax, c[0] - 1, c[1] + 4, 'un tour', 'sujet', 'm')
text(ax, c[0] - 1, c[1] - 2, '360 parts égales', 'sujet', 's')
Z = (50, 10); RZ = 32; AZ = 22
q = lambda r, a: (Z[0] + r * math.cos(math.radians(a)), Z[1] + r * math.sin(math.radians(a)))
poly(ax, [Z, q(RZ, 0), q(RZ, AZ)], 'varie')
line(ax, [Z, q(RZ, 0)], 'varie', lw=1.0); line(ax, [Z, q(RZ, AZ)], 'varie', lw=1.0)
arc(ax, Z, 12, 0, AZ, 'varie', 1.0)
text(ax, 83, 13, '1°', 'varie', 'l', weight='bold')
text(ax, 66, 3.5, 'une part = 1 degré', 'varie', 's')
line(ax, [P(R, 0), q(RZ, 0)], 'varie', lw=0.5, dash=True)
line(ax, [P(R, 1), q(RZ, AZ)], 'varie', lw=0.5, dash=True)
save(fig, '25-003')
