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

fig, ax = canvas(68)
f = geo(6, 14, 44)
poly(ax, [f(0, 0), f(1, 0), f(1, TN)], 'fixe')
poly(ax, [f(0, 0), f(CS, 0), f(CS, SN)], 'sujet')
for x in (CS, 1):
    line(ax, [f(x - 0.04, 0), f(x - 0.04, 0.04), f(x, 0.04)], 'fixe', lw=0.6)
arc = arcpts(lambda x, y: (6 + x * 8, 14 + y * 8), 0, TH)
line(ax, arc, 'varie', lw=1.0)
text(ax, 17, 17.5, 'θ', 'varie', 's')
text(ax, f(CS, SN / 2)[0] - 1.5, f(CS, SN / 2)[1] + 2, 'sin θ', 'sujet', 's', ha='right')
text(ax, f(CS / 2, 0)[0], 11, 'cos θ', 'sujet', 's')
brace(ax, f(0, 0)[0], f(1, 0)[0], 7.5, 'fixe', 'OA = 1')
text(ax, f(1, TN / 2)[0] + 1.5, f(1, TN / 2)[1], 'tan θ', 'fixe', 's', ha='left')
text(ax, 72, 54, 'deux triangles\nde même forme', 'varie', 's')
text(ax, 44, 62, 'tan θ = sin θ / cos θ', 'resultat', 'l')
text(ax, 72, 46, 'même angle θ', 'varie', 's')
save(fig, '29-117')
