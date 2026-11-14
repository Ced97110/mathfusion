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

fig, ax = canvas(60)
X = lambda v: xs(v, 0.8, 1.0, 8, 76)
text(ax, 44, 54, 'la zone se resserre sur 1', 'encre', 'm')
line(ax, [(X(1), 9), (X(1), 47)], 'fixe', dash=True)
line(ax, [(8, 9), (76, 9)], 'fixe')
for v, t in [(0.8, '0,8'), (0.85, '0,85'), (0.9, '0,9'), (0.95, '0,95'), (1.0, '1')]:
    ax.plot([X(v)] * 2, [8, 10], color=COL['fixe'], lw=0.8)
    text(ax, X(v), 4.5, t, 'fixe', 's')
rows = [(40, 'θ = 0,6', CS, SN / TH, 'cos θ ≈ 0,825', 'sin θ / θ ≈ 0,941'),
        (22, 'θ = 0,1', 0.995, 0.998, 'cos θ ≈ 0,995', 'sin θ / θ ≈ 0,998')]
for y, t, c, r, lc, lr in rows:
    text(ax, 8, y + 7.5, t, 'encre', 's', ha='left')
    rect(ax, X(c), y - 3, X(1) - X(c), 6, 'resultat')
    disc(ax, X(r), y, 1.1, 'varie')
    text(ax, X(r) + (0 if c < 0.9 else 1), y + 7.5, lr, 'varie', 's', ha='center' if c < 0.9 else 'right')
    text(ax, X(c) + (6 if c < 0.9 else -1), y - 7, lc, 'sujet', 's', ha='left' if c < 0.9 else 'right')
save(fig, '29-120')
