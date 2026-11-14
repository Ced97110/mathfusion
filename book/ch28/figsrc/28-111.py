import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def pt(cx, cy, R, a): return (cx + R * math.cos(math.radians(a)), cy + R * math.sin(math.radians(a)))
def ucirc(ax, cx, cy, R, ext=3):
    disc(ax, cx, cy, R, 'fixe', fill=False, lw=0.8)
    line(ax, [(cx - R - ext, cy), (cx + R + ext, cy)], 'fixe', lw=0.6)
    line(ax, [(cx, cy - R - ext), (cx, cy + R + ext)], 'fixe', lw=0.6)
def arcp(ax, cx, cy, r, a0, a1, role, lw=1.0):
    line(ax, [pt(cx, cy, r, a0 + (a1 - a0) * i / 40) for i in range(41)], role, lw)
def dot(ax, p, role, r=1.1): ax.add_patch(Circle(p, r, ec=COL[role], fc=COL[role], zorder=4))
def wedge(ax, cx, cy, R, a0, a1, role):
    poly(ax, [(cx, cy)] + [pt(cx, cy, R, a0 + (a1 - a0) * i / 30) for i in range(31)], role)

fig, ax = canvas(64)
cs = [15, 44, 73]; r = 11; cyy = 33
cfg = [(['III', 'IV'], 'sujet', 'sin < 0', 'III ou IV'), (['I', 'III'], 'varie', 'tan > 0', 'I ou III'), (['III'], 'resultat', 'les deux', 'III seul')]
W_ = {'I': (0, 90), 'II': (90, 180), 'III': (180, 270), 'IV': (270, 360)}
for c, (qs, role, t1, t2) in zip(cs, cfg):
    for q in qs: wedge(ax, c, cyy, r, *W_[q], role)
    ucirc(ax, c, cyy, r, ext=1.5)
    text(ax, c, 54, t1, role, 'm', weight='bold')
    text(ax, c, 11, t2, role, 's')
text(ax, 29.5, 33, '+', 'encre', 'l'); text(ax, 58.5, 33, '=', 'encre', 'l')
text(ax, 44, 4.5, 'on s’arrête : un seul quadrant', 'encre', 's')
save(fig, '28-111')
