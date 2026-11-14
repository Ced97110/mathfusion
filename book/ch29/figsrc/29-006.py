import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arcpts(cx, cy, r, a0, a1, n=60):
    return [(cx + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), cy + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
fig, ax = canvas(70)
# left: road bend, right: clock
cx1, cy1, r1 = 21, 44, 12
disc(ax, cx1, cy1, r1, 'fixe', fill=False)
poly(ax, [(cx1, cy1)] + arcpts(cx1, cy1, r1, -6, 6), 'sujet')
text(ax, 21, 62, 'virage : 500 m', 'sujet', 's')
text(ax, 21, 29, '12°', 'sujet', 's')
cx2, cy2, r2 = 67, 44, 12
disc(ax, cx2, cy2, r2, 'fixe', fill=False)
poly(ax, [(cx2, cy2)] + arcpts(cx2, cy2, r2, 90, -30), 'autre')
line(ax, [(cx2, cy2), (cx2, cy2 + r2)], 'autre', lw=1.4)
line(ax, [(cx2, cy2), arcpts(cx2, cy2, r2, -30, -30, 1)[0]], 'autre', lw=1.4)
text(ax, 67, 62, 'aiguille : 12 cm', 'autre', 's')
text(ax, 67, 29, '120°', 'autre', 's')
box(ax, 4, 6, 34, 14, 'fixe', label='× 0,01745', size='s')
box(ax, 50, 6, 34, 14, 'fixe', label='× 0,01745', size='s')
text(ax, 44, 13, 'même', 'varie', 's')
arrow(ax, (21, 27), (21, 20), 'varie')
arrow(ax, (67, 27), (67, 20), 'varie')
save(fig, '29-006')
