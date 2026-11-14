import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

TH = 0.6
CS, SN, TN = math.cos(TH), math.sin(TH), math.tan(TH)
def geo(ox, oy, s):
    return lambda x, y: (ox + x * s, oy + y * s)
def arcpts(f, a0, a1, n=40):
    return [f(math.cos(a0 + (a1 - a0) * i / n), math.sin(a0 + (a1 - a0) * i / n)) for i in range(n + 1)]
def sector(f):
    return [f(0, 0)] + arcpts(f, 0, TH)
def lead(ax, pt, xl, yl, s, role, ha='left'):
    line(ax, [pt, (xl - 1 if ha == 'left' else xl + 1, yl)], role, lw=0.6)
    ax.plot([pt[0]], [pt[1]], marker='o', ms=2, color=COL[role], zorder=6)
    text(ax, xl, yl, s, role, 's', ha=ha)
def nested(ax, f):
    poly(ax, [f(0, 0), f(1, 0), f(1, TN)], 'fixe')
    poly(ax, sector(f), 'varie')
    poly(ax, [f(0, 0), f(1, 0), f(CS, SN)], 'sujet')
def xs(v, v0, v1, x0, x1):
    return x0 + (v - v0) / (v1 - v0) * (x1 - x0)
def rect(ax, x, y, w, h, role, lw=0.8):
    ax.add_patch(Rectangle((x, y), w, h, ec=COL[role], fc=FILL[role], lw=lw, zorder=2))

fig, ax = canvas(56)
X = lambda v: xs(v, 0, 0.02, 8, 70)
v = 0.01745
line(ax, [(8, 14), (70, 14)], 'fixe')
for u, t in [(0, '0'), (0.005, '0,005'), (0.01, '0,01'), (0.015, '0,015'), (0.02, '0,02')]:
    ax.plot([X(u)] * 2, [12.8, 15.2], color=COL['fixe'], lw=0.8)
    text(ax, X(u), 9, t, 'fixe', 's')
brace(ax, X(0), X(v), 19, 'varie', '1° = π/180 rad ≈ 0,01745', down=False)
brace(ax, X(0), X(v), 33, 'sujet', 'sin 1° ≈ 0,01745', down=False)
line(ax, [(X(v), 15), (X(v), 33)], 'resultat', lw=0.8, dash=True)
disc(ax, X(v), 14, 1.5, 'resultat')
text(ax, 44, 50, 'un seul nombre, deux rôles', 'encre', 'm')
save(fig, '29-125')
