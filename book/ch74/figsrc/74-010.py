import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def ngon(c, ang0, n, s):
    ext = 360 / n; pts = [c]; p = c; d = ang0
    for _ in range(n - 1):
        p = (p[0] + s * math.cos(math.radians(d)), p[1] + s * math.sin(math.radians(d))); pts.append(p); d += ext
    return pts
fig, ax = canvas(62)
c = (30, 31)
for k in range(3): poly(ax, ngon(c, k * 108, 5, 15), 'sujet')
R = 17
gap = [c] + [(c[0] + R * math.cos(math.radians(324 + t)), c[1] + R * math.sin(math.radians(324 + t))) for t in range(0, 37, 6)]
poly(ax, gap, 'limite')
text(ax, c[0] + 22, c[1] - 6, '36°', 'limite', 's')
text(ax, 68, 50, '360 ÷ 108', 'encre', 'm'); text(ax, 68, 43, '≈ 3,33', 'limite', 'l')
text(ax, 68, 34, '3 × 108 = 324', 'sujet', 's'); text(ax, 68, 27, 'trou de 36°', 'limite', 's')
text(ax, 68, 17, 'pas un entier', 'limite', 'm')
save(fig, '74-010')
