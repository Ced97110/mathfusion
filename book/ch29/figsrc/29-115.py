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
f = geo(5, 10, 32)
nested(ax, f)
line(ax, [f(0, 0), f(1, 0)], 'fixe')
text(ax, 22, 48, 'figures emboîtées', 'encre', 's')
text(ax, 69, 48, 'aires rangées', 'encre', 's')
line(ax, [(52, 12), (52, 44)], 'fixe')
for (y, w, role, lab) in [(35, 28.2, 'sujet', 'OAP 0,282'), (24, 30.0, 'varie', 'OAP 0,3'), (13, 34.2, 'fixe', 'OAT 0,342')]:
    rect(ax, 52, y, w, 7, role)
    text(ax, 54, y + 3.5, lab, role, 's', ha='left')
save(fig, '29-115')
