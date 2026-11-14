import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from math import cos, sin, radians
def P(cx, cy, R, a): return (cx + R * cos(radians(a)), cy + R * sin(radians(a)))
def circ(ax, cx, cy, R, ext=4):
    disc(ax, cx, cy, R, 'fixe', fill=False)
    line(ax, [(cx - R - ext, cy), (cx + R + ext, cy)], 'fixe', lw=0.6)
    line(ax, [(cx, cy - R - ext), (cx, cy + R + ext)], 'fixe', lw=0.6)
def arc(ax, cx, cy, r, a0, a1, role='varie', lw=1.0):
    n = max(8, int(abs(a1 - a0) / 4)); pts = [P(cx, cy, r, a0 + (a1 - a0) * i / n) for i in range(n + 1)]
    line(ax, pts, role, lw=lw); arrow(ax, pts[-2], pts[-1], role, lw=lw)
def dot(ax, p, role, r=1.2): ax.add_patch(Circle(p, r, ec=COL[role], fc=COL[role], zorder=6))
fig, ax = canvas(66)
text(ax, 44, 61, r'$\tan\theta = y \div x$', 'sujet', 'l')
R = 13; cy = 36
for cx, a, xs, rule, val, role in [(22, 30, 'x > 0', 'même signe : tan > 0', 'tan ≈ 0,577', 'resultat'),
                                  (66, 130, 'x < 0', 'signes contraires : tan < 0', 'tan ≈ −1,19', 'autre')]:
    circ(ax, cx, cy, R)
    p = P(cx, cy, R, a)
    line(ax, [(cx, cy), p], 'sujet', lw=1.0)
    line(ax, [p, (p[0], cy)], 'fixe', lw=0.8, dash=True)
    dot(ax, p, 'sujet')
    text(ax, cx, cy + R + 6, f'{a}°', 'sujet', 's')
    if a == 30:
        text(ax, p[0] + 1.5, (p[1] + cy) / 2 + 1, 'y > 0', 'varie', 's', ha='left')
    else:
        text(ax, p[0] - 1.5, (p[1] + cy) / 2 + 1, 'y > 0', 'varie', 's', ha='right')
    text(ax, (cx + p[0]) / 2, cy - 3.2, xs, 'varie', 's')
    text(ax, cx, 18, rule, role, 's')
    text(ax, cx, 12, val, role, 's', weight='bold')
save(fig, '28-065')
