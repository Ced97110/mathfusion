import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arcpts(cx, cy, r, a0, a1, n=60):
    return [(cx + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), cy + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
fig, ax = canvas(78)
cx, cy, R = 34, 39, 30
t = math.radians(180 / math.pi)
disc(ax, cx, cy, R, 'fixe', fill=False)
A = (cx + R, cy)
B = (cx + R * math.cos(1), cy + R * math.sin(1))
line(ax, [(cx, cy), A], 'sujet', lw=1.6)
line(ax, [(cx, cy), B], 'sujet', lw=1.6)
line(ax, arcpts(cx, cy, R, 0, 180 / math.pi, 60), 'varie', lw=2.6)
line(ax, arcpts(cx, cy, 8, 0, 180 / math.pi, 30), 'resultat', lw=1.2)
disc(ax, cx, cy, 0.8, 'encre')
text(ax, cx - 3, cy - 3, r'$O$', 'encre', 'm')
text(ax, A[0] + 3, A[1] - 1, r'$A$', 'encre', 'm', ha='left')
text(ax, B[0] + 1, B[1] + 4, r'$B$', 'encre', 'm')
text(ax, (cx + A[0]) / 2, cy - 4, r'$r$', 'sujet', 'm')
text(ax, cx + B[0] * 0 + (B[0] - cx) / 2 - 4, cy + (B[1] - cy) / 2 + 2, r'$r$', 'sujet', 'm')
text(ax, A[0] - 3, cy + 17, r'$r$', 'varie', 'm', ha='right') if False else None
text(ax, 76, 52, r'arc $AB$ : $r$', 'varie', 's', ha='right') if False else None
text(ax, cx + R * math.cos(0.5) + 6, cy + R * math.sin(0.5) + 3, r'arc : $r$', 'varie', 's', ha='left')
text(ax, cx + 13, cy + 3.5, '1 radian', 'resultat', 's', ha='left')
save(fig, '29-015')
