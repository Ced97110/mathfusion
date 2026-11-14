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

fig, ax = canvas(66)
X = lambda v: xs(v, 0, 0.8, 8, 78)
cs = CS
for y in (46, 18):
    line(ax, [(8, y), (78, y)], 'fixe')
text(ax, 8, 56, 'θ < tan θ', 'fixe', 's', ha='left')
text(ax, 8, 8, 'θ cos θ < sin θ', 'resultat', 's', ha='left')
for v, role, lab, ha, d in [(TH, 'varie', 'θ\n0,6', 'right', 1), (TN, 'fixe', 'tan θ\n0,684', 'left', 1)]:
    disc(ax, X(v), 46, 1.3, role)
    text(ax, X(v) + (-1.2 if ha == 'right' else 1.2), 52, lab, role, 's', ha=ha)
    disc(ax, X(v * cs), 18, 1.3, 'varie' if role == 'varie' else 'sujet')
    arrow(ax, (X(v), 43.5), (X(v * cs), 20.5), 'varie' if role == 'varie' else 'sujet', lw=0.8)
for v, role, lab, ha in [(TH * cs, 'varie', 'θ cos θ\n0,495', 'right'), (TN * cs, 'sujet', 'sin θ\n0,565', 'left')]:
    text(ax, X(v) + (-1.2 if ha == 'right' else 1.2), 11.5, lab, role, 's', ha=ha)
text(ax, 47, 32, '× cos θ ≈ 0,825\n(positif : ordre gardé)', 'varie', 's', ha='right')
save(fig, '29-118')
