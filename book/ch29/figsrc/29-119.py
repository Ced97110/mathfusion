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

fig, ax = canvas(62)
X = lambda v: xs(v, 0.8, 1.0, 8, 78)
text(ax, 44, 56, 'θ cos θ < sin θ < θ', 'fixe', 'l')
arrow(ax, (44, 52), (44, 44), 'varie')
text(ax, 48, 48, '÷ θ  (θ positif)', 'varie', 's', ha='left')
text(ax, 44, 39, 'cos θ < sin θ / θ < 1', 'resultat', 'l')
line(ax, [(8, 14), (78, 14)], 'fixe')
for v, t in [(0.8, '0,8'), (0.85, '0,85'), (0.9, '0,9'), (0.95, '0,95'), (1.0, '1')]:
    ax.plot([X(v)] * 2, [12.8, 15.2], color=COL['fixe'], lw=0.8)
    text(ax, X(v), 9, t, 'fixe', 's')
for v, role, lab in [(CS, 'sujet', 'cos θ ≈ 0,825'), (SN / TH, 'varie', 'sin θ / θ ≈ 0,941'), (1.0, 'fixe', '1')]:
    disc(ax, X(v), 14, 1.3, role)
    text(ax, X(v), 21, lab, role, 's', ha='center')
    line(ax, [(X(v), 15.5), (X(v), 19.3)], role, lw=0.6)
save(fig, '29-119')
