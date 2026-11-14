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

fig, ax = canvas(64)
Xd = lambda d: xs(d, 0, 6, 8, 62)
Xs = lambda s: xs(s, 0, 0.12, 8, 62)
for y, X, vals in [(48, Xd, [i for i in range(7)]), (20, Xs, [0.02 * i for i in range(7)])]:
    line(ax, [(8, y), (62, y)], 'fixe')
    for u in vals:
        ax.plot([X(u)] * 2, [y - 1.2, y + 1.2], color=COL['fixe'], lw=0.8)
text(ax, 8, 44, '0', 'fixe', 's')
text(ax, 8, 16, '0', 'fixe', 's')
text(ax, Xs(0.1), 16, '0,1', 'fixe', 's')
text(ax, 71, 48, 'degrés', 'fixe', 's')
text(ax, 71, 20, 'sinus', 'fixe', 's')
disc(ax, Xd(5), 48, 1.4, 'sujet')
text(ax, Xd(5), 53, '5°', 'sujet', 'm')
arrow(ax, (Xd(5), 45), (Xs(0.08725), 23.5), 'varie')
text(ax, 58, 35, '× 0,01745', 'varie', 's', ha='left')
disc(ax, Xs(0.08716), 20, 2.6, 'resultat', fill=False)
disc(ax, Xs(0.08725), 20, 1.0, 'varie')
text(ax, 40, 9.5, 'règle : 0,08725', 'varie', 's')
text(ax, 40, 4.5, 'calculatrice : 0,08716', 'resultat', 's')
save(fig, '29-126')
