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
X = lambda v: xs(v, 0, 0.6, 8, 70)
text(ax, 44, 51, 'écart relatif = 1 − sin θ / θ', 'encre', 'm')
text(ax, 44, 45, 'pour θ = 0,1', 'fixe', 's')
rect(ax, X(0), 31, X(0.5) - X(0), 6, 'sujet')
text(ax, X(0) + 2, 34, 'borne 1 − cos θ = 0,5 %', 'sujet', 's', ha='left')
rect(ax, X(0), 20, X(0.2) - X(0), 6, 'varie')
text(ax, X(0.2) + 2, 23, 'écart réel ≈ 0,2 %', 'varie', 's', ha='left')
line(ax, [(X(0), 14), (X(0.6), 14)], 'fixe')
for v, t in [(0, '0'), (0.2, '0,2'), (0.4, '0,4'), (0.6, '0,6')]:
    ax.plot([X(v)] * 2, [13, 15], color=COL['fixe'], lw=0.8)
    text(ax, X(v), 9.5, t, 'fixe', 's')
text(ax, X(0.6) + 8, 14, 'en %', 'fixe', 's')
save(fig, '29-124')
