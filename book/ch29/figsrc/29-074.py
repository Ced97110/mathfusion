import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def P(cx, cy, r, a):
    return (cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)))
def arcpts(cx, cy, r, a0, a1, n=48):
    return [P(cx, cy, r, a0 + (a1 - a0) * i / n) for i in range(n + 1)]
def sector(ax, cx, cy, r, a0, a1, role):
    poly(ax, [(cx, cy)] + arcpts(cx, cy, r, a0, a1), role)
fig, ax = canvas(66)
cx, cy, R = 44, 27, 18; a1 = math.degrees(1)
disc(ax, cx, cy, R, 'fixe', fill=False)
for a0, role in [(10, 'sujet'), (100, 'autre')]:
    sector(ax, cx, cy, R, a0, a0 + a1, role)
    line(ax, arcpts(cx, cy, R, a0, a0 + a1), 'varie', lw=2.4)
    x, y = P(cx, cy, 10, a0 + a1 / 2); text(ax, x, y, '1 rad', role, 's')
text(ax, cx, cy - 4, r'$O$', 'encre', 'm')
# rotation arrow: arc from the blue angle to the purple angle, outside the circle
pts = arcpts(cx, cy, 24, 38, 130)
line(ax, pts[:-3], 'varie', lw=1.6)
arrow(ax, pts[-4], pts[-1], 'varie', lw=1.6)
text(ax, cx, 59, 'rotation autour de O', 'varie', 's')
text(ax, cx, 5, 'arcs superposés : égaux', 'resultat', 'm', weight='bold')
save(fig, '29-074')
