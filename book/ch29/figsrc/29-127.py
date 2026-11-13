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
X = lambda v: xs(v, 0, 1, 10, 78)
v = 0.01745
text(ax, 8, 53, 'en degrés : 1 ≈ sin 1° ?', 'limite', 's', ha='left')
line(ax, [(10, 42), (78, 42)], 'fixe')
text(ax, 10, 37, '0', 'fixe', 's'); text(ax, 78, 37, '1', 'fixe', 's')
line(ax, [(X(v), 42), (78, 42)], 'limite', lw=1.4, dash=True)
text(ax, 44, 38.5, 'grand écart', 'limite', 's')
disc(ax, 78, 42, 1.4, 'limite')
text(ax, 78, 47, 'mesure : 1', 'limite', 's', ha='right')
disc(ax, X(v), 42, 1.4, 'resultat')
text(ax, 9, 47, 'sin 1° ≈ 0,01745', 'resultat', 's', ha='left')
text(ax, 8, 25, 'en radians : mesure ≈ sin 1°', 'resultat', 's', ha='left')
line(ax, [(10, 14), (78, 14)], 'fixe')
text(ax, 10, 9, '0', 'fixe', 's'); text(ax, 78, 9, '1', 'fixe', 's')
disc(ax, X(v), 14, 2.6, 'resultat', fill=False)
disc(ax, X(v), 14, 1.0, 'sujet')
text(ax, 9, 19.5, 'mesure 0,01745 = sin 1°', 'resultat', 's', ha='left')
save(fig, '29-127')
