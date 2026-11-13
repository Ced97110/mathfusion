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

fig, ax = canvas(52)
X = lambda v: xs(v, 0.5, 0.7, 8, 78)
line(ax, [(8, 12), (78, 12)], 'fixe')
for v, t in [(0.5, '0,5'), (0.55, '0,55'), (0.6, '0,6'), (0.65, '0,65'), (0.7, '0,7')]:
    ax.plot([X(v)] * 2, [10.8, 13.2], color=COL['fixe'], lw=0.8)
    text(ax, X(v), 7.5, t, 'fixe', 's')
for v, y, role, lab in [(SN, 23, 'sujet', 'sin θ ≈ 0,565'), (TH, 31, 'varie', 'θ = 0,6'), (TN, 23, 'fixe', 'tan θ ≈ 0,684')]:
    line(ax, [(X(v), 13), (X(v), y - 2)], role, lw=0.6)
    disc(ax, X(v), 12, 1.3, role)
    text(ax, X(v), y, lab, role, 's')
text(ax, 44, 44, 'sin θ < θ < tan θ', 'resultat', 'l')
save(fig, '29-116')
