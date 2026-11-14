import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arcpts(cx, cy, r, a0, a1, n=60):
    return [(cx + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), cy + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
fig, ax = canvas(76)
cx, cy, R = 44, 34, 24
a0, a1 = 20, 110
line(ax, arcpts(cx, cy, R, a1, a0 + 360, 120), 'fixe', lw=1.0)
line(ax, arcpts(cx, cy, R, a0, a1, 60), 'varie', lw=3.0)
A = (cx + R * math.cos(math.radians(a0)), cy + R * math.sin(math.radians(a0)))
B = (cx + R * math.cos(math.radians(a1)), cy + R * math.sin(math.radians(a1)))
line(ax, [A, B], 'fixe', dash=True, lw=0.7)
disc(ax, A[0], A[1], 1.0, 'encre'); disc(ax, B[0], B[1], 1.0, 'encre')
text(ax, A[0] + 4, A[1] - 1, r'$A$', 'encre', 'm')
text(ax, B[0] - 3, B[1] + 3, r'$B$', 'encre', 'm')
mid = math.radians((a0 + a1) / 2)
text(ax, cx + (R + 8) * math.cos(mid) + 6, cy + (R + 8) * math.sin(mid) + 2, r'arc $AB$', 'varie', 'm')
text(ax, 50, 41, 'segment droit', 'fixe', 's')
text(ax, cx - 8, cy - 14, 'autre morceau', 'fixe', 's')
save(fig, '29-016')
