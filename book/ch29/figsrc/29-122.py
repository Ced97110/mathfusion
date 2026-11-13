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
k = 200.0
Ax, By = 54.0, 12.0
Ox = Ax - k
line(ax, [(24, 12), (60, 12)], 'fixe')
arrow(ax, (26, 12), (12, 12), 'fixe')
text(ax, 4, 6, 'vers O, hors image', 'fixe', 's', ha='left')
Pm = (Ox + k * math.cos(0.2), By + k * math.sin(0.2))
Tm = (Ax, By + k * math.tan(0.2))
line(ax, [(24, Tm[1] - 30 * math.tan(0.2)), Tm], 'fixe', dash=True)
line(ax, [(Pm[0], By), Pm], 'sujet', lw=1.6)
line(ax, [(Ox + k * math.cos(0.2 * i / 40), By + k * math.sin(0.2 * i / 40)) for i in range(41)], 'varie', lw=1.6)
line(ax, [(Ax, By), Tm], 'resultat', lw=1.6)
text(ax, Pm[0] - 1.5, 28, 'sin θ ≈ 0,199', 'sujet', 's', ha='right')
text(ax, Ax + 2, 28, 'tan θ ≈ 0,203', 'resultat', 's', ha='left')
lead(ax, (Pm[0] + 0.3, Pm[1] + 0.3), 56, 60, 'arc θ = 0,2', 'varie')
save(fig, '29-122')
